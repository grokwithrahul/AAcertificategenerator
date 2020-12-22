from certificategenerator import certificate
import cv2
import os

test = certificate.certificate()
csvpath = './test.csv'
impath = './impath.csv'
test.config(csvpath, impath, "Barack", signaturename="Rahul", style=1)
a = test.generate()
cv2.imwrite('tes.jpg', a)
