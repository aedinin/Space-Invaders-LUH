import time
from game.states import State, next_state
from game.config import TARGET_FPS, FRAME_TIME, DT_MAX, TOTAL_FRAMES

script = {30: "ENTER", 90: "P", 150: "P", 240: "Q"}     #Simulate keyboard input at a specific point in time

state = State.MENU
game_time = 0.0
frame = 0
last_time = time.perf_counter()

while state is not State.QUIT and frame < TOTAL_FRAMES:
    frame_start = time.perf_counter()
    
    dt = frame_start - last_time        #delta time(Actual time taken for a single frame)
    last_time = frame_start
    if dt > DT_MAX:
        dt = DT_MAX
        #To avoid interference such as that which might occur when switching interface states

    key = script.get(frame)     #Simulate keyboard input at a specific point in time
    new_state = next_state(state,key)
    if new_state is not state:
        print(f"[{frame/30:.1f}s] {state.value} --> {new_state.value}")
        state = new_state

    if state is State.RUNNING:
        game_time = game_time + dt
        #displacement += velocity * dt

    if frame % 15 == 0:     #Executed every 15 frames (approximately 0.5 seconds)
        print(f" frame={frame} state={state.value} game_time={game_time:.2f} dt={dt:.3f}")

    sleep_time = FRAME_TIME - (time.perf_counter() - frame_start)
    if sleep_time > 0:
        time.sleep(sleep_time)

    frame = frame + 1

print(f"loop ended, gametime {game_time:.2f}")