import cv2 as cv
import numpy as np
from sklearn.neural_network import MLPClassifier
from skimage.feature import hog

# open training images path from file
f = open("cards.txt",'r')
cards = f.read().split('\n')


X = []
Y = []

# preprocess the images before training the model
# resize, grayscale, Histogram of Oriented Gradients
def preprocess(X):
    resized = cv.resize(X, (52, 52))
    gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
    hog_image = hog(gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), feature_vector=True)
    return hog_image


# store the images features into a list and store their corresponded name in another list
for card in cards:
    img = cv.imread(card)
    features = preprocess(img)
    name = card.replace('Training_images/', '').replace('.png', '')
    X.append(features)
    Y.append(name)

# convert to numpy array
X = np.array(X)
Y = np.array(Y)

# train the model using MLPclassifier
model = MLPClassifier(hidden_layer_sizes=(1024, 512, 256), activation='relu', solver='adam', max_iter=10000)
model.fit(X, Y)

# storing the trained model
import joblib
joblib.dump(model, 'model.pkl')
