import time
TARGET_FPS = 30
FRAME_TIME = 1.0 / TARGET_FPS
TOTAL_FRAMES = 90

start = time.perf_counter()
frame = 0

while frame < TOTAL_FRAMES:
    frame_start = time.perf_counter()
    
    #game content

    work_time = time.perf_counter() - frame_start
    remaining = FRAME_TIME - work_time
    if remaining > 0:
     time.sleep(remaining)

    frame = frame + 1

elapsed = time.perf_counter() - start
print(f"{frame} frames {elapsed:.6f} s, FPS={frame/elapsed:.2f}")