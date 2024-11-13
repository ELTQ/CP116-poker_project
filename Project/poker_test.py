import joblib
from poker_visual import preprocess
import cv2 as cv
from poker_solver import Card
p_model = joblib.load('model.pkl')


def predCard(img):
    currentCard = p_model.predict(preprocess(cv.imread(img)).reshape(1, -1))
    currentCard = currentCard[0]
    return Card(currentCard.split("_")[1],currentCard.split("_")[0])
