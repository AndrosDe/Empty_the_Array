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


def start():
    """
    This is the start up function where a player can read the rules or start up the game.
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
    # Variables
    dice_one = dice_roll()
    dice_two = dice_roll()

    print(f"{name} rolled a {dice_one} and a {dice_two}")


# Here we call up the game:
print("Welcome to the 'Shut the box'- Game")
name = input("Please enter your name: ")
print(f"Hello {name}.\nWould you like to start a new game or read how the game is played?")
start()
