"""Game: main loop, state machine, per-frame update and render."""
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

class game:
    """Holds the whole game state and drives one frame at a time."""
    
    
    def __init__(self):
        self.state = State.MENU
        game_time = 0.0
        frame = 0
        last_time = time.perf_counter()
        last_key = None
        last_key_time = 0.0

        ship_x = WIDTH / 2 


    def run(self):
        """Hide the cursor, play until QUIT, always restore the cursor."""
        sys.stdout.write(HIDE_CURSOR)
        try:
            self.loop()
        finally:
            sys.stdout.write(SHOW_CURSOR)
        print(f"\nloop ended, game_time {game_time:.2f}")


    def loop(self):
            while self.state is not State.QUIT:
            self.step()
            
            
        def step(self):
            """One frame: time -> input -> state -> update -> render -> throttle."""
            frame_start = time.perf_counter()

            # delta time: seconds since the previous frame, capped to survive stalls
            dt = frame_start - self,last_time
            self.last_time = frame_start
            if dt > DT_MAX:
                dt = DT_MAX
                #To avoid interference such as that which might occur when switching interface states


        key = self.read_imput()       # real keyboard: returns an action name or None
        self.handle_key(key)
        self.update(dt, key)
        self.render()
        
        # sleep away whatever is left of this frame's budget
        sleep_time = FRAME_TIME - (time.perf_counter() - frame_start)
        if sleep_time > 0:
            time.sleep(sleep_time)

        self.frame = self.frame + 1


        def read_input(self):
            """Read one key; ignore auto-repeat for action keys."""
            key = read_key()
            if key is not None:
                return None

            now = time.perf_counter()
            same = (key == self.last_key)
            gap = now - self.last_key_time
            self.last_key = key
            self.last_key_time = now

        
            # holding P must not toggle pause 30 times per second
            if same and gap < HOLD_GUARD and key in ACTION_KEYS:
                return None
            return key
    
    def handle_key(self, key):
        """Let the state machine decide whether this key changes the state."""
        new_state = next_state(self.state, key)
        if new_state is not self.state:
            self.state = new_state

    def update(self, dt, key):
        """Advance the world; skipped entirely unless the game is running."""
        if self.state is not State.RUNNING:
            return

        self.game_time = self.game_time + dt

        if key == "LEFT":
            self.ship_x = self.ship_x - SHIP_SPEED * dt
        if key == "RIGHT":
            self.ship_x = self.ship_x + SHIP_SPEED * dt

        if self.ship_x < 2:
            self.ship_x = 2
        if self.ship_x > WIDTH - 3:
            self.ship_x = WIDTH - 3

    def render(self):
        """Build the frame in memory, then write it in one go."""
        grid = new_grid()
        draw_border(grid)
        put_text(grid, 2, 2, "SPACE INVADERS")
        put_text(grid, 2, 4, f"state: {self.state.value}")
        put_text(grid, 2, HEIGHT - 3,
                 f"frame: {self.frame}  game_time: {self.game_time:.1f}")
        draw_ship(grid, int(self.ship_x))

        if self.state is State.MENU:
            draw_overlay(grid, "PRESS ENTER TO START")
        elif self.state is State.PAUSED:
            draw_overlay(grid, "PAUSED - PRESS P TO RESUME")
        elif self.state is State.GAME_OVER:
            draw_overlay(grid, "GAME OVER - PRESS R")

        sys.stdout.write(CURSOR_HOME + grid_to_text(grid))
        sys.stdout.flush()