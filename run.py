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


def closing_one_tile(dice_sum):
    """
    Closing one tile taking dice_sum
    """
    computer_array.remove(dice_sum)


def closing_two_tiles(i, j):
    """
    Closing two tiles, according to the parameters
    """
    if i in computer_array:
        if j in computer_array:
            computer_array.remove(i)
            computer_array.remove(j)
            print(f"So Python can close... {i} and {j}.")
        else:
            raise ValueError
    else:
        raise ValueError


def closing_three_tiles(i, j, dice_sum):
    """
    Closing three tiles, with the remove() method
    to remove an element from the array
    and putting an 'X' there instead,
    according to the parameters
    """
    k = dice_sum - (i + j)
    if i in computer_array:
        if j in computer_array:
            if k in computer_array:
                computer_array.remove(i)
                computer_array.remove(j)
                computer_array.remove(k)
                print(f"So Python can close... {i}, {j} and {k}.")
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


def computer_tiles_iii(dice_sum):
    """
    Closing the three appropriate tiles, if they are open.
    """
    # Defining the variables that will be the parameters
    # for the closing tile functions
    one = dice_sum - (dice_sum - 1)  # One
    two = dice_sum - (dice_sum - 2)  # Two
    three = dice_sum - (dice_sum - 3)  # Three
    four = dice_sum - (dice_sum - 4)  # Four
    five = dice_sum - (dice_sum - 5)  # Five

    if dice_sum >= 6:
        try:
            closing_three_tiles(one, two, dice_sum)
        except ValueError:
            try:
                closing_three_tiles(one, three, dice_sum)
            except ValueError:
                try:
                    closing_three_tiles(one, four, dice_sum)
                except ValueError:
                    try:
                        closing_three_tiles(one, five, dice_sum)
                    except ValueError:
                        try:
                            closing_three_tiles(two, three, dice_sum)
                        except ValueError:
                            try:
                                closing_three_tiles(two, four, dice_sum)
                            except ValueError:
                                try:
                                    closing_three_tiles(three, four, dice_sum)
                                except ValueError:
                                    computer_tiles_ii(dice_sum)
    else:
        computer_tiles_ii(dice_sum)


def computer_tiles_ii(dice_sum):
    """
    Closing the two appropriate tiles, if they are open.
    """
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
                        computer_tiles_i(dice_sum)


def computer_tiles_i(dice_sum):
    """
    Closing the one appropriate tiles, if it is open.
    """
    value_dice = "So Python can close... "

    try:
        closing_one_tile(dice_sum)
        print(value_dice + f" {dice_sum}.")
    except ValueError:
        print(value_dice)
        print("Nothing! No tiles to close, ending the Pythons turn.")


def player_input(dice_sum):
    """
    Here we ask the player for stating
    how many tiles are to close in this round.
    Should an invalid entry be made,
    the input request will be repeated.
    """
    print("How many tiles do you want to close in this round?\n")
    value_player = input("Please enter one, two, three or none to continue: ")

    if value_player == "none":
        print("None! No tiles to close, ending the your turn.")
    elif value_player == "one":
        player_input_one(dice_sum)
    elif value_player == "two":
        player_input_two(dice_sum)
    elif value_player == "three":
        player_input_three(dice_sum)
    else:
        print("Invalid input, you need to select:")
        print("'none','one','two' or 'three' to continue.")
        player_input(dice_sum)


def player_input_one(dice_sum):
    """
    Here we ask the player for the tile to close in this round.
    It will be checked if the input matches the sum of bot dices
    and if the tiles is still open in the array.
    Should an invalid entry be made
    the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    one_tile_choosen = input("Please enter the tile to close:\n")
    tile_set_one = int(one_tile_choosen)

    try:
        tile = [int(tile_set_one)]
        if len(tile) != 1:
            player_input(dice_sum)
            raise ValueError(
                f"One number is needed, you provided {len(tile_set_one)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    if tile_set_one == dice_sum:
        if tile_set_one in player_array:
            player_array.remove(tile_set_one)
            print(f"Closing tile {tile_set_one}.")
        else:
            print("This tile was already closed.")
            print("Another tile must be selected.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'one' tile,")
        print("the value must match the value of both dices.")
        player_input(dice_sum)


def player_input_two(dice_sum):
    """
    Here we ask the player for two tiles to close in this round.
    It will be checked if the sum of the input matches
    the sum of bot dices and if the tiles is still open in the array.
    Should an invalid entry be made,
    the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    print("Please enter the two tile to close.")
    two_tile_choosen = input("For example: 7, 1\n")
    tile_set_two = two_tile_choosen.split(",")

    try:
        [int(tile) for tile in tile_set_two]
        if len(tile_set_two) != 2:
            player_input(dice_sum)
            raise ValueError(
                f"Two numbers are needed, you provided {len(tile_set_two)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    tile_list = [int(tile) for tile in tile_set_two]

    if tile_list[0] == tile_list[1]:
        print("Invalid numbers, please choose different numbers.")
        player_input_two(dice_sum)

    if sum(tile_list) == dice_sum:
        i = tile_list[0]
        j = tile_list[1]
        if i in player_array:
            if j in player_array:
                player_array.remove(i)
                player_array.remove(j)
                print(f"Closing tiles {i} and {j}.")
            else:
                print("This tile was already closed and you must close both.")
                print("Please select different tiles.")
                player_input(dice_sum)
        else:
            print("This tile was already closed and you must close both.")
            print("Please select different tiles.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'two' tiles,")
        print("the value of both tiles must match the value of both dices.")
        player_input(dice_sum)


def player_input_three(dice_sum):
    """
    Here we ask the player for three tile to close in this round.
    It will be checked if the sum input matches the sum of bot dices
    and if the tiles is still open in the array.
    Should an invalid entry be made,
    the previous input request will be repeated.
    If all is fine the tile will be closed.
    """
    tile_closed = "This tile was already closed and you must close all tiles."
    three_tile_choosen = input("Please enter the three tile to close:\n")
    tile_set_three = three_tile_choosen.split(",")

    try:
        [int(tile) for tile in tile_set_three]
        if len(tile_set_three) != 3:
            player_input(dice_sum)
            raise ValueError(
                f"Two numbers are needed, you provided {len(tile_set_three)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    tile_list = [int(tile) for tile in tile_set_three]

    if tile_list[0] == tile_list[1]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)
    elif tile_list[1] == tile_list[2]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)
    elif tile_list[0] == tile_list[2]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)

    if sum(tile_list) == dice_sum:
        i = tile_list[0]
        j = tile_list[1]
        k = tile_list[2]
        if i in player_array:
            if j in player_array:
                if k in player_array:
                    player_array.remove(i)
                    player_array.remove(j)
                    player_array.remove(k)
                    print(f"Closing tiles {i}, {j} and {k}.")
                else:
                    print(tile_closed)
                    print("Please select different tiles.")
                    player_input(dice_sum)
            else:
                print(tile_closed)
                print("Please select different tiles.")
                player_input(dice_sum)
        else:
            print(tile_closed)
            print("Please select different tiles.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'three' tiles,")
        print("the value of all tiles must match the value of both dices.")
        player_input(dice_sum)


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
        print("Invalid entry, please enter:")
        print("'game' to start a game")
        print("'rules' to read the rules:\n")
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
    empty = []

    while i <= 9:
        print(f"***** Round {i} ******\n")

        print("You are rolling your dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"{name} rolled {dice_one} and a {dice_two}")

        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        print(f"Your tiles are: {player_array}\n")
        player_input(dice_sum)
        print(f"Your left-over tiles are: {player_array}\n")

        print("Python is rolling the dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"Python rolled {dice_one} and a {dice_two}")

        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        print(f"Pythons tiles are: {player_array}\n")
        computer_tiles_iii(dice_sum)
        print(f"Pythons left-over tiles are: {computer_array}\n")

        input("Please press any key to continue.\n")
        if player_array == empty or computer_array == empty:
            break
        i += 1

    print("Game completed.\n")
    score(name)


def score(name):
    """
    Calculating the score and determining the winner of the match
    """
    player_score = 0
    computer_score = 0

    player_score = player_score + sum(player_array)
    computer_score = computer_score + sum(computer_array)

    print(f"You got: {player_score} points!")
    print(f"Python got: {computer_score} points!\n")

    if player_score > computer_score:
        print("Python has less points.")
        print("Python wins!")
    else:
        print(f"{name} has less points.")
        print(f"{name} wins!")


def main():
    """
    This is the main function.
    """
    print("Welcome to the 'Shut the box'- Game")

    name = input("Please enter your name: ")
    print(f"Hello {name}.")
    print("Would you like to start a new game or read the game rules?")

    start(name)

# Here we call up the game:


player_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
computer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
main()
