# Space Invaders - GIP Spieleprojekt (WiSe 26/27)

Terminal-based Space Invaders in Python 3, standard library only (no GUI
framework). The whole game is drawn as a character grid inside the terminal.

## Requirements

- Python 3.10 or newer (`python` on Windows, `python3` on Linux/macOS)
- A real terminal, at least 20 rows high (the playfield is 41x18 characters)
- No third-party packages

## Run

    python main.py

## Controls

| Key | Action |
|---|---|
| `ENTER` | start the game from the menu |
| `LEFT` `RIGHT` | move the ship |
| `P` | pause / resume |
| `Q` | quit |
| `R` | back to the menu after game over |

## Structure

    main.py          entry point: enables ANSI escapes, starts Game
    game/game.py     Game class: fixed-step loop, dt, state handling
    game/states.py   State enum + next_state() transition table
    game/input.py    keyboard -> action names (Windows: msvcrt, POSIX: termios)
    game/render.py   character grid helpers + ANSI screen handling
    game/config.py   every tunable constant (fps, field size, ship speed)

## Team

- Long Teng
- <name>
- <name>
- <name>
- <name>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and pull request workflow.