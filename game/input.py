"""Keyboard input. Windows backend (msvcrt); POSIX backend TODO."""

try:
    import msvcrt

    def _read_raw():
        """Return one raw character, or None if no key is waiting."""
        if not msvcrt.kbhit():
            return None
        return msvcrt.getwch()
    
    def _read_blocking():
        return msvcrt.getwch()

except ImportError:          # Linux/macOS: not supported yet
    def _read_raw():
        return None

    def _read_blocking():
        return None


KEY_MAP = {
    "\r": "ENTER",
    "\n": "ENTER",
    " ": "SPACE",
}

SPECIAL_KEYS = {
    "H": "UP",
    "P": "DOWN",
    "K": "LEFT",
    "M": "RIGHT",
}

def read_key():
    """Return the last key pressed this frame as an action name, or None."""
    last = None
    while True:
        raw = _read_raw()
        if raw is None:
            return last

        if raw in ("\x00", "\xe0"):
            code = _read_blocking()
            if code is not None:
                special = SPECIAL_KEYS.get(code)
                if special:
                    last = special
            continue

        last = KEY_MAP.get(raw, raw.upper())


if __name__ == "__main__":
    import time

    print("Press keys. Ctrl+C to quit.")
    try:
        while True:
            key = read_key()
            if key:
                print(f"key: {key!r}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        print("bye")