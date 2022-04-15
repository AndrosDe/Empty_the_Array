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

The remaining value entries in the array will be added together.
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
    # these variables are used to divorce the text for the program structure.
    # Input requests to prevent the whole text from being shown at once.
    print(rule_part_one)
    input("Please press 'Enter' to continue.\n")

    print(rule_part_two)
    input("Please press 'Enter' to continue.\n")

    print(rule_part_three)
    input("Please press 'Enter' to continue.\n")

    print(rule_part_four)


def dice_roll():
    """
    This function will create a random number between 1 and 6.
    Just like a dice with six sides would do.
    """
    dice = random.randrange(1, 6)
    return dice


def ai_close_one_tile(dice_sum):
    """
    Closing one tile taking dice_sum
    """
    # The remove-function was used as it targets "values" and not "index".
    COMPUTER_ARRAY.remove(dice_sum)


def ai_close_two_tiles(i, j):
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


def ai_close_three_tiles(i, j, dice_sum):
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
    if dice_sum >= 8:
        try:
            ai_close_three_tiles(one, two, dice_sum)
        except ValueError:
            try:
                ai_close_three_tiles(one, three, dice_sum)
            except ValueError:
                try:
                    ai_close_three_tiles(one, four, dice_sum)
                except ValueError:
                    try:
                        ai_close_three_tiles(one, five, dice_sum)
                    except ValueError:
                        try:
                            ai_close_three_tiles(two, three, dice_sum)
                        except ValueError:
                            try:
                                ai_close_three_tiles(two, four, dice_sum)
                            except ValueError:
                                try:
                                    ai_close_three_tiles(three, four, dice_sum)
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
        ai_close_two_tiles(one, one_less)
    except ValueError:
        try:
            ai_close_two_tiles(two, two_less)
        except ValueError:
            try:
                ai_close_two_tiles(three, three_less)
            except ValueError:
                try:
                    ai_close_two_tiles(four, four_less)
                except ValueError:
                    try:
                        ai_close_two_tiles(five, five_less)
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
        ai_close_one_tile(dice_sum)
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
    while True:
        print(" ")
        print(f"The sum of the dices is: {dice_sum}\n")
        print(f"Your tiles are: {PLAYER_ARRAY}\n")
        print("Which tile(s) do you want to close in this round?\n")
        print("If you want to pass this round, please enter:")
        print(" pass, none or just press 'Enter'.\n")
        print("Please enter your choice like this:")

        tile_input = input("'8' or '7, 1' or '5, 2, 1' or 'none'\n")
        # Creating a list with string values from the input.
        tile_array_str = tile_input.split(",")

        # Validating the content of the input
        # Except of the exceptions below only numbers are valid
        if val_input_as_pass(tile_input):
            if val_input_as_num(tile_array_str):
                tile_array_int = [int(a) for a in tile_array_str]
                if val_input_equal_dice(tile_array_int, dice_sum):
                    if val_input_lenght(tile_array_int):
                        if val_input_same_num(tile_array_int):
                            if val_input_tile_available(tile_array_int):
                                player_closing_tiles(tile_array_int)
                                break

        else:
            print("None! No tiles to close, ending your turn.\n")
            break


def val_input_as_pass(a):
    """
    Validate if the player wants to pass this round.
    """
    if a != "none":
        if a != 'None':
            if a != 'pass':
                if a != 'Pass':
                    if a != "":
                        return True


def val_input_as_num(a):
    """
    Validate if numbers (int) have been entered.
    """
    try:
        [int(i) for i in a]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def val_input_equal_dice(a, b):
    """
    Validating if the value of the dice and the numbers chosen are equal.
    """
    x = "The value of the tile(s) must match the combined value of both dices."
    if sum(a) != b:
        print(x)
        return False
    else:
        return True


def val_input_lenght(a):
    """
    Validating if one, two, or three numbers have been entered.
    """
    if len(a) > 3:
        print("Only one, two or three tiles can be closed at a time.")
        print(f"You provided {len(a)} numbers.")
        return False
    else:
        return True


def val_input_same_num(a):
    """
    Validating if the numbers are different, you can use a number only once.
    """
    if len(a) == 1:
        return True
    elif len(a) == 2:
        b = val_input_same_two_num(a)
        if b is False:
            return False
        else:
            return True
    elif len(a) == 3:
        b = val_input_same_three_num(a)
        if b is False:
            return False
        else:
            return True


def val_input_same_two_num(a):
    """
    Validating if a set of two numbers are different,
    you can use a number only once.
    """
    if a[0] == a[1]:
        print("Invalid numbers, please choose different numbers.")
        return False
    else:
        return True


def val_input_same_three_num(a):
    """
    Validating if a set of three numbers are different,
    you can use a number only once.
    """
    if a[0] == a[1]:
        print("Invalid numbers, please choose different numbers.")
        return False
    elif a[1] == a[2]:
        print("Invalid numbers, please choose different numbers.")
        return False
    elif a[0] == a[2]:
        print("Invalid numbers, please choose different numbers.")
        return False
    else:
        return True


def val_input_tile_available(a):
    """
    Validating if the numbers chosen are still in the array.
    """
    if len(a) == 1:
        b = val_input_one_tile_available(a)
        if b is False:
            return False
        else:
            return True
    elif len(a) == 2:
        b = val_input_two_tile_available(a)
        if b is False:
            return False
        else:
            return True
    elif len(a) == 3:
        b = val_input_three_tile_available(a)
        if b is False:
            return False
        else:
            return True


def val_input_one_tile_available(a):
    """
    Validate if the one number chosen is still in the array.
    """
    if a[0] in PLAYER_ARRAY:
        return True
    else:
        print(f"Tile {a[0]} was already closed.")
        print("Another tile must be selected.")
        return False


def val_input_two_tile_available(a):
    """
    Validate if the two numbers chosen are still in the array.
    """
    if a[0] in PLAYER_ARRAY:
        if a[1] in PLAYER_ARRAY:
            return True
        else:
            print(f"Tile {a[1]} was already closed and you must close both.")
            print("Another tile must be selected.")
            return False
    else:
        print(f"Tile {a[0]} was already closed and you must close both.")
        print("Another tile must be selected.")
        return False


def val_input_three_tile_available(a):
    """
    Validate if the three numbers chosen are still in the array.
    """
    if a[0] in PLAYER_ARRAY:
        if a[1] in PLAYER_ARRAY:
            if a[2] in PLAYER_ARRAY:
                return True
            else:
                print(f"Tile {a[2]} was already closed, you must close all.")
                print("Another tile must be selected.")
                return False
        else:
            print(f"Tile {a[1]} was already closed, you must close all.")
            print("Another tile must be selected.")
            return False
    else:
        print(f"Tile {a[0]} was already closed,you must close all.")
        print("Another tile must be selected.")
        return False


def player_closing_tiles(a):
    """
    Review the result of the input for length.
    """
    if len(a) == 1:
        b = player_colsing_one_tile(a)
        if b is False:
            return False
        else:
            return True
    elif len(a) == 2:
        b = player_colsing_two_tiles(a)
        if b is False:
            return False
        else:
            return True
    elif len(a) == 3:
        b = player_colsing_three_tiles(a)
        if b is False:
            return False
        else:
            return True
    else:
        print("Odd, this should have been validated to only have 3 numbers.")
        print("Please, contact the developer.")
        return False


def player_colsing_one_tile(a):
    """
    Remove the number from the array.
    """
    PLAYER_ARRAY.remove(a[0])
    print(f"Closing tile {a[0]}.")
    return True


def player_colsing_two_tiles(a):
    """
    Remove the two numbers from the array.
    """
    PLAYER_ARRAY.remove(a[0])
    PLAYER_ARRAY.remove(a[1])
    print(f"Closing tiles {a[0]} and {a[1]}.")
    return True


def player_colsing_three_tiles(a):
    """
    Remove the three numbers from the array.
    """
    PLAYER_ARRAY.remove(a[0])
    PLAYER_ARRAY.remove(a[1])
    PLAYER_ARRAY.remove(a[2])
    print(f"Closing tiles {a[0]}, {a[1]} and {a[2]}.")
    return True


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
        print("We have a draw!")
        print(f"Python and {name} have the same amount of points.\n")
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

        # Asking for player input.
        player_input(dice_sum)

        print(f"Your left-over tiles are: {PLAYER_ARRAY}\n")
        input("Please press 'Enter' to continue.\n")

        # It is the computers turn.
        # Rolling the dices for the computer.
        print(" ")
        print("***** Python's turn *****\n")
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
        input("Please press 'Enter' to continue.\n")

        if PLAYER_ARRAY == empty or COMPUTER_ARRAY == empty:
            break  # When one of the arrays is empty the codes stops running.
        i += 1

    # Showing that the code stopped running.
    print("Game completed.\n")
    # Calculating the score.
    score(name)

    # Goodbye message at the end of the game.
    print("\n ***** Thank you for playing 'Empty the Array' *****\n")
    print("  ___   ___   ___   ___   ___   ___   ___   ___   ___ ")
    print(" |___| |___| |___| |___| |___| |___| |___| |___| |___|\n\n")
    print("               .-------.          ______ ")
    print("              /   o   /|         /\     \ ")
    print("             /_______/o|        /o \  o  \ ")
    print("             | o     | |       /   o\_____\ ")
    print("             |   o   |o/       \o   /o    / ")
    print("             |     o |/         \ o/  o  / ")
    print("             '-------'           \/____o/ \n\n")


def intro():
    """
    The intro function to the game, where the player can enter the name.
    """
    # Welcome Message.
    print("******* Welcome to the 'Empty the Array'- Game *******\n")
    print("  ___   ___   ___   ___   ___   ___   ___   ___   ___ ")
    print(" |   | |   | |   | |   | |   | |   | |   | |   | |   |")
    print(" | 1 | | 2 | | 3 | | 4 | | 5 | | 6 | | 7 | | 8 | | 9 |")
    print(" |___| |___| |___| |___| |___| |___| |___| |___| |___|\n\n")
    print("               .-------.          ______ ")
    print("              /   o   /|         /\     \ ")
    print("             /_______/o|        /o \  o  \ ")
    print("             | o     | |       /   o\_____\ ")
    print("             |   o   |o/       \o   /o    / ")
    print("             |     o |/         \ o/  o  / ")
    print("             '-------'           \/____o/ \n\n")
    # Input request for the name.
    # No validations are made here, as the player is free to choose
    # whatever name they want in this game.
    name = input("Please enter your name: ")

    print(f"\nHello {name}.")
    start(name)


# Here we call up the game, with the intro function,
# the main function will be called up a bit later,
# This way the player's name only needs to be entered once
# and can start the match after reading the rules,
# without starting the whole program again.

intro()
