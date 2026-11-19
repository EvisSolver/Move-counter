import cv2
def find_contours(clean_mask):
    objects = []
    contours, _ = cv2.findContours(clean_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) < 200: continue
        x,y,w,h = cv2.boundingRect(cnt)
        cx = x + w // 2
        cy = y + h // 2

        objects.append((cx, cy))
    return objects