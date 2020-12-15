from bin.tools.datahandle import getoverlays
from .thankyou import getThankYouImg
from .signature import getSignature
import os
import cv2


def overlayImgs(style, photo, wordcloud, thankyouname, signaturename):
    coords = getoverlays(style)
    background = getBackground(style)
    background = cv2.resize(background, (1600, 2264))
    photo = cv2.cvtColor(photo, cv2.COLOR_GRAY2RGB)
    photoxy, wordcloudxy, thankyouxy, signaturexy = tuple(coords[0]), tuple(coords[1]), tuple(coords[2]), tuple(coords[3])
    background = getThankYouImg(background, thankyouname, thankyouxy[0], thankyouxy[1])
    background = getSignature(background, signaturename, signaturexy[0], signaturexy[1])
    faceh, facew = 400, 400
    wordcloudh, wordlcoudw = 1000, 1000
    thankyouh, thankyouw = 200, 600
    signatureh, signaturew = 300, 150

    background[photoxy[1]: photoxy[1] + faceh, photoxy[0]: photoxy[0] + facew] = photo
    background[wordcloudxy[1]: wordcloudxy[1] + wordcloudh, wordcloudxy[0]: wordcloudxy[0] + wordlcoudw] = wordcloud
    #background[thankyouxy[1]: thankyouxy[1] + thankyouh, thankyouxy[0]: thankyouxy[0] + thankyouw] = thankyou
    #background[signaturexy[1]: signaturexy[1] + signatureh, signaturexy[0]: signaturexy[0] + signaturew] = signature

    return background


def getBackground(stylenum):
    path = os.listdir('../bin/data/backgrounds')[stylenum-1]
    print(path)
    out = cv2.imread('../bin/data/backgrounds/'+path)

    return out
