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


# --- BLUE BALL ---
blue_ball_x = 100
blue_ball_y = 100

blue_ball_x_speed = 15
blue_ball_y_speed = 10

blue_ball_x_speed_radius = 30

# --- GREEN BALL ---
green_ball_x = 250
green_ball_y = 200

green_ball_x_speed = -12
green_ball_y_speed = 8

green_ball_x_speed_radius = 25

# --- RED BALL ---
red_ball_x = 400
red_ball_y = 300

red_ball_x_speed = 10
red_ball_y_speed = -14

red_ball_x_speed_radius = 20

# --- BALLS COLORS ---
Colors = np.array(
    [
        [255,0,0] # -- Blue
        [0,255,0], # -- Green
        [0,0,255], # -- Red
    ]
)

# --- BALLS ---
Balls = {
        "blue_ball": {"x": blue_ball_x, "y": blue_ball_y, "x_speed": blue_ball_x_speed, "y_speed": blue_ball_y_speed, "radius": blue_ball_x_speed_radius, "color": Colors[0]},
        "green_ball": {"x": green_ball_x, "y": green_ball_y, "x_speed": green_ball_x_speed, "y_speed": green_ball_y_speed, "radius": green_ball_x_speed_radius, "color": Colors[1]},
        "red_ball": {"x": red_ball_x, "y": red_ball_y, "x_speed": red_ball_x_speed, "y_speed": red_ball_y_speed, "radius": red_ball_x_speed_radius, "color": Colors[2]}
        }