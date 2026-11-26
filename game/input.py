"""Keyboard input: one backend per platform behind a small shared API.

    start()      -- enter single-key mode (no-op on Windows)
    stop()       -- restore the terminal (always call it, even on Ctrl+C)
    read_key()   -- last action name seen this frame, or None
"""

import os
import sys

KEY_MAP = {
    "\r": "ENTER",
    "\n": "ENTER",
    " ": "SPACE",
}


# --------------------------------------------------------------- Windows
try:
    import msvcrt

    SPECIAL_WIN = {"H": "UP", "P": "DOWN", "K": "LEFT", "M": "RIGHT"}

    def start():
        pass

    def stop():
        pass

    def _read_token():
        if not msvcrt.kbhit():
            return None
        raw = msvcrt.getwch()
        if raw in ("\x00", "\xe0"):
            return SPECIAL_WIN.get(msvcrt.getwch())
        return KEY_MAP.get(raw, raw.upper())


# ----------------------------------------------------------------- POSIX
except ImportError:
    import select
    import termios
    import tty

    SPECIAL_POSIX = {"A": "UP", "B": "DOWN", "C": "RIGHT", "D": "LEFT"}
    _saved = None

    def start():
        global _saved
        if not sys.stdin.isatty():
            raise RuntimeError(
                "stdin is not a terminal - run the game in a real terminal")
        fd = sys.stdin.fileno()
        _saved = termios.tcgetattr(fd)
        tty.setcbreak(fd)          # single key, but Ctrl+C still works

    def stop():
        if _saved is not None:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, _saved)

    def _pending(timeout=0.0):
        return bool(select.select([sys.stdin], [], [], timeout)[0])

    def _read_byte():
        return os.read(sys.stdin.fileno(), 1).decode(errors="ignore")

    def _read_token():
        if not _pending():
            return None
        raw = _read_byte()
        if raw == "\x1b":                     # arrow keys start with ESC [ X
            if not _pending(0.02):
                return None                   # a lone ESC: ignore it
            if _read_byte() != "[":
                return None
            if not _pending(0.02):
                return None
            return SPECIAL_POSIX.get(_read_byte())
        return KEY_MAP.get(raw, raw.upper())


# ---------------------------------------------------------------- shared
def read_key():
    """Return the last action name seen this frame, or None."""
    last = None
    while True:
        token = _read_token()
        if token is None:
            return last
        last = token


if __name__ == "__main__":
    import time

    start()
    print("Press keys. Ctrl+C to quit.")
    try:
        while True:
            key = read_key()
            if key:
                print(f"key: {key!r}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
    finally:
        stop()
    print("bye")