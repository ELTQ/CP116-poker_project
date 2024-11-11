import joblib
from poker_visual import preprocess

p_model = joblib.load('model.pkl')


name = "Ace_of_Diamond"
rankSuit = name.split("_of_")

dict_hand = {}
dict_river = {}
for card in hand:
    card = preprocess(card)
    pred = p_model.predict(card)
    rank = pred.split("_")[0]
    suit = pred.split("_")[1]
    dict_hand[rank] = suit
for card in community_cards:
    card = preprocess(card)
    pred = p_model.predict(card)
    rank = pred.split("_")[0]
    suit = pred.split("_")[1]
    dict_river[rank] = suit
