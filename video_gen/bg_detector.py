import cv2

def bg_detect():
    bg_subtractor_MOG2 = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
    return bg_subtractor_MOG2