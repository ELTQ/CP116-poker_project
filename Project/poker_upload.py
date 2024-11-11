
from PIL import Image
import keyboard
import poker_solver
import poker_test


class Game:
    def __init__(self):
        self.hand = []
        self.community_cards = []
        self.pot = 0
        self.betMoney = 0


    def import_image(self):
        file_path = input("Enter the path of your image: ").replace(" ","")
        try:
            image = Image.open(file_path)
            return image
        except:
            print("File not found. Please check the path.")
            return None

    def load_hand(self):
        print("Please upload your current hand")
        while True:
            image = self.import_image()
            if image != None:
                self.hand.append(image)
            if len(self.hand) ==2:
                break
        temp = [predCard(c) for c in self.hand]
        self.hand = temp
        print("Your hand has been saved.")

    def load_flop(self):
        print("Now that the flop has been dealt, please upload the flop.")
        for i in range(3):
            self.community_deal()

    def community_deal(self):
        if len(self.community_cards) == 5:
            print("You've reached the maximum amount of cards you can add to the river.")
        else:
            not_valid = True
            while not_valid:
                card = self.import_image()
                if card != None:
                    self.community_cards.append(card)
                    not_valid = False
            temp = [predCard(c) for c in self.community_cards]
            self.community_cards = temp



    def game_loop(self):
        print("Welcome to a new game of Poker!")

        haveErr = False
        while not haveErr:
            try:
                poker_solver.playerNum = int(input("How many player are there?: "))
                haveErr = True
            except:
                print("Invalid amount, please try again.")
    #     self.load_hand()
    #     # get cards() from eliot
    #     # run decision from alex
    #     # if the decision folds, then return or use other way
    #     # to stop the function
    #     # or ask what the user decides
    #     # then decide to quit the function(the program)
    #     # or not
    #     print(self.hand)
    #     # self.load_flop()
        counter = 0
        while True:
            print("Press 'r' to add cards" * (counter < 4))
            print("Press 'p' to update the pot")
            print("Press 'q' to quit ")
            # if keyboard.is_pressed("r"): #input("what is your decision")
            check = input("")
            if check == "r" and counter < 4:
                if counter == 0:
                    self.load_hand()
                elif counter == 1:
                    self.load_flop()
                else:
                    self.community_deal()
                counter += 1
            elif check=="p":
                pot = input("Enter the amount of current pot: ")
                self.pot = float(pot)
                print("Okay! Current pot amount set to ", self.pot)
            elif check == "q":
                break
            haveErr = False
            while not haveErr:
                try:
                    self.betMoney += int(input("How much money do you need to check?: "))
                    haveErr = True
                except:
                    print("Invalid amount, please try again.")
            haveErr = False
            while not haveErr:
                try:
                    self.allIn = int(input("Is anyone all in?(Type 1 for yes, 2 for no): ")) == 1
                    haveErr= True
                except:
                    print("Invalid amount, please try again.")
            print(makeDecision([self.hand,self.community_cards, self.pot, self.betMoney, self.allIn))


if __name__ == "__main__":
    game = Game()
    game.game_loop()
