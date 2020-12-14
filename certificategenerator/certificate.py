from sketchify import sketch
from ..bin import _tools
#from sentencecloud_generator import x
import os

class certificate():
    def __init__(self):
        self.style = 1
        self.csvpath = False
        self.imgpath = False
        self.configdone = False

    def config(self, csvpath, imgpath, name, **kwargs):
        self.csvpath = csvpath
        self.imgpath = imgpath
        self.name = name
        self.style = kwargs.get("style")
        self.configdone = True

    def error_handler(self):
        if not self.configdone:
            raise Exception('[Errno 1] Config not run')
        if not os.path. exists(self.csvpath) or os.path.exists(self.imgpath):
            raise FileNotFoundError('[Errno 2] File at specified path does not exist')

    def generate(self):
        self.error_handler()
        image = sketch.normal_sketch(self.imgpath)
        thankyou = _tools.thankYouImg(self.name)
        #wordcloud = x

monke = certificate()
monke.config('oozma', 'kappa')
monke.generate()
