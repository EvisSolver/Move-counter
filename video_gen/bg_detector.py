import cv2

def bg_detect(frame):
    bg_subtractor_MOG2 = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
    mask = bg_subtractor_MOG2.apply(frame)
    return mask