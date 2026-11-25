import time
from game.config import TARGET_FPS, FRAME_TIME, DT_MAX, HOLD_GUARD
from game.input import read_key
from game.states import State, next_state

state = State.MENU
game_time = 0.0
frame = 0
last_time = time.perf_counter()
last_key = None
last_key_time = 0.0

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
        print(f"[{frame / TARGET_FPS:.1f}s] {state.value} --> {new_state.value}")
        state = new_state

    if state is State.RUNNING:
        game_time = game_time + dt

    if frame % 15 == 0:     #Executed every 15 frames (approximately 0.5 seconds)
        print(f"frame={frame} state={state.value} game_time={game_time:.2f} dt={dt:.3f}")

    sleep_time = FRAME_TIME - (time.perf_counter() - frame_start)
    if sleep_time > 0:
        time.sleep(sleep_time)

    frame = frame + 1

print(f"loop ended, game_time {game_time:.2f}")