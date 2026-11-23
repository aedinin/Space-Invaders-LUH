import time

start = time.perf_counter()
frame = 0
while frame < 90:
    frame = frame + 1
    
elapsed = time.perf_counter() - start
print(f"{frame} frames {elapsed:.6f} s, FPS={frame/elapsed:.2f}")