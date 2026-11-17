import cv2
import numpy as np
from cv_config import *


for frame_idx in range(total_frames):
    x += x_speed
    y += y_speed

    if x >= 610 or x < 30: x_speed *= -1
    if y >= 450 or y < 30: y_speed *= -1