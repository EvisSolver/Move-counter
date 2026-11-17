import cv2
import numpy as np
from cv_config import *


for frame_idx in range(total_frames):
    


    
def move_ball(ball_name):
    if Balls[f"{ball_name}"]["x"] >= (Params["width"] - Balls[f"{ball_name}"]["radius"]) \
    or Balls[f"{ball_name}"]["x"] <= Balls[f"{ball_name}"]["radius"]: Balls[f"{ball_name}"]["x_speed"] *= -1

    if Balls[f"{ball_name}"]["y"] >= (Params["height"] - Balls[f"{ball_name}"]["radius"]) \
    or Balls[f"{ball_name}"]["y"] <= Balls[f"{ball_name}"]["radius"]: Balls[f"{ball_name}"]["y_speed"] *= -1
    Balls[f"{ball_name}"]["x"] += Balls[f"{ball_name}"]["x_speed"]
    Balls[f"{ball_name}"]["y"] += Balls[f"{ball_name}"]["y_speed"]