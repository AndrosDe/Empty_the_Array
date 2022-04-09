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


def computer_tiles(dice_sum):
    """
    Closing the appropriate tiles if they are open with the
    remove() method to remove an element from the array.
    """

    value_dice = f"{dice_sum}, so Python can close tile... "
    value_error = "Nothing! No tiles to close, ending the Pythons turn."

    # Defining the variables that will be the parameters
    # for the closing tile functions
    one = dice_sum - (dice_sum - 1)  # One
    two = dice_sum - (dice_sum - 2)  # Two
    three = dice_sum - (dice_sum - 3)  # Three
    four = dice_sum - (dice_sum - 4)  # Four
    five = dice_sum - (dice_sum - 5)  # Five

    one_less = dice_sum - 1  # One less than dice_sum
    two_less = dice_sum - 2  # Two less than dice_sum
    three_less = dice_sum - 3  # Three less than dice_sum
    four_less = dice_sum - 4  # Four less than dice_sum
    five_less = dice_sum - 5  # Five less than dice_sum

    def closing_one_tile(dice_sum):
        """
        Closing one tile taking dice_sum
        """
        index = computer_array.index(dice_sum)
        computer_array.insert(index, "X")
        computer_array.remove(dice_sum)
        print(value_dice + f" {dice_sum}.")

    def closing_two_tiles(i, j):
        """
        Closing two tiles, according to the parameters
        """
        if (i, j) in computer_array:
            index_i = computer_array.index(i)
            index_j = computer_array.index(j)
            computer_array.insert(index_i, "X")
            computer_array.insert(index_j, "X")
            computer_array.remove(i)
            computer_array.remove(j)
            print(value_dice + f" {i} and {j}.")
        else:
            computer_array.remove(100)

    def closing_three_tiles(i, j):
        """
        Closing three tiles, according to the parameters
        """
        k = dice_sum - (i + j)
        if (i, j, k) in computer_array:
            index_i = computer_array.index(i)
            index_j = computer_array.index(j)
            index_k = computer_array.index(k)
            computer_array.insert(index_i, "X")
            computer_array.insert(index_j, "X")
            computer_array.insert(index_k, "X")
            computer_array.remove(i)
            computer_array.remove(j)
            computer_array.remove(k)
            print(value_dice + f" {i}, {j} and {k}.")
        else:
            computer_array.remove(100)

    try:
        closing_one_tile(dice_sum)
    except ValueError:
        try:
            closing_two_tiles(one, one_less)
        except ValueError:
            try:
                closing_two_tiles(two, two_less)
            except ValueError:
                try:
                    closing_two_tiles(three, three_less)
                except ValueError:
                    try:
                        closing_two_tiles(four, four_less)
                    except ValueError:
                        try:
                            closing_two_tiles(five, five_less)
                        except ValueError:
                            try:
                                closing_three_tiles(one, two)
                            except ValueError:
                                try:
                                    closing_three_tiles(one, three)
                                except ValueError:
                                    try:
                                        closing_three_tiles(one, four)
                                    except ValueError:
                                        try:
                                            closing_three_tiles(one, five)
                                        except ValueError:
                                            try:
                                                closing_three_tiles(two, three)
                                            except ValueError:
                                                try:
                                                    closing_three_tiles(two, four)
                                                except ValueError:
                                                    try:
                                                        closing_three_tiles(three, four)
                                                    except ValueError:
                                                        print(value_dice + value_error)

    print(f"Pythons tiles are: {computer_array}\n")


def player_input(dice_sum):
    """
    Here we ask the player for stating how many tiles are to close in this round.
    Should an invalid entry be made, the input request will be repeated.
    """
    print("How many tiles do you want to close in this round?\n")
    value_player = input("Please enter one, two, three or none to continue: ")

    if value_player == "one":
        player_input_one(dice_sum)
    elif value_player == "two":
        player_input_two(dice_sum)
    elif value_player == "three":
        player_input_three(dice_sum)
    elif value_player == "none":
        print("Nothing! No tiles to close, ending the your turn.")
    else:
        print("Invalid input, you need to select one, two or three to continue.")
        player_input(dice_sum)


def player_input_one(dice_sum):
    """
    Here we ask the player for the tile to close in this round.
    It will be checked if the input matches the sum of bot dices and if the tiles is still open in the array.
    Should an invalid entry be made, the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    one_tile_choosen = input("Please enter the tile to close:\n")
    tile_set_one = int(one_tile_choosen)
    print(tile_set_one)

    if tile_set_one == dice_sum:
        if tile_set_one in player_array:
            index = player_array.index(tile_set_one)
            player_array.insert(index, "X")
            player_array.remove(tile_set_one)
            print(f"Closing tile {tile_set_one}.")
        else:
            print("This tile was already closed. Another tile mus be selected.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'one' tile, the value must match the value of both dices.")
        player_input(dice_sum)

    print(f"Your left-over tiles are: {player_array}\n")


def player_input_two(dice_sum):
    """
    Here we ask the player for two tiles to close in this round.
    It will be checked if the sum of the input matches the sum of bot dices and if the tiles is still open in the array.
    Should an invalid entry be made, the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    two_tile_choosen = input("Please enter the two tile to close:\n")
    tile_set_two = int(two_tile_choosen)
    print(tile_set_two)

    if sum(tile_set_two) == dice_sum:
        i = tile_set_two[0]
        j = tile_set_two[1]
        if (i, j) in player_array:
            index_i = player_array.index(i)
            index_j = player_array.index(j)
            player_array.insert(index_i, "X")
            player_array.insert(index_j, "X")
            player_array.remove(i)
            player_array.remove(j)
            print(f"Closing tiles {i} and {j}.")
        else:
            print("This tile was already closed and you must close both of them. Other tiles mus be selected.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'two' tiles, the value of both tiles must match the value of both dices.")
        player_input(dice_sum)

    print(f"Your left-over tiles are: {player_array}\n")


def player_input_three(dice_sum):
    """
    Here we ask the player for three tile to close in this round.
    It will be checked if the sum input matches the sum of bot dices and if the tiles is still open in the array.
    Should an invalid entry be made, the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    three_tile_choosen = input("Please enter the three tile to close:\n")
    tile_set_three = int(three_tile_choosen)
    print(tile_set_three)

    if sum(tile_set_three) == dice_sum:
        i = tile_set_three[0]
        j = tile_set_three[1]
        k = tile_set_three[2]
        if {i, j, k} in player_array:
            index_i = player_array.index(i)
            index_j = player_array.index(j)
            index_k = player_array.index(k)
            player_array.insert(index_i, "X")
            player_array.insert(index_j, "X")
            player_array.insert(index_k, "X")
            player_array.remove(i)
            player_array.remove(j)
            player_array.remove(k)
            print(f"Closing tiles {i}, {j} and {k}.")
        else:
            print("This tile was already closed and you must close all of them. Other tiles mus be selected.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'three' tiles, the value of all tiles must match the value of both dices.")
        player_input(dice_sum)

    print(f"Your left-over tiles are: {player_array}\n")


def start(name):
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
        start(name)
    elif start_or_rules == 'game':
        game_round(name)
    else:
        print("Invalid entry, please enter 'game' to start a game or 'rules' to read the rules:\n")
        start(name)


def game_round(name):
    """
    This defines a round for the game:
    A round has:
    1. The players trun:
    -> rolling the dice
    -> imput of the tiles to close
    -> closing the tiles
    2. The computers turn:
    -> rolling the dice
    -> closing the tiles

    This is repeated 9 times or until one of the arrys is empty.
    """
    i = 1
    while i <= 9:
        print(f"Round {i}\n")

        print("You are rolling your dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"{name} rolled {dice_one} and a {dice_two}")

        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        player_input(dice_sum)

        print("Python is rolling the dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"Python rolled {dice_one} and a {dice_two}")

        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        computer_tiles(dice_sum)

        input("Please press any key to continue.\n")
        if player_array == ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'] or computer_array == ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']:
            break
        i += 1


def main():
    """
    This is the main function.
    """
    print("Welcome to the 'Shut the box'- Game")

    name = input("Please enter your name: ")
    print(f"Hello {name}.\nWould you like to start a new game or read the game rules?")

    start(name)

# Here we call up the game:


player_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
main()
