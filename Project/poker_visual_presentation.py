import joblib
from poker_visual import preprocess
import cv2 as cv
from poker_solver import Card
p_model = joblib.load('model.pkl')

Done = False
while not Done:
    img = input("Enter the path for the card: ")
    pred = p_model.predict(preprocess(cv.imread(img)).reshape(1, -1))
    print(pred)
    finish = input("Are you finished? (y/n): ")
    if finish == "y":
        Done = True
    elif finish == "n":
        Done == False
    else:
        finish = input("Are you finished? (y/n): ")

