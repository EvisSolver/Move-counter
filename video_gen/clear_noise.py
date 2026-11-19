import cv2
def clear_noise(mask):
    kernel_for_MORPH_OPEN = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    kernel_for_MORPH_DILATE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    clear_n = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_for_MORPH_OPEN)
    clean_circles = cv2.morphologyEx(clear_n, cv2.MORPH_OPEN, kernel_for_MORPH_DILATE)
    return clean_circles