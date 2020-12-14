from bin.tools.datahandle import getoverlays
import os
import cv2


def overlayImgs(style, photo, wordcloud, thankyou, signature):
    coords = getoverlays(style)
    background = getBackground(style)
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


def getBackground(stylenum):
    path = os.listdir('../data/backgrounds')[stylenum-1]
    out = cv2.imread(path)

    return out
