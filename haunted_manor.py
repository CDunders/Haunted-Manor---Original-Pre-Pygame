import random
from time import sleep
import rock_paper_scissors as rps
import memory_game as mg
import roll_a_double as rad

MIN_HEALTH = 0
MAX_HEALTH = 10

class Player:
    """Class representing the player with stats, inventory, and gameplay functions"""
    def __init__(self, hp=MAX_HEALTH):
        self.name = ''
        self.hp = hp
        self.inventory = []
        self.health_potion_collected = False # Indicates if a health potiion has been collected
    
    @staticmethod # Instance data not required for this method
    def choice_validation():
        """Prompts the player to enter a choice and validates the input"""
        choice = input("\nEnter the number of choice:\n > ")
        while choice != "1" and choice != "2":
            print("Please enter the number of your choice.")
            choice = input("\nEnter the number of choice:\n > ")
        return choice
    
    def roll_a_double_func(self):
        """Initiates the 'roll_a_double' game using the player name"""
        users = rad.Users(self.name, "Old Ghost Lady")
        return users.greeting()

    def player_name(self):
        """Prompts the player for their name and checks it's not blank"""
        self.name = input("Player, what is your name? ").title()
        # Validate name, can't be blank
        while self.name == "":
            print("Can't be blank.")
            self.name = input("Player, what is your name? ").title()            
        return self.name
    
    def health_attack(self):
        """Called when player is attacked, reduces health by a random value and returns updated hp"""
        self.hp = self.hp-random.randint(1,8)
        # HP cannot go below 0
        if self.hp < MIN_HEALTH:
            self.hp = MIN_HEALTH
        return self.hp
    
    def health_gain(self):
        """Called when player drinks health potion, restores health back to full (MAX_HEALTH)"""
        self.hp = MAX_HEALTH
        return self.hp

    def stats(self):
        """Displays current stats, allows use of health potion if available and checks game over condition"""
        if self.hp <= MIN_HEALTH:
            # Ends game if health at 0
            print(f"\nCURRENT HEALTH: {self.hp}\nCURRENT INVENTORY: {self.inventory}\n")
            print("You die!")
            self.replay()
        else:
            # If health potion in inventory
            if 'Health Potion' in self.inventory:
                # Provide stats and option to use health potion
                print(f"\nCURRENT HEALTH: {self.hp}\nCURRENT INVENTORY: {self.inventory}\n")
                print("Would you like to use your health potion?\n1.Yes\n2.No")
                # Check choice validation
                choice = self.choice_validation()
                if choice == "1":
                    # If use health potion, update health and remove from inventory. Print updated stats
                    self.health_gain()
                    self.inventory.remove ('Health Potion')
                    print("\nYou drank the health potion. Health is now back to full!")
                    print(f"\nCURRENT HEALTH: {self.hp}\nCURRENT INVENTORY: {self.inventory}\n")
                else:
                    # Don't use health potion
                    print(f"No problem, maybe you'll need it later 😉\n") # Add a winky face
            else:
                # If health potion not in inventory, just print stats
                print(f"\nCURRENT HEALTH: {self.hp}\nCURRENT INVENTORY: {self.inventory}\n") 
    


    def intro(self):
        """Gives introduction and starts the game based on player's choice"""
        print(f"\nWelcome {self.name}. You find yourself standing at the gate of a large and very old Manor, some people say it's haunted...")
        sleep(2)
        print(f"\nAre you brave enough to enter the haunted manor?\n1.Yes\n2.No")
        # Check choice validation
        choice = self.choice_validation()
        if choice == "1":
            # Go to garden (room)
            self.garden()
        else:
            # End game
            print("\nGoodbye")
            quit()
    
    def garden(self):
        """Garden gameplay based on players choices (including possible attack by dog and finding a sword)"""
        print("\nYou walk through the gate into the Manor grounds and towards the front door. Something glistening catches your eye but then you hear something....Growling!\n")
        sleep(2)
        print(f"A huge snarling dog with bared teeth is running towards you! {self.name}, do you run to the safety of the house or back to the gate?\n1.House\n2.Gate")
        # Check choice validation        
        choice = self.choice_validation()       
        if choice == "1":
            # Go to hallway (room)
            self.hallway()
        else:
            print("\nYou were attacked by the dog!")
            # Call health attack
            self.health_attack()
            print(f"Your remaining health is {self.hp}.")
            sleep(2)
            print("\nYou notice something glistening under a near by tree, a sword! You might need this! It's added to your inventory.")
            # Add sword to inventory
            self.inventory.append ('Sword')
            sleep(2)
            # Call stats
            self.stats()
            sleep(2)
            print("You wait for a minute, no sign of the dog anymore. You make your way to the manor door.")     
            sleep(3)
            print("\nYou made it! And now find yourself standing in a very large hallway.")  
            sleep(2) 
            # Go to hallway
            self.hallway()         

    def hallway(self):
        """Hallway gameplay based on players choices"""
        print("\nTo the left of you is a door leading to the Living Room and to the right is the Dining Room, which will you choose?\n1.Living Room\n2.Dining Room")
        # Check choice validation       
        choice = self.choice_validation()
        if choice == "1":
            # Go to livingroom (room)
            self.living_room()
        else:
            # Go to diningroom (room)
            self.dining_room()

    def dining_room(self):
        """Dining room gameplay based on players choices (including interactions with ghost and finding a key)"""
        # Call stats
        self.stats()
        # If key in inventory
        if 'key' not in self.inventory:
            print("You see a ghostly figure in the corner of the room, do you approach it?\n1.Yes\n2.No")
            # Check choice validation            
            choice = self.choice_validation()
            if choice == "1":
                # Go to ghost (gameplay)
                self.ghost()
            else:
                # Call room choice (hallway or next room)
                self.room_choice()
        else:
            # If key not in inventory
            print("You have completed everything in this room.")
            # Call room choice (hallway or next room)
            self.room_choice()

    def living_room(self):
        """Living room gameplay based on players choices (including interaction with chest and finding health potion)"""
        # Call stats
        self.stats()
        # If health potion not collected already
        if self.health_potion_collected == False:
            print("There is a box in the far corner, do you go and open it?\n1.Yes\n2.No")
            # Check choice validation           
            choice = self.choice_validation()
            if choice == "1":
                print("\nIt's locked!\n") 
                sleep(1)
                print("You can see there is a keypad on the top with the numbers 0-5 and a Play button. Next to the keypad is a display of 6 * symbols.")
                sleep(2)
                print('Underneath the display of symbols it reads "Can you match the hidden numbers?"')
                sleep(2)
                print("You press Play...and a voice begins to speak...")
                # Call memory game (gameplay), need to win to open box and get health potion
                game = mg.main()
                # If you win (returns true)
                if game:
                    print(f"\nYou find a health potion, it's added to your inventory.")
                    # Add health potion to inventory
                    self.inventory.append ('Health Potion')
                    # Update health_potion_collected to true
                    self.health_potion_collected = True
            # Call room choice (hallway or next room)
            self.room_choice()
        else:
            # If health posion collected is true (already collected)
            print("You have completed everything in this room.\n")
            # Call room choice (hallway or next room)
            self.room_choice()

    def kitchen(self):
        """Kitchen gameplay based on players choices (including possible ghost attack)"""
        print("\nYou get a glimpse of a shadow as you walk into the kitchen.")
        sleep(1)
        print("\nA headless ghost lurks on the other side of the room....And is now running towards you!")
        # If sword in inventory, you attack the ghost
        if 'Sword' in self.inventory:
            sleep(2)
            print("\nYou draw your sword and prepare to fight!")
            sleep(1)
            print("\nYou stab the ghost and it vanishes....you were lucky, this time!")
            # Go to cellar (room)
            self.cellar()
        else:
            # If sword not in inventory, the ghost attacks you
            print("\nYou don't appear to have any weapon to defend yourself, maybe you missed something along the way!")
            print("\nThe ghost attacks you and then vanishes....")
            # Call health attack
            self.health_attack()
            # Go to cellar (room)
            self.cellar()


    def cellar(self):
        """Cellar gameplay based on players choices, you need the key to enter. (Including possible ghost attack and finding the treasure)"""
        # Call stats
        self.stats()
        sleep(2)
        # Option to investigate cellar
        print("There is a noise coming from what appears to be a celler, do you investigate further?\n1.Yes\n2.No")
        # Check choice validation         
        choice = self.choice_validation()
        if choice == "1":
            print("\nIt's locked!")
            # If key in inventory, use to unlock cellar door
            if 'key' in self.inventory:
                print("\nYou try the key you got from the Old Lady Ghost, it works, you open the creeking door slowly as the noise inside gets louder!")
                # Remove key from inventory
                self.inventory.remove ('key')
                # Go to final fight (gameplay)
                self.final_fight()
            # If key not in inventory, you can't open cellar door. Game ends
            else:
                print("\nYou do not have the key, perhaps you missed something along the way?")
                print("\nYou see the back door and leave the house, you escaped! Though you may have missed some treasure along the way...\n")
                # Call replay, option to start game over
                self.replay()
        # Choose not to investigate cellar
        else:
            print("\nYou see the back door and leave the house, you escaped! Though you may have missed some treasure along the way...")
            # Call replay, option to start game over            
            self.replay()
    

    def final_fight(self):
        """Final fight gameplay held in the cellar, determines game outcome"""
        print("\nIt's dark down here!")
        sleep(3)
        print("\nYou still can't tell what is making the noise but it's a deep groaning and it does not sound happy!")
        sleep(3)
        print("\nSomething else catches your eye, distracting you from the niose. TREASURE!! And lots of it! Maybe this was worth it after all...")
        sleep(2)
        print("\nYou approuch the treasure but then freeze in your tracks as you feel a breath on the back of your neck! You slowly turn around.....")
        sleep(4)
        print("\nIt's the headless ghost again! He is really angry now! I hope you have enough energy and a sword to get through this one!")
        # If sword in inventory, you can attack the ghost
        if 'Sword' in self.inventory:
            sleep(2)
            print("\nYou draw your sword and prepare to fight once more!")
            sleep(2)
            print("\nYou stab the ghost but he doesn't vanish this time! He attacks back! He got you!")
            # Call health attack
            self.health_attack()
            sleep(2)
            print("You stike again and this time he vanishes once more!")
            # You win and treasure added to inventory
            self.inventory.append('treasure')
            sleep(4)
            print(f"\nYou survived and got the treasure, you win! 💰💰💰")
            sleep(2)
            # Call final stats
            self.stats()
            # Call replay, option to start game over
            self.replay()
        # If sword not in inventory, ghost attacks you and you die
        else:
            sleep(2)
            print("\nYou don't appear to have any weapon to defend yourself, maybe you missed something along the way!")
            sleep(3)
            print("\nThe ghost attacks you and you die, game over!")
            # Call replay, option to start game over
            self.replay()


    def room_choice(self):
        """Gives choice of moving to next room or hallway"""
        print("\nWould you like to go back to the Hallway or to the next room?\n1.Hallway\n2.Next Room")
        choice = self.choice_validation()
        if choice == "1":
            # Go to hallway (room)
            self.hallway()
        else:
            # Go to kitchen (room)
            self.kitchen()

    
    def ghost(self):
        """Ghost gameplay, play a game against the ghost to get the key"""
        print("\nAs you approach the ghostly figure, you see it's an old lady and she begins to speak to you....")
        print("\nYou are brave to approach me young one! I might have something that can assist you, but you will have to win a game against me before i will give it to you.\n")
        print("Would you like to play?\n1.Yes\n2.No")
        # Check choice validation       
        choice = self.choice_validation()
        if choice == "1":
            # List of functions
            functions = [rps.rock_paper_scissors, self.roll_a_double_func]
            # Randomise functions
            selected_function = random.choice(functions)
            # Selected game from function list
            game = selected_function()
            # If won (if game give a boolean value of true)
            if game: 
                # Adds key to inventory
                self.inventory.append ('key')
                print("\nHere is your reward! A key!")
                sleep(2)
            # If lost (if game give a boolean value of false)
            else:
                print("\nYou don't get any reward! Sorry.")
        # Call room choice (hallway or next room)
        self.room_choice()

    def replay(self):
        """Option to replay game, retaining player name but re-setting the other stats"""
        sleep(2)
        print("\nPlay again?\n1.Yes\n2.No")
        # Check choice validation 
        choice = self.choice_validation()
        if choice == "1": 
            # Call intro (back to start)
            self.hp = MAX_HEALTH
            self.inventory = []
            self.health_potion_collected = False
            self.intro()   
        # End game      
        else:
            print("\nGoodbye")
            quit()
    

my_player = Player()
my_player.player_name()
my_player.intro()

#player_name = Player.player_name(my_player)
#start_game = Player.intro(my_player)

###Testing working with classes###
#attack = player.health_attack(my_player)
#print(attack)
#print(my_player.name)
