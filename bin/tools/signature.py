import numpy as np
import cv2

def getSignature(image, name, coordx, coordy):
    #image = np.zeros((200, 300, 4), np.uint8)
    fontScale = optimalScale(name, 300)
    cv2.putText(image, name, (coordx, coordy), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale, (255, 255, 255, 255), 4)
    return image


def optimalScale(text, width):
    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=scale/10, thickness=4)
        newWidth = textSize[0][0]
        if newWidth <= width:
            break

    return scale/10
