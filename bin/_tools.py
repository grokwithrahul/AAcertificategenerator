from bin.datahandle import getoverlays
from sentencecloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
from sketchify import sketch


def thankYouImg(name):
    image = np.zeros((200, 600, 4), np.uint8)
    text = "Thank you "+name+"!"
    fontScale, thickness = optimalScale(text, 850)
    cv2.putText(image, text, (0, 100), cv2.FONT_HERSHEY_DUPLEX, fontScale, (0, 0, 255, 255), thickness)
    return image


def optimalScale(text, width):
    thickness = 2 if len(text) > 25 else 3 if len(text) > 15 else 4
    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=scale/10, thickness=thickness)
        newWidth = textSize[0][0]
        if newWidth <= width:
            break

    return scale/10, thickness


def overlayimgs(style, photo, wordcloud, thankyou, signature, background):
    coords = getoverlays(style)
    photoxy, wordcloudxy, thankyouxy, signaturexy = tuple(coords[0]), tuple(coords[1]), tuple(coords[2]), tuple(coords[3])
    faceh, facew = 600, 600
    wordcloudh, wordlcoudw = 1500, 1500
    thankyouh, thankyouw = 600, 200
    signatureh, signaturew = 300, 150

    background[photoxy[1]: photoxy[1] + faceh, photoxy[0]: photoxy[0] + facew] = photo
    background[wordcloudxy[1]: wordcloudxy[1] + wordcloudh, wordcloudxy[0]: wordcloudxy[0] + wordlcoudw] = wordcloud
    background[thankyouxy[1]: thankyouxy[1] + thankyouh, thankyouxy[0]: thankyouxy[0] + thankyouw] = thankyou
    background[signaturexy[1]: signaturexy[1] + signatureh, signaturexy[0]: signaturexy[0] + signaturew] = signature

    return background

