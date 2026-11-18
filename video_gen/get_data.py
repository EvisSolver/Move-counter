import os, time
from cv_config import *

# --- VIDEO ---
cap = cv2.VideoCapture("test.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(fps, w, h, n_frames)

def get_data(n_frames):
    percent_steps = {}

    mile_stones = {
        0: 0,
        int(n_frames * 0.25): 25,
        int(n_frames * 0.50): 50,
        int(n_frames * 0.75): 75
    }
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    start = time.perf_counter()
    for i in range(n_frames):
        ret, frame = cap.read()
        if i in mile_stones:
            if not ret: break
            os.makedirs("out", exist_ok = True)
            percent = mile_stones[i]
            percent_steps[percent] = i
            cv2.imwrite(f"out/frame_{percent}pcs.png", frame)
    elapsed = time.perf_counter() - start
    read_fps = n_frames / elapsed
    print(f"FPS read: {read_fps:.2f}")
    print(elapsed)
get_data(n_frames)
cap.release()