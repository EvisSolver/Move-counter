import numpy as np
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

x = 100
y = 100

x_speed = 15
y_speed = 10

radius = 30

Colors = np.array(
    [
        [0,0,255],
        [0,255,0],
        [255,0,0]
    ]
)


Balls = [
    {
        "blue_ball": {}
    }
]