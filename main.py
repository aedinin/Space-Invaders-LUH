import time
from game.states import State, next_state
TARGET_FPS = 30
FRAME_TIME = 1.0 / TARGET_FPS

state = State.MENU
keys = ["ENTER", "P", "P", "Q"]
index = 0
frame = 0

while state is not State.QUIT:
    key = keys[index] if index < len(keys) else None
    index = index + 1
    new_state = next_state(state,key)
    print(f"frame {frame} {state.value}-- {key} --> {new_state.value}")
    state = new_state
    frame = frame + 1

print("loop ended")