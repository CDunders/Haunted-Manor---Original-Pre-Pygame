import random as rand
from time import sleep

ROUNDS = 5

class Users:
    """A Class for user set up"""
    def __init__(self, user_1, user_2):
        """Initialize the game"""
        self.user_1 = user_1
        self.user_2 = user_2

        # Users scores
        self.user_1_scores = []
        self.user_2_scores = []


    def greeting(self):
        """Greeting intro to game"""
        print(f"\nWe will be playing 'Roll A Double'\n")
        print("You will take it in turns to roll two dice. If you get a double, you win the game. Simple!\n")
        print(f"{ROUNDS} rounds will be played.")
        return self.play_round()
    

    def play_round(self):
        for i in range(3):
            play_1 = input(f"\nIt's {self.user_1}'s turn. Press enter to roll the dice:\n> ")
            while play_1 != "":
                play_1 = input(f"\nIt's {self.user_1}'s turn. Press enter to roll the dice:\n> ")
            self.dice_roll_player_1()
            
            sleep(2)
            print(f"\nIt's {self.user_2}'s turn.")
            self.dice_roll_player_2()

            sleep(2)
            self.display_results()

        if sum(self.user_1_scores) > sum(self.user_2_scores):
            print(f"\n{self.user_1} is the winner!")
            self.user_1_scores.clear()
            self.user_2_scores.clear()
            sleep(2)
            return True
        elif sum(self.user_1_scores) < sum(self.user_2_scores):
            print(f"\n{self.user_2} is the winner!")
            self.user_1_scores.clear()
            self.user_2_scores.clear()
            sleep(2)
            return False
        else:
            print("\nIt's ended in a draw'!")
            self.user_1_scores.clear()
            self.user_2_scores.clear()
            sleep(2)
            return False

    def display_results(self):
        last_score_1 = self.user_1_scores[-1]
        last_score_2 = self.user_2_scores[-1]
        if last_score_1 == 1 and last_score_2 == 1:
            print("\nIt's a draw!\n")
        elif last_score_1 != 1 and last_score_2 != 1:
            print("\nIt's a draw!\n")
        elif last_score_1 == 1 and last_score_2 != 1:
            print(f"\n{self.user_1} wins this round!\n")
        else:
            print(f"\n{self.user_2} wins this round!\n")
        sleep(2)
        print(f"{self.user_1} has a current score of {sum(self.user_1_scores)}")
        print(f"{self.user_2} has a current score of {sum(self.user_2_scores)}")
        if sum(self.user_1_scores) > sum(self.user_2_scores):
            print(f"{self.user_1} is the current game leader!")
        elif sum(self.user_1_scores) < sum(self.user_2_scores):
            print(f"{self.user_2} is the current game leader!")
        else:
            print(f"You are currently drawing!")
        sleep(2)


    def dice_roll_player_1(self):
        dice_1 = rand.randint(1,6)
        dice_2 = rand.randint(1,6)
        print(f"{self.user_1} rolled a {dice_1} and {dice_2}")
        if dice_1 == dice_2:
            print("You got a double!")
            point = 1
            self.user_1_scores.append(point)
        else:
            print("Not this time.")
            point = 0
            self.user_1_scores.append(point)

    def dice_roll_player_2(self):
        dice_1 = rand.randint(1,6)
        dice_2 = rand.randint(1,6)
        print(f"{self.user_2} rolls a {dice_1} and {dice_2}")
        if dice_1 == dice_2:
            #print("You got a double!")
            point = 1
            self.user_2_scores.append(point)
        else:
            #print("Not this time.")
            point = 0
            self.user_2_scores.append(point)
