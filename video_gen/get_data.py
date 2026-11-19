import os, time
from cv_config import *
from bg_detector import bg_detect
from clear_noise import clear_noise
from findContours import find_contours
from update_tracks import update_tracks

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

    bg_subtractor_MOG2 = bg_detect()
    count_1, count_2, count_3 = int(),int(),int()

    tracks = {}
    disappeared = {}
    next_id = int()

    for i in range(n_frames):
        ret, frame = cap.read()
        mask = bg_subtractor_MOG2.apply(frame)
        clean_mask = clear_noise(mask)
        objects = find_contours(clean_mask)

        tracks, next_id, disappeared = update_tracks(tracks, objects, next_id, disappeared)
        print(tracks)

        n_object = len(objects)
        if n_object == 1: count_1 += 1
        if n_object == 2: count_2 += 1
        if n_object == 3: count_3 += 1

        if i in [50, 100, 150, 200, 250, 300, 350]:
            os.makedirs("for_mask", exist_ok = True)
            cv2.imwrite(f"for_mask/frame_{i}pcs.png", clean_mask)
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
    print(f'''
count_1: {count_1}
count_2: {count_2}
count_3: {count_3}
''')
get_data(n_frames)
cap.release()