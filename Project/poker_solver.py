import random
from itertools import combinations

import numpy

playerNum = 2
suits = ["S", "C", "H", "D"]
# all possible suits
ranks = {'Two':1, 'Three':2, 'Four':3, 'Five':4, 'Six':5, 'Seven':6, 'Eight':7, 'Nine':8, 'Ten':9, 'Jack':10, 'Queen':11, 'King':12, 'Ace':13}
# all ranks with correlated rankings
# which two is the smallest and Ace is the biggest
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# standard form of card in this file


def haveOverlap(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False
# find were there overlap between two lists

def combine(card1,card2):
    ans = []
    for c in card1+card2:
        ans.append(c)
    return ans
# combine two lists resulting in a new list
# no original ones will be influenced

def sortCards(lOCards):
    return sorted(lOCards, key=lambda x: ranks[x.rank])
# sort the list of card based on rank

def getSameRanks(lOCards):
    ans = []
    current = []
    for c in sortCards(lOCards):
        if len(current) == 0:
            current.append(c)
            continue
        if current[0].rank == c.rank:
            current.append(c)
            continue
        ans.append(current)
        current = [c]
    if current not in ans:
        ans.append(current)

    maxLen = 0
    maxRank = 0
    maxComb = []
    for comb in ans:
        try:
            if len(comb) > maxLen or (len(comb) == maxLen and ranks[comb[0].rank] >= maxRank):
                maxLen = len(comb)
                maxRank = ranks[comb[0].rank]
                maxComb = comb
        except:
            print("problem with cards")
    return maxComb
# get cards that have the same rank within the list

def getStraight(lOCards, keepAll = False):
    sortedCards = sortCards(lOCards)
    straight = []
    lastRank = 0
    if sortedCards[-1].rank == "A":
        straight.append(sortedCards[-1])
        lastRank = 1

    for c in sortedCards:
        if len(straight) == 0:
            lastRank = ranks[c.rank]
            straight.append(c)
            continue
        if ranks[c.rank] == lastRank:
            continue
        if ranks[c.rank] - lastRank == 1:
            lastRank = ranks[c.rank]
            straight.append(c)
            continue
        if len(straight) >= 5:
            if keepAll:
                return straight
            return straight[-5:]
        straight = [c]
        lastRank = ranks[c.rank]
    if len(straight) >= 5:
        if keepAll:
            return straight
        return straight[-5:]
    return None
# get combo that is straight if possible


def getFlush(lOCards, keepAll = False):
    sortedCards = sortCards(lOCards)
    sameSuit = {}
    for c in sortedCards:
        if c.suit not in sameSuit:
            sameSuit[c.suit] = [c]
            continue
        sameSuit[c.suit].append(c)
    for s in sameSuit:
        if len(sameSuit[s]) >=5:
            if keepAll:
                return sameSuit[s]
            return sameSuit[s][-5:]
    return None
# get combo that is flush if possible

def copyCards(lOCards):
    return [c for c in lOCards]
# return the copy of a list of cards

def sameCard(c1,c2):
    return c1.rank == c2.rank and c1.suit == c2.suit
# tell whether or not are two cards the same interms of values
# inside it

def findSame(lOC1, lOC2):
    same = []
    if lOC1 == None or lOC2 == None:
        return None
    for c1 in lOC1:
        for c2 in lOC2:
            try:
                if sameCard(c1,c2):
                    same.append(c1)
            except:
                print(c1,c2)
    return same
# find same cards within the two lists

def getStraightFlush(lOCards):
    same = findSame(getFlush(lOCards), getStraight(lOCards))
    if same == None:
        return None
    if len(same) >= 5:
        return same[-5:]
    return None
# get straight flush combo if possible

def getFourOfAKind(lOCards):
    sameRank = getSameRanks(lOCards)
    if len(sameRank) == 4:
        return [sameRank]
    return None
# get four of a kind if possible

def getThreeOfAKind(lOCards):
    sameRank = getSameRanks(lOCards)
    if len(sameRank) == 3:
        return [sameRank]
    return None
# get three of a kind if possible

def exclude(lOC,what):
    notSame = copyCards(lOC)
    for w in what:
        for ns in notSame:
            if sameCard(w,ns):
                notSame.remove(ns)
    return notSame
# exclude the what from the list of cards input without adjusting original


def getFullHouse(lOCards):
    copiedCards = copyCards(lOCards)
    sameRanks = []

    while True:
        if len(copiedCards) == 0:
            break
        nextGetRank = getSameRanks(copiedCards)
        copiedCards = exclude(copiedCards, nextGetRank)
        if nextGetRank == None or len(nextGetRank) == 0:
            break
        if len(nextGetRank) < 2:
            continue
        sameRanks.append(nextGetRank)


    possibleThree = []
    possiblePair = []
    for s in sameRanks:
        if len(s) >= 3:
            possibleThree.append(s)
        elif len(s) >= 2:
            possiblePair.append(s)

    if len(possibleThree) == 0:
        return None
    maxThree = max(possibleThree, key = lambda x: ranks[x[0].rank])
    possibleThree.remove(maxThree)
    possiblePair += possibleThree
    if len(possiblePair) == 0:
        return None
    possiblePair = sorted(possiblePair, key = lambda x: ranks[x[0].rank])
    maxTwo = max(possiblePair, key = lambda x: ranks[x[0].rank])
    return [maxThree[-3:], maxTwo[-2:]]
# get full house if possible

def getPair(lOCards):
    sameRank = getSameRanks(lOCards)
    if len(sameRank) < 2:
        return None
    return [sorted(sameRank, key = lambda x: ranks[x.rank])[-2:]]
# get pair if possible

def getTwoPairs(lOCards):
    sameRank = getSameRanks(lOCards)
    if len(sameRank) < 2:
        return None
    clearedLOC = exclude(lOCards,sameRank)
    another = getSameRanks(clearedLOC)
    if len(another) < 2:
        return None
    return [sameRank[-2:], another[-2:]]
# get two pairs if possible

def getRoyalFlush(lOCards):
    straightFlush = getStraightFlush(lOCards)
    if straightFlush == None:
        return None
    if straightFlush[0].rank == "J":
        return straightFlush
    return None
# get royal flush if possible


   # ranks:
    # royal flush
    # straight flush
    # four of a kind
    # full house
    # flush
    # straight
    # three of a kind
    # two pairs
    # one pair
    # high card
def formCard(lOCards, pool):
    combined = combine(lOCards,pool)
    checkThese = [getRoyalFlush,getStraightFlush,getFourOfAKind,getFullHouse,getFlush,getStraight,getThreeOfAKind,getTwoPairs,getPair]
    for func,i in zip(checkThese,range(len(checkThese))):
        cards = func(combined)
        if cards == None:
            continue
        return cards, i
    return [sorted(combined,key = lambda x: ranks[x.rank])[len(combined)-1]], 1000
 # form combos if possible

def compair(pl1Card, pl2Card, pool):
    usr1 = formCard(pl1Card, pool)
    usr2 = formCard(pl2Card, pool)
    if usr1[1] < usr2[1]:
        return True
    if usr1[1] > usr2[1]:
        return False
    us1Cards = usr1[0]
    us2Cards = usr2[0]
    for i,j in zip(us1Cards,us2Cards):
        try:
            if ranks[i.rank] > ranks[j.rank]:
                return True
            if ranks[i.rank] < ranks[j.rank]:
                return False
        except:
            for ii,jj in zip(i,j):
                if ranks[ii.rank] > ranks[jj.rank]:
                    return True
                if ranks[ii.rank] < ranks[jj.rank]:
                    return False
    return True
# see if pl1 win with pl2card and pool


# loop through everything
# def winLoose(pl1Card,pool):
#     win = 0
#     rounds = 0
#     for i in list(combinations(allCards,2)):
#         if haveOverlap(i,pl1Card) or haveOverlap(i,pool):
#             continue
#         if compair(pl1Card,i, pool):
#             win+=1
#         rounds += 1
#     return win/rounds
# loop through everything but cost too much time to run

# random choice
def winLoose(pl1Card,pool, copied):
    win = 0
    rounds = 0
    for i in range(10000):
        possibleCards = copyCards(copied)
        currentPool = list(numpy.random.choice(possibleCards, size=5 - len(pool), replace=False)) + pool
        possibleCards = exclude(possibleCards,currentPool)
        pls = []
        for pl in range(playerNum-1):
            pls.append(list(numpy.random.choice(possibleCards, size=2,replace=False)))
            possibleCards = exclude(possibleCards,pls[-1])
        winPl = True
        for p in pls:
            if not compair(pl1Card,p, currentPool):
                winPl = False
        if winPl:
            win += 1
        rounds += 1
        print(rounds)
    return win/rounds
# returns the winrate

def cardToString(cards):
    ans = ""
    for combination in cards:
        for c in combination:
            ans += c.rank + c.suit + ","
    return ans
# change cards to string for possible usage

allCards = []
for s in suits:
    for r in ranks:
        allCards.append(Card(s, r))
# append all cards into all cards


# iniHand = list(combinations(allCards, 2))
# pool = list(combinations(allCards, 5))
# for h in iniHand:
#     for p in pool:
#         if haveOverlap(h, p):
#             continue
#         pocketWin[cardToString((h,p))] = winLoose(h,p)
# probability = ""
# for pw in pocketWin:
#     probability += pw, pocketWin[pw]
# f = file = open("data.txt","w")
# f.write(probability)
# f.close()





def makeDecision(hand, poolCard, poolMoney, bet, allin):
    copied = copyCards(allCards)
    # iniHand = [Card("D", "A"), Card("S", "A")]
    iniHand = hand
    # iniPool = [Card("D","8"),Card("S","T"),Card("S","4")]
    iniPool = poolCard
    copied = exclude(copied, iniHand)
    possibleCards = copyCards(copied)
    winRate = winLoose(iniHand, iniPool,possibleCards)
    if allin:
        if winRate > .8:
            return "check", winRate
        return "fold", winRate
    if bet < poolMoney*winRate:
        if poolMoney * winRate > 2 * bet:
            return "raise", winRate
        return "check", winRate
    return "fold", winRate
# function taht help make decision
