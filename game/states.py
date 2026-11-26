from enum import Enum

class State(Enum):
    MENU = "menu"
    RUNNING = "running"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    QUIT = "quit"

def next_state(state, key):
    if state is State.MENU:
        if key == "ENTER":
            return State.RUNNING
        if key == "Q":
            return State.QUIT
    elif state is State.RUNNING:
        if key == "P":
            return State.PAUSED
        if key == "Q":
            return State.QUIT
    elif state is State.PAUSED:
        if key == "P":
            return State.RUNNING
        if key == "Q":
            return State.QUIT
    elif state is State.GAME_OVER:
        if key == "R":
            return State.MENU
        if key == "Q":
            return State.QUIT

    return state





