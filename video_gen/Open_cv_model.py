import cv2
import numpy as np
from cv_config import *


def move_ball(ball_name, frame):
    ball = Balls[ball_name]

    # -- X
    if Balls[f"{ball_name}"]["x"] >= (Params["width"] - Balls[f"{ball_name}"]["radius"]) \
    or Balls[f"{ball_name}"]["x"] <= Balls[f"{ball_name}"]["radius"]: Balls[f"{ball_name}"]["x_speed"] *= -1

    # -- Y
    if Balls[f"{ball_name}"]["y"] >= (Params["height"] - Balls[f"{ball_name}"]["radius"]) \
    or Balls[f"{ball_name}"]["y"] <= Balls[f"{ball_name}"]["radius"]: Balls[f"{ball_name}"]["y_speed"] *= -1

    Balls[f"{ball_name}"]["x"] += Balls[f"{ball_name}"]["x_speed"]
    Balls[f"{ball_name}"]["y"] += Balls[f"{ball_name}"]["y_speed"]

    cv2.circle(frame, (ball["x"], ball["y"]), ball["radius"], ball["color"], -1)
    cv2.line(frame, (line_x, 0), (line_x, Params["height"]), (255,255,255), 1)

for frame_idx in range(total_frames):
    frame = np.full(
        (
            Params["height"],
            Params["width"],
            3
        ), 
        (40, 40, 40), dtype = np.uint8
    )
    for ball_name in Balls: move_ball(ball_name, frame)
    out_video.write(frame)
out_video.release()