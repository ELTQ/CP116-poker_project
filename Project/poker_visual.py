import cv2 as cv
import pandas as pd
import numpy as np
import torch
import math

f = open("cards.txt")
cards = f.readlines()
cards = [c.replace('\n', '') for c in cards]
print(cards)

def preprocess(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image
img = cv.imread("Training_images\heart.png")
img = preprocess(img)
cv.imshow("Heart", img)

poker = cv.imread("Testing_images\king_of_clubs2.png")
poker = cv.resize(poker,(250, 350))
canny = cv.Canny(poker,100,200)
cropped = canny[5:75, 2:35]

cv.imshow("Poker", poker)
cv.imshow("Canny", canny)
cv.imshow("Cropped", cropped)
k = cv.waitKey(0)
