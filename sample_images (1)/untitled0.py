# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:22:16 2021

@author: SEC
"""

import cv2
import glob

def resize_image(image, w= 300, h= 300):
    img_color = cv2.imread(image, 1)
    img_cnew = cv2.resize(img_color, (w, h))
    fname_new =image[:-4] + "_resized.jpg"
    cv2.imwrite(fname_new, img_cnew)

def display_new_image():
    new_imgs = glob.glob("*_resized.jpg")
    for new_image in new_imgs:
        new_image_color = cv2.imread(new_image, 1)
        cv2.imshow('check images', new_image_color)
        cv2.waitKey(2000) # 0: press button; 2000: 2 seconds
    cv2.destroyAllWindows()
    
def main():
    imgs = glob.glob("*.jpg")
    for image in imgs:
        resize_image(image)
    display_new_image()
    
main()