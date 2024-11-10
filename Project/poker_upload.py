

from PIL import Image
import keyboard


class Game:
    def __init__(self):
        self.hand = []
        self.community_cards = []

    def import_image(self):
        file_path = input("Enter the path of your image: ").replace(" ","")
        try:
            image = Image.open(file_path)
            return image
        except FileNotFoundError:
            print("File not found. Please check the path.")
            return None

    def load_hand(self):
        print("Please upload your current hand")
        for i in range(2):
            image = self.import_image()
            self.hand.append(image)

        print("Your hand has been saved.")

    def load_flop(self):
        print("Now that the flop has been dealt, please upload the flop.")
        for i in range(3):
            card = self.import_image()
            self.community_cards.append(card)

    def community_deal(self):
        if len(self.community_cards) == 5:
            print("You've reached the maximum amount of cards you can add to the river.")
        else:
            card = self.import_image()
            self.community_cards.append(card)


    def game_loop(self):
        print("Welcome to a new game of Poker!")
        self.load_hand()
        # get cards() from eliot
        # run decision from alex
        # if the decision folds, then return or use other way
        # to stop the function
        # or ask what the user decides
        # then decide to quit the function(the program)
        # or not
        print(self.hand)
        self.load_flop()


        print(self.community_cards)
        print("Press 'r' to add community cards or press 'q' to quit program")
        print("Press 'p' to update the pot")

        while True:
            # if keyboard.is_pressed("r"): input("what is your decision")
                self.community_deal()
                print(community_cards)
            if keyboard.is_pressed("q"):
                break

if __name__ == "__main__":
    game = Game()
    game.game_loop()
