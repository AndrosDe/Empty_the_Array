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
    rule = '''At the start of the game you will start with a full list from 1 to 9.
During the game, each player plays in turn.
A player begins their turn by rolling the die or dice.
After throwing, the player adds up (or subtracts) the dice and
then removes one of any combination of open numbers
that sums to the total number of the dices.

For example, if the total number is 8 the player may choose
any of the following sets of numbers (as long as all of
the numbers are available in the list):
    - 8
    - 7, 1
    - 6, 2
    - 5, 3
    - 5, 2, 1
    - 4, 3, 1

The player then rolls the dice again, aiming to shut more numbers.
The player continues throwing the dice and shutting numbers until
reaching a point at which, given the results produced by the dice,
the player cannot shut any more numbers.
At that point, the player scores the sum of remaining numbers in the list.
For example, if the numbers 2, 3, and 5 are still open
when the player throws a one, the player's score is 10 (2 + 3 + 5 = 10).
Player then passes to the next player.

After every player has taken a turn, the player with the lowest score wins.'''
    print(rule)


def username():
    """
    This function is for the player to enter or change the name.
    """
    name = input("Please enter your name: ")
    return name


def dice_roll():
    """
    This will create a random number between 1 and 6.
    Just like a dice with 6 sides would do.
    """
    dice = random.randrange(1, 6)
    return dice


def main():
    """
    This is the main game function.
    """
    # Variables
    dice_one = dice_roll()
    dice_two = dice_roll()
    name = username()

    print(f"Hello {name}.\nWould you like to start a new game or read how the game is played?")
    start_or_rules = input("Please enter 'game' to start a game or 'rules' to read the rules:\n")
    if start_or_rules == 'rules':
        game_rules()
    else:
        print(f"{dice_one}\n{dice_two}")


# Here we call up the game:
print("Welcome to the 'Shut the box'- Game")
main()
