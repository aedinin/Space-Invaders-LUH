import os
import sys
import time
from game.config import TARGET_FPS, FRAME_TIME, DT_MAX, HOLD_GUARD
from game.input import read_key
from game.render import (CURSOR_HOME, HIDE_CURSOR, SHOW_CURSOR, draw_border, grid_to_text, new_grid, put_text)
from game.states import State, next_state

os.system("")

state = State.MENU
game_time = 0.0
frame = 0
last_time = time.perf_counter()
last_key = None
last_key_time = 0.0

sys.stdout.write(HIDE_CURSOR)
try:
    while state is not State.QUIT:
        frame_start = time.perf_counter()
    
        dt = frame_start - last_time        #delta time(Actual time taken for a single frame)
        last_time = frame_start
        if dt > DT_MAX:
            dt = DT_MAX
            #To avoid interference such as that which might occur when switching interface states

        key = read_key()        # real keyboard: returns an action name or None
        if key is not None:
            same = (key == last_key)
            gap = frame_start - last_key_time
            last_key = key
            last_key_time = frame_start
            if same and gap < HOLD_GUARD:
                key = None
    
        new_state = next_state(state,key)
    
        if new_state is not state:
            state = new_state

        if state is State.RUNNING:
            game_time = game_time + dt

        grid = new_grid()
        draw_border(grid)
        put_text(grid, 2, 2, "SPACE INVADERS")
        put_text(grid, 2, 4, f"state: {state.value}")
        put_text(grid, 2, 6, f"frame: {frame}")
        put_text(grid, 2, 8, f"game_time: {game_time:.2f}")
        put_text(grid, 2, 10, f"last: {new_state.value}")

        sys.stdout.write(CURSOR_HOME + grid_to_text(grid))
        sys.stdout.flush()

        sleep_time = FRAME_TIME - (time.perf_counter() - frame_start)
        if sleep_time > 0:
            time.sleep(sleep_time)

        frame = frame + 1
finally:
    sys.stdout.write(SHOW_CURSOR)

print(f"\nloop ended, game_time {game_time:.2f}")