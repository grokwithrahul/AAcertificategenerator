from sketchify import sketch
import cv2


def getSketch(imagePath):
    sketched = sketch.normal_sketch(imagePath)
    out = cv2.resize(sketched, (400, 400))
    return out
