import os
import sys
import time

from game.config import (ACTION_KEYS, DT_MAX, FRAME_TIME, HEIGHT, HOLD_GUARD,
                         SHIP_SPEED, TARGET_FPS, WIDTH)
from game.input import read_key
from game.render import (CURSOR_HOME, HIDE_CURSOR, SHOW_CURSOR, draw_border,
                         draw_overlay, draw_ship, grid_to_text, new_grid,
                         put_text)
from game.states import State, next_state

os.system("")

state = State.MENU
game_time = 0.0
frame = 0
last_time = time.perf_counter()
last_key = None
last_key_time = 0.0

ship_x = WIDTH / 2 

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
            if same and gap < HOLD_GUARD and key in ACTION_KEYS:
                key = None
    
        new_state = next_state(state,key)
    
        if new_state is not state:
            state = new_state

        if state is State.RUNNING:
            game_time = game_time + dt
            if key == "LEFT":
                ship_x = ship_x - SHIP_SPEED * dt
            if key == "RIGHT":
                ship_x = ship_x + SHIP_SPEED * dt
            if ship_x < 2:
                ship_x = 2
            if ship_x > WIDTH - 3:
                ship_x = WIDTH -3

        grid = new_grid()
        draw_border(grid)
        put_text(grid, 2, 2, "SPACE INVADERS")
        put_text(grid, 2, 4, f"state: {state.value}")
        put_text(grid, 2, HEIGHT - 3, f"frame: {frame} game_time:{game_time:.1f}")
        put_text(grid, 2, 10, f"last: {new_state.value}")
        draw_ship(grid, int(ship_x))

        if state is State.MENU:
            draw_overlay(grid, "PRESS ENTER TO START")
        elif state is State.PAUSED:
            draw_overlay(grid, "PAUSED - PRESS P TO RESUME")
        elif state is State.GAME_OVER:
            draw_overlay(grid, "GAME OVER - PRESS R")

        sys.stdout.write(CURSOR_HOME + grid_to_text(grid))
        sys.stdout.flush()
               
        sleep_time = FRAME_TIME - (time.perf_counter() - frame_start)
        if sleep_time > 0:
            time.sleep(sleep_time)

        frame = frame + 1
finally:
    sys.stdout.write(SHOW_CURSOR)

print(f"\nloop ended, game_time {game_time:.2f}")