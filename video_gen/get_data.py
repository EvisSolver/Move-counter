import os
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
    
    for i in range(n_frames):
        if i in mile_stones:
            ret, frame = cap.read()
            if not ret: break
            os.makedirs("out", exist = True)
            cv2.imwrite(f"out/frame_{percent}pcs.png")
            percent = mile_stones[i]
            percent_steps[percent] = i
get_data(n_frames)
cap.release()