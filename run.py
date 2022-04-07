# WELLCOME TO "THE SHUT THE BOX" DICE-GAME PYTHON CODE
# Shut the box (also called canoga, batten down the hatches or trick-track)
# is a game of dice for one or more players.
# Traditionally, a counting box is used with tiles numbered 1 to 9.
# More can information on the game can be found here:
# https://en.wikipedia.org/wiki/Shut_the_box

# Modules:
""" The random module will be used for the dice roll. """
import random


def game_rules():
    """
    Here the player gets a print out on how to play the game.
    """
    rule = '''
At the start of the game you will start with a full list from 1 to 9.
During the game, each player plays in turn for 9 rounds or if a list is empty,
after which the remaining entries in the list are sum up.
The player with the lowest sum will win the match.

A round will playout like this:
The player begins the their turn by rolling the die or dice.
After throwing, the player adds up (or subtracts) the dice and then removes one
of any combination of open numbers that sums to the total number of the dices.

For example, if the total number is 8 the player may choose any of the
following sets of numbers (if all of the numbers are available in the list):
    - 8
    - 7, 1
    - 6, 2
    - 5, 3
    - 5, 2, 1
    - 4, 3, 1

Then the next players turn comes and chooses a set of tiles to close.
If the dice yield now numbers to close any tile, then the player must "pass".

Calculating Score:
At the 9th round or when the one of the player has an empty list,
the players scores the sum of remaining numbers in the list.
For example, if the numbers 2, 3, and 5 are still open the player's score is
10 (2 + 3 + 5 = 10).
'''
    print(rule)


def dice_roll():
    """
    This will create a random number between 1 and 6.
    Just like a dice with 6 sides would do.
    """
    dice = random.randrange(1, 6)
    return dice


def computer_turn():
    """
    A turn has two parts to it:
    1. rolling the dice and generating the sum of the dice
    2. closing the appropriate tiles if they are open.
    """
    print("Python is rolling the dice...\n")
    dice_roll()

    dice_one = dice_roll()
    dice_two = dice_roll()
    print(f"Python rolled {dice_one} and a {dice_two}")

    dice_sum = dice_sum = dice_one + dice_two
    print(f"The sum of the dices are {dice_sum}.\n")

    # to "close" the tiles we use the remove() method
    # to remove an element from the array
    value_dice = f"{dice_sum}, so I can remove..."
    value_error = "Nothing! No tiles to close, ending the my turn"

    if dice_sum == 2:
        print(value_dice)
        # try to remove 2, if not possible remove 1
        try:
            computer_tiles.remove(1)
            print(" a 1.")
        except ValueError:
            try:
                computer_tiles.remove(2)
                print(" a 2.")
            except ValueError:
                print(value_error)
    elif dice_sum == 3:
        print(value_dice)
        # try to remove 3 or 2, 1
        try:
            computer_tiles.remove(2)
            computer_tiles.remove(1)
            print(" a 2 and a 1.")
        except ValueError:
            try:
                computer_tiles.remove(3)
                print(" a 3")
            except ValueError:
                print(value_error)
    elif dice_sum == 4:
        print(value_dice)
        # try to remove 4 or 2 or 3,1
        try:
            computer_tiles.remove(4)
            print(" a 4.")
        except ValueError:
            try:
                computer_tiles.remove(1)
                computer_tiles.remove(3)
                print(" 3 and 1.")
            except ValueError:
                print(value_error)
    elif dice_sum == 5:
        print(value_dice)
        # try to remove 5 or 3, 2 or 4,1
        try:
            computer_tiles.remove(5)
            print(" a 5.")
        except ValueError:
            try:
                computer_tiles.remove(1)
                computer_tiles.remove(4)
                print(" 4 and 1.")
            except ValueError:
                try:
                    computer_tiles.remove(2)
                    computer_tiles.remove(3)
                    print(" 3 and 2.")
                except ValueError:
                    print(value_error)
    elif dice_sum == 6:
        print(value_dice)
        # try to remove 6 or 3 or 4, 2
        try:
            computer_tiles.remove(6)
            print(" a 6.")
        except ValueError:
            try:
                computer_tiles.remove(3)
                print(" a 3.")
            except ValueError:
                try:
                    computer_tiles.remove(2)
                    computer_tiles.remove(4)
                    print(" 4 and 2.")
                except ValueError:
                    print(value_error)
    elif dice_sum == 7:
        print(value_dice)
        # try to remove 7 or 6,1 or 5,2 or 4,3 or 3,2,1
        try:
            computer_tiles.remove(7)
            print(" a 7.")
        except ValueError:
            try:
                computer_tiles.remove(6)
                computer_tiles.remove(1)
                print(" 6 and 1.")
            except ValueError:
                try:
                    computer_tiles.remove(5)
                    computer_tiles.remove(2)
                    print(" 5 and 2.")
                except ValueError:
                    try:
                        computer_tiles.remove(4)
                        computer_tiles.remove(3)
                        print(" 4 and 3.")
                    except ValueError:
                        try:
                            computer_tiles.remove(4)
                            computer_tiles.remove(2)
                            computer_tiles.remove(1)
                            print(" 4, 2 and 1.")
                        except ValueError:
                            print(value_error)
    elif dice_sum == 8:
        print(value_dice)
        # try to remove 8 or 7,1 or 6,2 or 5,3 or 5,2,1 or 4,3,1
        try:
            computer_tiles.remove(8)
            print(" a 8.")
        except ValueError:
            try:
                computer_tiles.remove(7)
                computer_tiles.remove(1)
                print(" 7 and 1.")
            except ValueError:
                try:
                    computer_tiles.remove(6)
                    computer_tiles.remove(2)
                    print(" 6 and 2.")
                except ValueError:
                    try:
                        computer_tiles.remove(5)
                        computer_tiles.remove(3)
                        print(" 5 and 3.")
                    except ValueError:
                        try:
                            computer_tiles.remove(5)
                            computer_tiles.remove(2)
                            computer_tiles.remove(1)
                            print(" 5, 2 and 1.")
                        except ValueError:
                            try:
                                computer_tiles.remove(4)
                                computer_tiles.remove(3)
                                computer_tiles.remove(1)
                                print(" 4, 3 and 1.")
                            except ValueError:
                                print(value_error)
    elif dice_sum == 9:
        print(value_dice)
        # try to remove 9 or 8,1 or 7,2 or 6,3 or 5,4 or 5,3,1 or 4,3,2
        try:
            computer_tiles.remove(9)
            print(" a 9.")
        except ValueError:
            try:
                computer_tiles.remove(8)
                computer_tiles.remove(1)
                print(" 8 and 1.")
            except ValueError:
                try:
                    computer_tiles.remove(7)
                    computer_tiles.remove(2)
                    print(" 7 and 2.")
                except ValueError:
                    try:
                        computer_tiles.remove(6)
                        computer_tiles.remove(3)
                        print(" 6 and 3.")
                    except ValueError:
                        try:
                            computer_tiles.remove(5)
                            computer_tiles.remove(4)
                            print(" 5 and 4.")
                        except ValueError:
                            try:
                                computer_tiles.remove(5)
                                computer_tiles.remove(3)
                                computer_tiles.remove(1)
                                print(" 5, 3 and 1.")
                            except ValueError:
                                try:
                                    computer_tiles.remove(4)
                                    computer_tiles.remove(3)
                                    computer_tiles.remove(2)
                                    print(" 4, 3 and 2.")
                                except ValueError:
                                    print(value_error)
    elif dice_sum == 10:
        print(value_dice)
        # try to remove 9,1 or 8,2 or 7,3 or 6,4 or 6,3,1 or 5,4,1, or 5,3,2
        try:
            computer_tiles.remove(9)
            computer_tiles.remove(1)
            print(" 9 and 1.")
        except ValueError:
            try:
                computer_tiles.remove(8)
                computer_tiles.remove(2)
                print(" 8 and 2.")
            except ValueError:
                try:
                    computer_tiles.remove(7)
                    computer_tiles.remove(3)
                    print(" 7 and 3.")
                except ValueError:
                    try:
                        computer_tiles.remove(6)
                        computer_tiles.remove(4)
                        print(" 6 and 4.")
                    except ValueError:
                        try:
                            computer_tiles.remove(6)
                            computer_tiles.remove(3)
                            computer_tiles.remove(1)
                            print(" 6, 3 and 1.")
                        except ValueError:
                            try:
                                computer_tiles.remove(5)
                                computer_tiles.remove(4)
                                computer_tiles.remove(1)
                                print(" 5, 4 and 1.")
                            except ValueError:
                                try:
                                    computer_tiles.remove(5)
                                    computer_tiles.remove(3)
                                    computer_tiles.remove(2)
                                    print(" 5, 3 and 2.")
                                except ValueError:
                                    print(value_error)
    elif dice_sum == 11:
        print(value_dice)
        # try to remove 9,2 or 8,3 or 7,4 or 6,5
        # or 7,3,1 or 6,4,1 or 6,3,2 or 5,4,2
        try:
            computer_tiles.remove(9)
            computer_tiles.remove(2)
            print(" 9 and 2.")
        except ValueError:
            try:
                computer_tiles.remove(8)
                computer_tiles.remove(3)
                print(" 8 and 3.")
            except ValueError:
                try:
                    computer_tiles.remove(7)
                    computer_tiles.remove(4)
                    print(" 7 and 4.")
                except ValueError:
                    try:
                        computer_tiles.remove(6)
                        computer_tiles.remove(5)
                        print(" 6 and 5.")
                    except ValueError:
                        try:
                            computer_tiles.remove(7)
                            computer_tiles.remove(3)
                            computer_tiles.remove(1)
                            print(" 7, 3 and 1.")
                        except ValueError:
                            try:
                                computer_tiles.remove(6)
                                computer_tiles.remove(4)
                                computer_tiles.remove(1)
                                print(" 6, 4 and 1.")
                            except ValueError:
                                try:
                                    computer_tiles.remove(6)
                                    computer_tiles.remove(3)
                                    computer_tiles.remove(2)
                                    print(" 6, 3 and 2.")
                                except ValueError:
                                    try:
                                        computer_tiles.remove(5)
                                        computer_tiles.remove(4)
                                        computer_tiles.remove(2)
                                        print(" 5, 4 and 2.")
                                    except ValueError:
                                        print(value_error)
    elif dice_sum == 12:
        print(value_dice)
        # try to remove 9,3 or 9,2,1 or 8,4 or 8,3,1 or 7,5
        # or 7,4,1 or 7,3,2 or 6,4,2 or 6,5,1 or 5,4,3
        try:
            computer_tiles.remove(9)
            computer_tiles.remove(3)
            print(" 9 and 3.")
        except ValueError:
            try:
                computer_tiles.remove(9)
                computer_tiles.remove(2)
                computer_tiles.remove(1)
                print(" 9, 2 and 1.")
            except ValueError:
                try:
                    computer_tiles.remove(8)
                    computer_tiles.remove(4)
                    print(" 8 and 4.")
                except ValueError:
                    try:
                        computer_tiles.remove(8)
                        computer_tiles.remove(3)
                        computer_tiles.remove(1)
                        print(" 8, 3 and 1.")
                    except ValueError:
                        try:
                            computer_tiles.remove(7)
                            computer_tiles.remove(5)
                            print(" 7and 5.")
                        except ValueError:
                            try:
                                computer_tiles.remove(7)
                                computer_tiles.remove(4)
                                computer_tiles.remove(1)
                                print(" 7, 4 and 1.")
                            except ValueError:
                                try:
                                    computer_tiles.remove(7)
                                    computer_tiles.remove(3)
                                    computer_tiles.remove(2)
                                    print(" 7, 3 and 2.")
                                except ValueError:
                                    try:
                                        computer_tiles.remove(6)
                                        computer_tiles.remove(4)
                                        computer_tiles.remove(2)
                                        print(" 6, 4 and 2.")
                                    except ValueError:
                                        try:
                                            computer_tiles.remove(6)
                                            computer_tiles.remove(5)
                                            computer_tiles.remove(1)
                                            print(" 6, 5 and 1.")
                                        except ValueError:
                                            try:
                                                computer_tiles.remove(5)
                                                computer_tiles.remove(4)
                                                computer_tiles.remove(3)
                                                print(" 5, 4 and 3.")
                                            except ValueError:
                                                print(value_error)

    print(f"Pythons left-over tiles are: {computer_tiles}\n")


def player_turn():
    """
    A turn has two parts to it:
    1. rolling the dice and generating the sum of the dice
    2. closing the appropriate tiles if they are open.
    """

    print("You are rolling your dice...\n")
    dice_roll()

    dice_one = dice_roll()
    dice_two = dice_roll()
    print(f"{name} rolled {dice_one} and a {dice_two}")

    dice_sum = dice_sum = dice_one + dice_two
    print(f"The sum of the dices are {dice_sum}.\n")

    # tile_choosen = input("Please choose the tiles to close:\n")

    # to "close" the tiles we use the remove() method
    # to remove an element from the array
    value_dice = f"{dice_sum}, so you can remove..."
    value_error = "Nothing! No tiles to close, ending the your turn"

    if dice_sum == 2:
        print(value_dice)
        # try to remove 2, if not possible remove 1
        try:
            player_tiles.remove(1)
            print(" a 1.")
        except ValueError:
            try:
                player_tiles.remove(2)
                print(" a 2.")
            except ValueError:
                print(value_error)
    elif dice_sum == 3:
        print(value_dice)
        # try to remove 3 or 2, 1
        try:
            player_tiles.remove(2)
            player_tiles.remove(1)
            print(" a 2 and a 1.")
        except ValueError:
            try:
                player_tiles.remove(3)
                print(" a 3")
            except ValueError:
                print(value_error)
    elif dice_sum == 4:
        print(value_dice)
        # try to remove 4 or 2 or 3,1
        try:
            player_tiles.remove(4)
            print(" a 4.")
        except ValueError:
            try:
                player_tiles.remove(1)
                player_tiles.remove(3)
                print(" 3 and 1.")
            except ValueError:
                print(value_error)
    elif dice_sum == 5:
        print(value_dice)
        # try to remove 5 or 3, 2 or 4,1
        try:
            player_tiles.remove(5)
            print(" a 5.")
        except ValueError:
            try:
                player_tiles.remove(1)
                player_tiles.remove(4)
                print(" 4 and 1.")
            except ValueError:
                try:
                    player_tiles.remove(2)
                    player_tiles.remove(3)
                    print(" 3 and 2.")
                except ValueError:
                    print(value_error)
    elif dice_sum == 6:
        print(value_dice)
        # try to remove 6 or 3 or 4, 2
        try:
            player_tiles.remove(6)
            print(" a 6.")
        except ValueError:
            try:
                player_tiles.remove(3)
                print(" a 3.")
            except ValueError:
                try:
                    player_tiles.remove(2)
                    player_tiles.remove(4)
                    print(" 4 and 2.")
                except ValueError:
                    print(value_error)
    elif dice_sum == 7:
        print(value_dice)
        # try to remove 7 or 6,1 or 5,2 or 4,3 or 3,2,1
        try:
            player_tiles.remove(7)
            print(" a 7.")
        except ValueError:
            try:
                player_tiles.remove(6)
                player_tiles.remove(1)
                print(" 6 and 1.")
            except ValueError:
                try:
                    player_tiles.remove(5)
                    player_tiles.remove(2)
                    print(" 5 and 2.")
                except ValueError:
                    try:
                        player_tiles.remove(4)
                        player_tiles.remove(3)
                        print(" 4 and 3.")
                    except ValueError:
                        try:
                            player_tiles.remove(4)
                            player_tiles.remove(2)
                            player_tiles.remove(1)
                            print(" 4, 2 and 1.")
                        except ValueError:
                            print(value_error)
    elif dice_sum == 8:
        print(value_dice)
        # try to remove 8 or 7,1 or 6,2 or 5,3 or 5,2,1 or 4,3,1
        try:
            player_tiles.remove(8)
            print(" a 8.")
        except ValueError:
            try:
                player_tiles.remove(7)
                player_tiles.remove(1)
                print(" 7 and 1.")
            except ValueError:
                try:
                    player_tiles.remove(6)
                    player_tiles.remove(2)
                    print(" 6 and 2.")
                except ValueError:
                    try:
                        player_tiles.remove(5)
                        player_tiles.remove(3)
                        print(" 5 and 3.")
                    except ValueError:
                        try:
                            player_tiles.remove(5)
                            player_tiles.remove(2)
                            player_tiles.remove(1)
                            print(" 5, 2 and 1.")
                        except ValueError:
                            try:
                                player_tiles.remove(4)
                                player_tiles.remove(3)
                                player_tiles.remove(1)
                                print(" 4, 3 and 1.")
                            except ValueError:
                                print(value_error)
    elif dice_sum == 9:
        print(value_dice)
        # try to remove 9 or 8,1 or 7,2 or 6,3 or 5,4 or 5,3,1 or 4,3,2
        try:
            player_tiles.remove(9)
            print(" a 9.")
        except ValueError:
            try:
                player_tiles.remove(8)
                player_tiles.remove(1)
                print(" 8 and 1.")
            except ValueError:
                try:
                    player_tiles.remove(7)
                    player_tiles.remove(2)
                    print(" 7 and 2.")
                except ValueError:
                    try:
                        player_tiles.remove(6)
                        player_tiles.remove(3)
                        print(" 6 and 3.")
                    except ValueError:
                        try:
                            player_tiles.remove(5)
                            player_tiles.remove(4)
                            print(" 5 and 4.")
                        except ValueError:
                            try:
                                player_tiles.remove(5)
                                player_tiles.remove(3)
                                player_tiles.remove(1)
                                print(" 5, 3 and 1.")
                            except ValueError:
                                try:
                                    player_tiles.remove(4)
                                    player_tiles.remove(3)
                                    player_tiles.remove(2)
                                    print(" 4, 3 and 2.")
                                except ValueError:
                                    print(value_error)
    elif dice_sum == 10:
        print(value_dice)
        # try to remove 9,1 or 8,2 or 7,3 or 6,4 or 6,3,1 or 5,4,1, or 5,3,2
        try:
            player_tiles.remove(9)
            player_tiles.remove(1)
            print(" 9 and 1.")
        except ValueError:
            try:
                player_tiles.remove(8)
                player_tiles.remove(2)
                print(" 8 and 2.")
            except ValueError:
                try:
                    player_tiles.remove(7)
                    player_tiles.remove(3)
                    print(" 7 and 3.")
                except ValueError:
                    try:
                        computer_tiles.remove(6)
                        computer_tiles.remove(4)
                        print(" 6 and 4.")
                    except ValueError:
                        try:
                            player_tiles.remove(6)
                            player_tiles.remove(3)
                            player_tiles.remove(1)
                            print(" 6, 3 and 1.")
                        except ValueError:
                            try:
                                player_tiles.remove(5)
                                player_tiles.remove(4)
                                player_tiles.remove(1)
                                print(" 5, 4 and 1.")
                            except ValueError:
                                try:
                                    player_tiles.remove(5)
                                    player_tiles.remove(3)
                                    player_tiles.remove(2)
                                    print(" 5, 3 and 2.")
                                except ValueError:
                                    print(value_error)
    elif dice_sum == 11:
        print(value_dice)
        # try to remove 9,2 or 8,3 or 7,4 or 6,5
        # or 7,3,1 or 6,4,1 or 6,3,2 or 5,4,2
        try:
            player_tiles.remove(9)
            player_tiles.remove(2)
            print(" 9 and 2.")
        except ValueError:
            try:
                player_tiles.remove(8)
                player_tiles.remove(3)
                print(" 8 and 3.")
            except ValueError:
                try:
                    player_tiles.remove(7)
                    player_tiles.remove(4)
                    print(" 7 and 4.")
                except ValueError:
                    try:
                        player_tiles.remove(6)
                        player_tiles.remove(5)
                        print(" 6 and 5.")
                    except ValueError:
                        try:
                            player_tiles.remove(7)
                            player_tiles.remove(3)
                            player_tiles.remove(1)
                            print(" 7, 3 and 1.")
                        except ValueError:
                            try:
                                player_tiles.remove(6)
                                player_tiles.remove(4)
                                player_tiles.remove(1)
                                print(" 6, 4 and 1.")
                            except ValueError:
                                try:
                                    player_tiles.remove(6)
                                    player_tiles.remove(3)
                                    player_tiles.remove(2)
                                    print(" 6, 3 and 2.")
                                except ValueError:
                                    try:
                                        player_tiles.remove(5)
                                        player_tiles.remove(4)
                                        player_tiles.remove(2)
                                        print(" 5, 4 and 2.")
                                    except ValueError:
                                        print(value_error)
    elif dice_sum == 12:
        print(value_dice)
        # try to remove 9,3 or 9,2,1 or 8,4 or 8,3,1 or 7,5
        # or 7,4,1 or 7,3,2 or 6,4,2 or 6,5,1 or 5,4,3
        try:
            player_tiles.remove(9)
            player_tiles.remove(3)
            print(" 9 and 3.")
        except ValueError:
            try:
                player_tiles.remove(9)
                player_tiles.remove(2)
                player_tiles.remove(1)
                print(" 9, 2 and 1.")
            except ValueError:
                try:
                    player_tiles.remove(8)
                    player_tiles.remove(4)
                    print(" 8 and 4.")
                except ValueError:
                    try:
                        player_tiles.remove(8)
                        player_tiles.remove(3)
                        player_tiles.remove(1)
                        print(" 8, 3 and 1.")
                    except ValueError:
                        try:
                            player_tiles.remove(7)
                            player_tiles.remove(5)
                            print(" 7and 5.")
                        except ValueError:
                            try:
                                player_tiles.remove(7)
                                player_tiles.remove(4)
                                player_tiles.remove(1)
                                print(" 7, 4 and 1.")
                            except ValueError:
                                try:
                                    player_tiles.remove(7)
                                    player_tiles.remove(3)
                                    player_tiles.remove(2)
                                    print(" 7, 3 and 2.")
                                except ValueError:
                                    try:
                                        player_tiles.remove(6)
                                        player_tiles.remove(4)
                                        player_tiles.remove(2)
                                        print(" 6, 4 and 2.")
                                    except ValueError:
                                        try:
                                            player_tiles.remove(6)
                                            player_tiles.remove(5)
                                            player_tiles.remove(1)
                                            print(" 6, 5 and 1.")
                                        except ValueError:
                                            try:
                                                player_tiles.remove(5)
                                                player_tiles.remove(4)
                                                player_tiles.remove(3)
                                                print(" 5, 4 and 3.")
                                            except ValueError:
                                                print(value_error)

    print(f"My left-over tiles are: {player_tiles}\n")


def start():
    """
    This is the start up function where a player
    can read the rules or start up the game.
    """
    start_or_rules = input("""Please enter:
    - 'game' to start a game
    - 'rules' to read the rules
    """)
    if start_or_rules == 'rules':
        game_rules()
        start()
    elif start_or_rules == 'game':
        main()
    else:
        print("Invalid entry, please enter 'game' to start a game or 'rules' to read the rules:\n")
        start()


def main():
    """
    This is the main game function to play the game
    """
    i = 1
    while i < 9:
        print(f"Round {i}\n")
        player_turn()
        computer_turn()
        if player_tiles == [] or computer_tiles == []:
            break
        i += 1


# Here we call up the game:
print("Welcome to the 'Shut the box'- Game")
name = input("Please enter your name: ")
print(f"Hello {name}.\nWould you like to start a new game or read the game rules?")
player_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start()
