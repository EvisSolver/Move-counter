import cv2
def clear_noise(mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    clear_n = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return clear_n