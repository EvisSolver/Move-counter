import cv2, math
def update_tracks(tracks, objects, next_id, max_dist=50):
    used_objects = set()

    for track_id, old_pos in tracks.items():
        best_dist = max_dist
        best_idx = None
        best_pos = None

        for idx, new_pos in enumerate(objects):
            if idx in used_objects:continue
            dist = math.hypot(new_pos[0] - old_pos[0], new_pos[1] - old_pos[1])
            if dist < best_dist:
                best_dist = dist
                best_idx = idx
                best_pos = new_pos
        if best_idx is not None:
            used_objects.add(best_idx)
            tracks[track_id] = best_pos
    for idx, new_pos in enumerate(objects):
        if idx not in used_objects: 
            tracks[next_id] = new_pos
            next_id += 1
    return tracks, next_id