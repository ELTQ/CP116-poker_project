import cv2 as cv
from skimage.filters import sobel
import numpy as np
from sklearn.neural_network import MLPClassifier


f = open("cards.txt")
cards = f.readlines()
cards = [c.replace('\n', '') for c in cards]




X = []
Y = []

def preprocess(X):
    resized = cv.resize(X, (28, 28))
    sobel_filtered = sobel(resized)
    flattened = sobel_filtered.flatten()
    return flattened

for card in cards:
    card = card.replace('Training_images/', 'Training_images2/')
    img = cv.imread(card)
    features = preprocess(img)
    name = card.replace('Training_images2/', '').replace('.png', '')
    X.append(features)
    Y.append(name)


X = np.array(X)
Y = np.array(Y)

model = MLPClassifier(hidden_layer_sizes=(128, 64, 32, 16, 8), activation='relu', max_iter=50000)
model.fit(X, Y)

import joblib
joblib.dump(model, 'model.pkl')
