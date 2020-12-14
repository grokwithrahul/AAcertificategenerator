from sketchify import sketch
import cv2


def getSketch(imagePath):
    image = cv2.imread(imagePath)
    out = cv2.resize(sketch.normal_sketch(image), (600, 600))
    return out
