import math


# choose k value from n
# while order do not matter
def C(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def odds(probability: float) -> int:
    return int(round(1/probability - 1,0))
# ... : 1

def getRank(rank:str) -> int:
    inputRanks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    relativeRank = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in range(len(inputRanks)):
        if inputRanks[i] == rank:
            return relativeRank[i]
    return -1

class Card:
    # rank: from 2 to A
    # suit: D(diamond), S(spade), H(heart), C(club)
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit


class Node:
    def __init__(self,val: float):
        self.value = val
        self.r = -1
        self.l = -1

def biggerThan(card1: Card, card2: Card):
    if getRank(card1.rank) > getRank(card2.rank):
        return True
    return False


def probabilityOfHavingABiggerPair(rank: str):
    return ((14 - getRank(rank)) * 4) / 50 * 3/49


def build(p: float, depth: int, root: Node, currentDepth: int) -> None:
    if currentDepth == depth:
        return
    root.l = Node(p * root.value)
    root.r = Node((1-p) * root.value)
    build(p,depth,root.l,currentDepth+1)
    build(p,depth,root.r,currentDepth+1)


def findAllPSum(root: Node) -> float:
    if root.r == -1:
        return root.value
    return findAllPSum(root.l) + findAllPSum(root.r) if root.r.l != -1 else 0

# this function will build a tree then find all possible wins
def findWin(p: float,depth: int):
    root = Node(1)
    build(p,depth,root,1)
    return findAllPSum(root)


def probabilityOfOtherPlayerHanveBetterPair(rank: str, amountPlayer: int):
    return probabilityOfHavingABiggerPair(rank) * (amountPlayer-1) - findWin(probabilityOfHavingABiggerPair(rank),amountPlayer)


# probabilitySingleOpponentHaivngBetterAcePairWhenWeHaveA
def PofAxBetterOurAx(rank: str):
    return (3/50*2/49)+(3/50*(13-getRank(rank))*4/49*2)

n_pocket_combination = C(52,2)

n_suit_combination_for_pocket_pair = C(4,2)
# any rank, there may be 4 possible suits
# for each different suit there may form a pair

P_of_specific_pocket_pair = n_suit_combination_for_pocket_pair/n_pocket_combination
P_of_pocket_pairs = n_suit_combination_for_pocket_pair * 13/n_pocket_combination
# 13 means 13 ranks

n_combination_for_suited_hands = C(13,2)
n_suit_combination_for_suited_hands = C(4,1)
P_of_specific_pocket_pair = n_suit_combination_for_suited_hands/n_pocket_combination
P_of_pocket_pair = n_combination_for_suited_hands * n_suit_combination_for_suited_hands/n_pocket_combination

n_combination_for_offsuited_hands = 78
n_suit_combination_for_offsuited_hands = C(4,1) * C(3,1)
P_of_specific_offsuit = n_suit_combination_for_offsuited_hands/n_pocket_combination
P_of_offsuit = n_suit_combination_for_offsuited_hands * n_combination_for_offsuited_hands/n_pocket_combination

P_of_oppo_double_ace_when_having_one_ace = 3/50 * 2/49


# probability of specific hand
all_possible_combination = math.factorial(52)/math.factorial(52-5)/math.factorial(5)

P_royal_flush = C(4,1)/all_possible_combination
P_straight_flush = C(10,1)*C(4,1)-C(4,1)/all_possible_combination
P_four_of_a_kind = C(13,1)*C(4,4)*C(48,1)/all_possible_combination
P_full_house = C(13,1)*C(4,3)*C(12,1)*C(4,2)/all_possible_combination
P_flush = C(13,5)*C(4,1)-C(10,1)*C(4,1)/all_possible_combination
P_straight = C(10,1)*math.pow(C(4,1),5)-C(10,1)*C(4,1)/all_possible_combination
P_three_of_a_kind = C(13,1)*C(4,3)*C(12,2)*math.pow(C(4,1),2)/all_possible_combination
P_two_pair = C(13,2)*math.pow(C(4,2),2)*C(11,1)*C(4,1)/all_possible_combination
P_pair = C(13,1)*C(4,2)*C(12,3)*math.pow(C(4,1),3)/all_possible_combination
P_high_card = (C(13,5)-10)*(math.pow(C(4,1),5)-4)

print(probabilityOfOtherPlayerHanveBetterPair("K",3))

if __name__ == "__main__":
    usrHand = []
    for i in range(2):
        usrHand.append(Card(input("what is your rank? [2,3,4,5,6,7,8,9,T,J,Q,K,A]"),input("what is your suit [D,S,H,C]")))
    playerAmount = int(input("how many players do we have"))
    pocketPair = False
    if usrHand[0].rank == usrHand[1].rank:
        pocketPair = True
    suitedHand = False
    if usrHand[0].suit == usrHand[1].suit:
        suitedHand = True

    if pocketPair:
        rank = usrHand[0].rank
        P_other_better_hand = probabilityOfOtherPlayerHanveBetterPair(rank,playerAmount)
        P_no_over_card_on_flop = C(4*getRank(rank)-6,3)/C(50,3)
        P_no_over_card_on_turn = C(4*getRank(rank)-6,4)/C(50,4)
        P_no_over_card_on_river = C(4*getRank(rank)-6,5)/C(50,5)
