import cv2

Params = {
    "width": 640,
    "height": 480
} # -- X, Y

fps = 24
video_duration = 10

codec = cv2.VideoWriter_fourcc(*'mp4v')
out_video = cv2.VideoWriter('test.mp4', codec, fps, (Params['width'], Params['height']))

total_frames = video_duration * fps


