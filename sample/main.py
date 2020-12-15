from certificategenerator import certificate
import cv2
import os

monke = certificate.certificate()
csvpath = './test.csv'
impath = './impath.csv'
monke.config(csvpath, impath, "Barack", signaturename="Rahul", style=1)
a = monke.generate()
cv2.imwrite('tes.jpg', a)