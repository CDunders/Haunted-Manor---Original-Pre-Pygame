import random

NUM_PAIRS = 3
TURNS = 6

def main():

    list = truth_list()
    shuffled = shuffle_list(list)
    display = displayed_list(shuffled)

    # Intro
    print(f"\nWelcome to the memory game! You will have {TURNS} turns to uncover {NUM_PAIRS} number matches and will use the index to uncover a value.")
    print("(index starts at 0)")
    print("\nLet's begin!\n")
    # Display hidden list
    print(f"{display}\n") 

    # If still have turn remaining
    for i in range(TURNS):
        if "*" in display:
            index_values = get_valid_index(display) 
            if checking_correct(index_values, shuffled, display):
                return True
    #if "*" in display_list
    print("\nSorry, you have ran out of turns. You have lost!")
    return False


def truth_list():
    # Create truth list
    list = []
    for i in range(NUM_PAIRS):
        list.append(i)
        list.append(i)
    return list


def shuffle_list(list):
    # Shuffle list
    random.shuffle(list)
    return list


def displayed_list(shuffled_list):
    # Create a displayed list
    # Keep track of a separate list, which is the one to display to the user. We use the '*' symbol to denote that a value is hidden to the user
    displayed_list = []
    for i in range(len(shuffled_list)):
        displayed_list.append("*")
    return displayed_list
    

def get_valid_index(display_list):
    # Get a valid index from the user
    guesses = 0
    numbers_picked = []

    while guesses < 2:
        try:
            user_input = int(input("Enter an index: "))

            if user_input >= 0 and user_input <= len(display_list)-1:
                if display_list[user_input] == "*":
                    if user_input in numbers_picked:
                        print("\nYou entered the same index twice. Try again.")
                    else:
                        numbers_picked.append(user_input)
                        guesses += 1
                else:
                    print("\nThis number has already been matched. Try again.")
            else: 
                print("\nNot a valid index. Try again.")

        except ValueError:
            print("\nThat's not an number!")
        
    return numbers_picked


def checking_correct(index_values, shuffled_list, display_list):
    # Check the values at indexes 
    # IF values match each other then replace astrix with the values
    # Return the updates display_list
    # Repeat until no astrix remain in disply_list

    value_1 = shuffled_list[index_values[0]]
    value_2 = shuffled_list[index_values[1]]

    if value_1 == value_2:
        display_list[index_values[0]] = value_1
        display_list[index_values[1]] = value_2     
        print("\nIt's a match!")   
        if "*" not in display_list:
            print(display_list)
            print("You won!")
            return True
    else:
        print("\nDid not match, try again!\n")

    print(display_list)
    return False


if __name__ == '__main__':
    main()