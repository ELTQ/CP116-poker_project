from PIL import Image
import keyboard
import poker_solver
from poker_test import predCard
from poker_solver import makeDecision

class Game:
    def __init__(self):
        self.hand = [] #list for user hand
        self.community_cards = [] #list for river
        self.pot = 0 #variable for pot amount
        self.betMoney = 0 #variable for bet amount


    def import_image(self):
        # Allow user to import their card images
        file_path = input("Enter the path of your image: ").replace(" ","") #Avoiding user error due to spaces after image path
        try:
            Image.open(file_path)
            return file_path
        except:
            # If bad file path ask again for file.
            print("File not found. Please check the path.")
            return None

    def load_hand(self):
        # load_hand function allows user to upload two cards to hand
        print("Please upload your current hand")
        while True:
            image = self.import_image()
            if image != None:
                self.hand.append(image) #saves images to hand list
            if len(self.hand) ==2: #after adding their two hand cards while loop breaks
                break
        temp = [predCard(c) for c in self.hand]
        self.hand = temp
        print("Your hand has been saved.")

    def load_flop(self):
        # load_flop adds first three cards from the river to the community cards list before continuing.
        print("Now that the flop has been dealt, please upload the flop.")
        for i in range(3):
            self.community_deal()

    def community_deal(self):
        # communty deal makes sure no more than 5 cards are added to the river
        if len(self.community_cards) == 5:
            print("You've reached the maximum amount of cards you can add to the river.")
        else:
            currentCard = ""
            not_valid = True
            while not_valid:
                card = self.import_image()
                if card != None:
                    currentCard = card
                    not_valid = False
            temp = [predCard(currentCard)]
            self.community_cards += temp



    def game_loop(self):
        # game loop runs the program
        print("Welcome to a new game of Poker!")
        counter = 0
        while True:
            haveErr = False
            while not haveErr:
                try:
                    # Adding the # of players to alex's playerNum variable
                    poker_solver.playerNum = int(input("How many player are there?: "))
                    haveErr = True
                except:
                    print("Invalid amount, please try again.")
            print("Press 'r' to add cards" * (counter < 4))
            print("Press 'p' to update the pot")
            print("Press 'q' to quit ")

            # if keyboard.is_pressed("r"): #input("what is your decision")
            check = input("")
            if check == "q":
                # giving the user a way to leave quit program
                break
                # 'p' allows user to uodate the pot amount
            if check=="p" or check=="r":
                haveErr = True
                while haveErr:
                    try:
                        pot = input("Enter the amount of current pot: ")
                        self.pot = float(pot)
                        haveErr = False
                    except:
                        print("err")
                print("Okay! Current pot amount set to ", self.pot)
            if check == "r" and counter < 4:
                if counter == 0:
                    self.load_hand()
                elif counter == 1:
                    self.load_flop()
                else:
                    self.community_deal()
                counter += 1

            haveErr = False
            while not haveErr:
                try:
                    # allow user to input their bet amount (for alex)
                    self.betMoney += int(input("How much money do you need to check?: "))
                    haveErr = True
                except:
                    print("Invalid amount, please try again.")
            haveErr = False
            while not haveErr:
                try:
                    # test to see if any players went all in (for alex)
                    self.allIn = int(input("Is anyone all in?(Type 1 for yes, 2 for no): ")) == 1
                    haveErr= True
                except:
                    print("Invalid amount, please try again.")
            if counter != 0 and check in "r,p":
                resl = makeDecision(self.hand,self.community_cards, self.pot, self.betMoney, self.allIn)
                print(f"We recommend you {resl[0]} the current winrate of your hand is {resl[1]}")


if __name__ == "__main__":
    game = Game()
    game.game_loop()
