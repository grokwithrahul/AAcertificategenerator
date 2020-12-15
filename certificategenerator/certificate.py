from sketchify import sketch
from bin.tools import thankyou as ty
from bin.tools import sketch as imgsketch
from bin.tools import signature as signaturegen
from bin.tools import wordcloud as wc
from bin.tools import _tools
import cv2
#from sentencecloud_generator import x
import os


class certificate():
    def __init__(self):
        self.style = 1
        self.csvpath = False
        self.imgpath = False
        self.configdone = False
        self.tyname = False
        self.signaturename = ""

    def config(self, csvpath, imgpath, thankyouname, **kwargs):
        self.csvpath = csvpath
        self.imgpath = imgpath
        self.tyname = thankyouname
        self.style = kwargs.get("style")
        self.signaturename = kwargs.get("signaturename")
        self.configdone = True

    def error_handler(self):
        if not self.configdone:
            raise Exception('[Errno 1] Config not run')
        if not os.path.exists(self.csvpath):
            raise FileNotFoundError('[Errno 2] CSV File at specified path does not exist')
        if not os.path.exists(self.imgpath):
            raise FileNotFoundError('[Errno 3] Image File at specified path does not exist')

    def generate(self):
        self.error_handler()
        image = imgsketch.getSketch(self.imgpath)
        #wordcloud = wc.createWordCloud(self.csvpath)
        wordcloud = cv2.imread('out.png')
        wordcloud = cv2.resize(wordcloud, (1000, 1000))
        #cv2.imsave('wc.png', wordcloud)
        out = _tools.overlayImgs(self.style, image, wordcloud, thankyouname=self.tyname, signaturename=self.signaturename)
        return out



