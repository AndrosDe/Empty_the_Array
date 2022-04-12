# WELLCOME TO THE "EMPTY THE ARRAY" GAME.
# THis is a coded variant of the dice game "Shut the box"
# Shut the box (also called Canoga, batten down the hatches, or trick-track)
# is a game of dice for one or more players.
# Traditionally, a counting box is used with tiles numbered 1 to 9.
# More information on the game here:
# https://en.wikipedia.org/wiki/Shut_the_box

# Modules:
""" The random module will be used for the dice roll. """
import random

# Gobal Variables
# These variables will be used by different functions in the game.
# The Values in the arrays will be validated, removed, and, in the end,
# added together by these functions.
PLAYER_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9]
COMPUTER_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game_rules():
    """
    Here the player gets a printout on how to play the game.
    """
    # The rules are split into 4 parts to prevent a "wall-of-text"-issue.
    rule_part_one = '''
How the game is played:

At the start of the game, you will start with a full array from 1 to 9.
During the game, each player plays in turn for nine rounds
or until an array is empty.

The remaining value entries in the array, are then added together.
The player with the lowest sum will win the match.

'''
    rule_part_two = '''
A round will playout like this:
The player begins their turn by rolling the die or dice.
After throwing, the player adds up (or subtracts) the dice and then removes one
of any combination of numbers that sum to the total number of the dices,
if all of these numbers are still available.

'''
    rule_part_three = '''
For example, if the total number is "8" the player may choose any of the
following sets of numbers (if all of the numbers are available in the array):
    - 8
    - 7, 1
    - 6, 2
    - 5, 3
    - 5, 2, 1
    - 4, 3, 1

Then the next player's turn comes and chooses a set of tiles to close.
If the dice yield no number(s) to close (all) tile(s),
then the player must "pass".

'''

    rule_part_four = '''
Calculating Score:
At the end of the 9th round or when one of the players has an empty array,
the player scores the sum of the remaining numbers in the array.
For example, if the numbers 2, 3, and 5 are still open the player's score is
10 (2 + 3 + 5 = 10).

'''
    # To make the actual code more readable,
    # these variables were used to divorce the text for the program structure.
    # Input requests to prevent the whole text from being shown at once.
    print(rule_part_one)
    input("Please press any key to continue.\n")

    print(rule_part_two)
    input("Please press any key to continue.\n")

    print(rule_part_three)
    input("Please press any key to continue.\n")

    print(rule_part_four)


def dice_roll():
    """
    This function will create a random number between 1 and 6.
    Just like a dice with six sides would do.
    """
    dice = random.randrange(1, 6)
    return dice


def closing_one_tile(dice_sum):
    """
    Closing one tile taking dice_sum
    """
    # The remove-function was used as it targets "values" and not "index".
    COMPUTER_ARRAY.remove(dice_sum)


def closing_two_tiles(i, j):
    """
    Closing two tiles, according to the parameters.
    """
    # The remove-function was used as it targets "values" and not "index".
    # The validation checks if both numbers are in the array.
    if i in COMPUTER_ARRAY:
        if j in COMPUTER_ARRAY:
            COMPUTER_ARRAY.remove(i)
            COMPUTER_ARRAY.remove(j)
            print(f"So Python can close... {i} and {j}.")
        else:
            raise ValueError
    else:
        raise ValueError


def closing_three_tiles(i, j, dice_sum):
    """
    Closing two tiles, according to the parameters.
    """
    # The remove-function was used as it targets "values" and not "index".
    # Third number must be the left over of the other two numbers and dice_sum.
    k = dice_sum - (i + j)
    # The validation checks if all numbers are in the array.
    if i in COMPUTER_ARRAY:
        if j in COMPUTER_ARRAY:
            if k in COMPUTER_ARRAY:
                COMPUTER_ARRAY.remove(i)
                COMPUTER_ARRAY.remove(j)
                COMPUTER_ARRAY.remove(k)
                print(f"So Python can close... {i}, {j} and {k}.")
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


def ai_valadation_three_tiles_combi(dice_sum):
    """
    Close the three appropriate tiles if they are open.
    """
    # Defining the variables that will be the parameters
    # for the closing tile functions.
    one = dice_sum - (dice_sum - 1)  # One
    two = dice_sum - (dice_sum - 2)  # Two
    three = dice_sum - (dice_sum - 3)  # Three
    four = dice_sum - (dice_sum - 4)  # Four
    five = dice_sum - (dice_sum - 5)  # Five

    # If the sum is greater than 6 because 6 is the first
    # number that can be split into 3 different numbers,
    # the program will "try and error" several combinations.
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
                                    ai_valadation_two_tiles_combi(dice_sum)
    else:
        ai_valadation_two_tiles_combi(dice_sum)


def ai_valadation_two_tiles_combi(dice_sum):
    """
    Close the two appropriate tiles if they are open.
    """
    # Defining the variables that will be the parameters
    # for the closing tile functions.
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

    # This is started after all three tiles combinations are exhausted.
    # Now the program will "try and error" several combinations
    # for closing two tiles at once.
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
                        ai_valadation_one_tile_combi(dice_sum)


def ai_valadation_one_tile_combi(dice_sum):
    """
    Close the one appropriate tiles if it is open.
    """
    value_dice = "So Python can close... "
    # Once all combinations for closing three and two tile are exhausted,
    # The program will the try to close one tile.
    try:
        closing_one_tile(dice_sum)
        print(value_dice + f" {dice_sum}.")
    # However if that tile is closed, no tiles will be closed this round.
    except ValueError:
        print(value_dice)
        print("Nothing! No tiles to close, ending the Pythons turn.")


def player_input(dice_sum):
    """
    Here we ask the player how many tiles should be closed in this round.
    Should an invalid entry be made, then the player will be asked again.
    """
    # Welcome message to the player input function of the game.
    print(" ")
    print(f"Your tiles are: {PLAYER_ARRAY}\n")
    print("How many tiles do you want to close in this round?\n")
    value_player = ""
    print(f"value_player: {value_player}\n")
    value_player = input("Please enter one, two, three or none to continue: ")

    # Validating the player's input, as only one of 4 choices can be made.
    # A quit option to end the game here could be added as well.
    if value_player == "none":
        print("None! No tiles to close, ending your turn.")
    elif value_player == "one":
        print(f"value_player: {value_player}\n")
        player_input_one(dice_sum)
    elif value_player == "two":
        print(f"value_player: {value_player}\n")
        player_input_two(dice_sum)
    elif value_player == "three":
        print(f"value_player: {value_player}\n")
        player_input_three(dice_sum)
    else:
        print(f"value_player: {value_player}\n")
        print("Invalid input, you need to select:")
        print("'none','one','two' or 'three' to continue.")
        player_input(dice_sum)


def player_input_length(dice_sum):
    """
    If an error by the length validation of the input appears,
    then these messages will be displayed and the "player_input()" is calles.
    """
    print("Do you want to close a different amount of tiles?\n")
    print(f"The sum of the dices is: {dice_sum}\n")
    player_input(dice_sum)


def player_input_one(dice_sum):
    """
    Here we ask the player for the tile to close in this round.
    It will check if the input matches the sum of bot dices
    and if the tiles are still open in the array.
    An invalid entry will repeat the previous input request.
    If all is well, the tile will be closed.
    """
    # Welcome Message (with input request) for closing one tile.
    one_tile_choosen = ""
    one_tile_choosen = input("Please enter the tile to close:\n")
    print(f"tile_choosen: {one_tile_choosen}\n")
    tile_set_one = int(one_tile_choosen)
    print(f"tile_choosen: {tile_set_one}\n")

    # Validating the input:
    # Validating if numbers (int) have been entered.
    try:
        tile = [int(tile_set_one)]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    # Validating if exsactly one number was entered.
    tile = [int(tile_set_one)]
    if len(tile) != 1:
        print(f"One number is needed, you provided {len(tile_set_one)}")
        player_input_length(dice_sum)

    # Validating if the number chosen is equal to the added value of two dice.
    if tile_set_one == dice_sum:
        # Validating if the number chosen is still in the array.
        if tile_set_one in PLAYER_ARRAY:
            # Now the value will be removed from the array.
            PLAYER_ARRAY.remove(tile_set_one)
            print(f"Closing tile {tile_set_one}.")
        else:
            print("This tile was already closed.")
            print("Another tile must be selected.")
            player_input(dice_sum)
    else:
        print("If you only want to close 'one' tile,")
        print("than the value must match the value of both dices.")
        print("Do you want to close a different amount of tiles?\n")
        player_input(dice_sum)


def player_input_two(dice_sum):
    """
    Here we ask the player for two tiles to close in this round.
    It will check if the sum of the input matches
    the sum of bot dices and if the tiles are still open in the array.
    An invalid entry will repeat the previous input request.
    If all is well, the tile will be closed.
    """
    # Welcome Message (with input request) for closing two tiles.
    print("Please enter the two tile to close.")
    two_tile_choosen = ""
    two_tile_choosen = input("For example: 7, 1\n")
    print(f"tile_choosen: {two_tile_choosen}\n")
    tile_set_two = two_tile_choosen.split(",")
    print(f"tile_choosen: {tile_set_two}\n")

    # Validating the input:
    try:
        # Validating if numbers (int) have been entered.
        [int(tile) for tile in tile_set_two]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    # After making sure that all entries are number, we make a list.
    tile_list = []
    print(f"tile_choosen: {tile_list}\n")
    tile_list = [int(tile) for tile in tile_set_two]
    print(f"tile_choosen: {tile_list}\n")

    # Validating if exsactly two numbers were entered.
    if len(tile_list) != 2:
        print(f"Two numbers are needed, you provided {len(tile_list)}")
        player_input_length(dice_sum)

    # Validating if the numbers are different, you can use a number only once.
    if tile_list[0] == tile_list[1]:
        print("Invalid numbers, please choose different numbers.")
        player_input_two(dice_sum)

    # Validating if value of the dices and the numbers chosen are equal.
    if sum(tile_list) == dice_sum:
        i = tile_list[0]
        j = tile_list[1]
        # Validating if the numbers chosen are still in the array.
        if i in PLAYER_ARRAY:
            if j in PLAYER_ARRAY:
                # Now the two numbers will be removed from the array.
                PLAYER_ARRAY.remove(i)
                PLAYER_ARRAY.remove(j)
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
        print("Do you want to close a different amount of tiles?\n")
        player_input(dice_sum)


def player_input_three(dice_sum):
    """
    Here we ask the player for three tiles to close in this round.
    It will check if the sum input matches the sum of bot dices
    and if the tiles are still open in the array.
    An invalid entry will repeat the previous input request.
    If all is well, the tile will be closed.
    """
    # Welcome Message (with input request) for closing three tiles.
    print("Please enter the three tiles to close.")
    three_tile_choosen = ""
    print(f"tile_choosen: {three_tile_choosen}\n")
    three_tile_choosen = input("For example: 5, 2, 1\n")
    print(f"tile_choosen: {three_tile_choosen}\n")
    tile_set_three = three_tile_choosen.split(",")
    print(f"tile_choosen: {tile_set_three}\n")

    # Validating the input:
    try:
        # Validating if numbers (int) have been entered.
        [int(tile) for tile in tile_set_three]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        player_input(dice_sum)

    tile_list = []
    print(f"tile_choosen: {tile_list}\n")
    tile_list = [int(tile) for tile in tile_set_three]
    print(f"tile_choosen: {tile_list}\n")

    # Validating if exsactly three numbers were entered.
    if len(tile_list) != 3:
        print(f"Three numbers are needed, you provided {len(tile_list)}")
        player_input_length(dice_sum)

    # Validating if the numbers are different, you can use a number only once.
    if tile_list[0] == tile_list[1]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)
    elif tile_list[1] == tile_list[2]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)
    elif tile_list[0] == tile_list[2]:
        print("Invalid numbers, please choose different numbers.")
        player_input_three(dice_sum)

    tile_closed = "This tile was already closed and you must close all tiles."
    # Validating if value of the dices and the numbers chosen are equal.
    if sum(tile_list) == dice_sum:
        i = tile_list[0]
        j = tile_list[1]
        k = tile_list[2]
        # Validating if the numbers chosen are still in the array.
        if i in PLAYER_ARRAY:
            if j in PLAYER_ARRAY:
                if k in PLAYER_ARRAY:
                    # Now the three numbers will be removed from the array.
                    PLAYER_ARRAY.remove(i)
                    PLAYER_ARRAY.remove(j)
                    PLAYER_ARRAY.remove(k)
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
        print("Do you want to close a different amount of tiles?\n")
        player_input(dice_sum)


def start(name):
    """
    The start-up function,
    where a player can read the rules or start up the game.
    """
    # Welcome Message of the "Start Game or Rules" function.
    print("Would you like to start a new game or read the game rules?")
    # Asking for the input of the player's choice.
    # Only two valid choices so far, a "quit" option could be added later
    start_or_rules = input("""Please enter:
    - 'game' to start a game
    - 'rules' to read the rules
    """)
    # Validating the players choice.
    if start_or_rules == 'rules':
        game_rules()
        start(name)
    elif start_or_rules == 'game':
        main_game(name)
    # If an invalid input was made, the function starts over again.
    else:
        print("Invalid entry, please enter:")
        print("'game' to start a game")
        print("'rules' to read the rules:\n")
        start(name)


def score(name):
    """
    Calculating the score and determining the winner of the match
    """
    player_score = 0
    computer_score = 0

    # Calculating the score, which could also be just:
    # player_score = sum(PLAYER_ARRAY)
    # However, shoud this game be extended and "new match" option impemented,
    # this function will not require any modification.
    player_score = player_score + sum(PLAYER_ARRAY)
    computer_score = computer_score + sum(COMPUTER_ARRAY)

    print(f"You got: {player_score} points!")
    print(f"Python got: {computer_score} points!\n")

    # Comparing the scores to determine the match-winner.
    # In "Empty the Array" the player with the least points wins.
    if player_score > computer_score:
        print("Python has fewer points.")
        print("Python wins!\n")
    elif player_score == computer_score:
        print("We have a draw!\n")
        print(f"Python and {name} have the same amount of points.")
    else:
        print(f"{name} has fewer points.")
        print(f"{name} wins!\n")


def main_game(name):
    """
    The main function of the game:
    It defines a game round:
    1. The players turn:
    -> rolling the dice
    -> input of the tiles to close
    -> closing the tiles
    2. The computers turn:
    -> rolling the dice
    -> closing the tiles

    The game ends after nine rounds or until one of the arrays is empty.

    After that, it will call up the score-function
    to determine the winner of the match.
    """
    i = 1
    empty = []

    while i <= 9:  # Run this code nine times.
        print(" ")
        print(f"***** Round {i} ******\n")  # To show that a new round started.

        # Rolling the dices.
        print("You are rolling your dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"{name} rolled {dice_one} and a {dice_two}")

        # Adding the value of the dices together.all(iterable)
        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        # Reminding the player which tiles are open.

        # Asking for player input.
        player_input(dice_sum)
        print(f"Your left-over tiles are: {PLAYER_ARRAY}\n")
        input("Please press any key to continue.\n")

        # It is the computers turn.
        # Rolling the dices for the computer.
        print("Python is rolling the dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"Python rolled {dice_one} and a {dice_two}")

        # Adding the value of the dices together.
        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        print(f"Pythons tiles are: {COMPUTER_ARRAY}\n")

        # Starting "try and error" - functions
        # to see what the computer can close.
        # It's rather "agressive" and will start
        # to close as much tiles first as possible,
        # which is not always the best staregy.
        ai_valadation_three_tiles_combi(dice_sum)
        print(f"Pythons left-over tiles are: {COMPUTER_ARRAY}\n")
        input("Please press any key to continue.\n")

        if PLAYER_ARRAY == empty or COMPUTER_ARRAY == empty:
            break  # When one of the arrays is empty the codes stops running.
        i += 1

    # Showing that the code stopped running.
    print("Game completed.\n")
    # Calculating the score.
    score(name)

    # Goodbye message at the end of the game.
    print("***** Thank you for playing 'Empty the Array' *****")


def intro():
    """
    The intro function to the game, where the player can enter the name.
    """
    # Welcome Message.
    print("Welcome to the 'Empty the Array'- Game")

    # Input request for the name.
    # No validations are made here, as the player is free to choose
    # whatever name is to be used in this game.
    name = input("Please enter your name: ")

    print(f"\nHello {name}.")
    start(name)


# Here we call up the game, with the intro function,
# the main function will be called up a bit later,
# This way the player name only needs to be entered once
# and can start the match after reading the rules,
# without starting the whole program again.
intro()
