import numpy as np
import cv2


def getThankYouImg(image, name, coordx, coordy):
    #image = np.zeros((200, 600, 4), np.uint8)
    text = "Thank you "+name+"!"
    fontScale, thickness = getOptimalScale(text, 800)
    cv2.putText(image, text, (coordx, coordy), cv2.FONT_HERSHEY_TRIPLEX, fontScale, (0, 0, 0, 0), thickness)
    return image


def getOptimalScale(text, width):
    thickness = 2 if len(text) > 25 else 3 if len(text) > 15 else 4
    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=scale/10, thickness=thickness)
        newWidth = textSize[0][0]
        if newWidth <= width:
            break

    return scale/10, thickness