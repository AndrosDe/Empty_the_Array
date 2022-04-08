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

    value_dice = f"{dice_sum}, so Python can remove... "
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
        computer_array.remove(dice_sum)
        print(value_dice + f"a {dice_sum}.")

    def closing_two_tiles(i, j):
        """
        Closing two tiles, according to the parameters
        """
        computer_array.remove(i)
        computer_array.remove(j)
        print(value_dice + f"a {i} and a {j}.")

    def closing_three_tiles(i, j):
        """
        Closing three tiles, according to the parameters
        """
        k = dice_sum - (i + j)
        computer_array.remove(i)
        computer_array.remove(j)
        computer_array.remove(k)
        print(value_dice + f"a {i}, {j} and a {k}.")

    try:
        closing_one_tile(dice_sum)
    except ValueError:
        if one and one_less in computer_array:
            try:
                closing_two_tiles(one, one_less)
            except ValueError:
                print(value_dice + value_error)
        elif two and two_less in computer_array:
            try:
                closing_two_tiles(two, two_less)
            except ValueError:
                print(value_dice + value_error)
        elif three and three_less in computer_array:
            try:
                closing_two_tiles(three, three_less)
            except ValueError:
                print(value_dice + value_error)
        elif four and four_less in computer_array:
            try:
                closing_two_tiles(four, four_less)
            except ValueError:
                print(value_dice + value_error)
        elif five and five_less in computer_array:
            try:
                closing_two_tiles(five, five_less)
            except ValueError:
                print(value_dice + value_error)
        elif one and two and (dice_sum - (one + two)) in computer_array:
            try:
                closing_three_tiles(one, two)
            except ValueError:
                print(value_dice + value_error)
        elif one and three and (dice_sum - (one + three)) in computer_array:
            try:
                closing_three_tiles(one, three)
            except ValueError:
                print(value_dice + value_error)
        elif one and four and (dice_sum - (one + four)) in computer_array:
            try:
                closing_three_tiles(one, four)
            except ValueError:
                print(value_dice + value_error)
        elif one and five and (dice_sum - (one + five)) in computer_array:
            try:
                closing_three_tiles(one, five)
            except ValueError:
                print(value_dice + value_error)
        elif two and three and (dice_sum - (two + three)) in computer_array:
            try:
                closing_three_tiles(two, three)
            except ValueError:
                print(value_dice + value_error)
        elif two and four and (dice_sum - (two + four)) in computer_array:
            try:
                closing_three_tiles(two, four)
            except ValueError:
                print(value_dice + value_error)
        elif three and four and (dice_sum - (three + four)) in computer_array:
            try:
                closing_three_tiles(three, four)
            except ValueError:
                print(value_dice + value_error)
        else:
            print(value_dice + value_error)

    print(f"Pythons left-over tiles are: {computer_array}\n")


def player_tiles(dice_sum):
    """
    Closing the appropriate tiles if they are open.
    To "close" the tiles we use the remove() method
    to remove an element from the array.

    """
    # tile_choosen = input("Please choose the tiles to close:\n")

    value_dice = f"{dice_sum}, so you can remove... "
    value_error = "Nothing! No tiles to close, ending the your turn."

    if dice_sum == 2:
        # try to remove 2, if not possible remove 1
        try:
            player_array.remove(1)
            print(value_dice + "a 1.")
        except ValueError:
            try:
                player_array.remove(2)
                print(value_dice + "a 2.")
            except ValueError:
                print(value_dice + value_error)
    elif dice_sum == 3:
        # try to remove 3 or 2, 1
        try:
            player_array.remove(2)
            player_array.remove(1)
            print(value_dice + "a 2 and a 1.")
        except ValueError:
            try:
                player_array.remove(3)
                print(value_dice + "a 3")
            except ValueError:
                print(value_dice + value_error)
    elif dice_sum == 4:
        # try to remove 4 or 2 or 3,1
        try:
            player_array.remove(4)
            print(value_dice + "a 4.")
        except ValueError:
            try:
                player_array.remove(1)
                player_array.remove(3)
                print(value_dice + "3 and 1.")
            except ValueError:
                print(value_dice + value_error)
    elif dice_sum == 5:
        # try to remove 5 or 3, 2 or 4,1
        try:
            player_array.remove(5)
            print(value_dice + "a 5.")
        except ValueError:
            try:
                player_array.remove(1)
                player_array.remove(4)
                print(value_dice + "4 and 1.")
            except ValueError:
                try:
                    player_array.remove(2)
                    player_array.remove(3)
                    print(value_dice + "3 and 2.")
                except ValueError:
                    print(value_dice + value_error)
    elif dice_sum == 6:
        # try to remove 6 or 3 or 4, 2
        try:
            player_array.remove(6)
            print(value_dice + "a 6.")
        except ValueError:
            try:
                player_array.remove(3)
                print(value_dice + "a 3.")
            except ValueError:
                try:
                    player_array.remove(2)
                    player_array.remove(4)
                    print(value_dice + "4 and 2.")
                except ValueError:
                    print(value_dice + value_error)
    elif dice_sum == 7:
        # try to remove 7 or 6,1 or 5,2 or 4,3 or 3,2,1
        try:
            player_array.remove(7)
            print(value_dice + "a 7.")
        except ValueError:
            try:
                player_array.remove(6)
                player_array.remove(1)
                print(value_dice + "6 and 1.")
            except ValueError:
                try:
                    player_array.remove(5)
                    player_array.remove(2)
                    print(value_dice + "5 and 2.")
                except ValueError:
                    try:
                        player_array.remove(4)
                        player_array.remove(3)
                        print(value_dice + "4 and 3.")
                    except ValueError:
                        try:
                            player_array.remove(4)
                            player_array.remove(2)
                            player_array.remove(1)
                            print(value_dice + "4, 2 and 1.")
                        except ValueError:
                            print(value_dice + value_error)
    elif dice_sum == 8:
        # try to remove 8 or 7,1 or 6,2 or 5,3 or 5,2,1 or 4,3,1
        try:
            player_array.remove(8)
            print(value_dice + "a 8.")
        except ValueError:
            try:
                player_array.remove(7)
                player_array.remove(1)
                print(value_dice + "7 and 1.")
            except ValueError:
                try:
                    player_array.remove(6)
                    player_array.remove(2)
                    print(value_dice + "6 and 2.")
                except ValueError:
                    try:
                        player_array.remove(5)
                        player_array.remove(3)
                        print(value_dice + "5 and 3.")
                    except ValueError:
                        try:
                            player_array.remove(5)
                            player_array.remove(2)
                            player_array.remove(1)
                            print(value_dice + "5, 2 and 1.")
                        except ValueError:
                            try:
                                player_array.remove(4)
                                player_array.remove(3)
                                player_array.remove(1)
                                print(value_dice + "4, 3 and 1.")
                            except ValueError:
                                print(value_dice + value_error)
    elif dice_sum == 9:
        # try to remove 9 or 8,1 or 7,2 or 6,3 or 5,4 or 5,3,1 or 4,3,2
        try:
            player_array.remove(9)
            print(value_dice + "a 9.")
        except ValueError:
            try:
                player_array.remove(8)
                player_array.remove(1)
                print(value_dice + "8 and 1.")
            except ValueError:
                try:
                    player_array.remove(7)
                    player_array.remove(2)
                    print(value_dice + "7 and 2.")
                except ValueError:
                    try:
                        player_array.remove(6)
                        player_array.remove(3)
                        print(value_dice + "6 and 3.")
                    except ValueError:
                        try:
                            player_array.remove(5)
                            player_array.remove(4)
                            print(value_dice + "5 and 4.")
                        except ValueError:
                            try:
                                player_array.remove(5)
                                player_array.remove(3)
                                player_array.remove(1)
                                print(value_dice + "5, 3 and 1.")
                            except ValueError:
                                try:
                                    player_array.remove(4)
                                    player_array.remove(3)
                                    player_array.remove(2)
                                    print(value_dice + "4, 3 and 2.")
                                except ValueError:
                                    print(value_dice + value_error)
    elif dice_sum == 10:
        # try to remove 9,1 or 8,2 or 7,3 or 6,4 or 6,3,1 or 5,4,1, or 5,3,2
        try:
            player_array.remove(9)
            player_array.remove(1)
            print(value_dice + "9 and 1.")
        except ValueError:
            try:
                player_array.remove(8)
                player_array.remove(2)
                print(value_dice + "8 and 2.")
            except ValueError:
                try:
                    player_array.remove(7)
                    player_array.remove(3)
                    print(value_dice + "7 and 3.")
                except ValueError:
                    try:
                        computer_array.remove(6)
                        computer_array.remove(4)
                        print(value_dice + "6 and 4.")
                    except ValueError:
                        try:
                            player_array.remove(6)
                            player_array.remove(3)
                            player_array.remove(1)
                            print(value_dice + "6, 3 and 1.")
                        except ValueError:
                            try:
                                player_array.remove(5)
                                player_array.remove(4)
                                player_array.remove(1)
                                print(value_dice + "5, 4 and 1.")
                            except ValueError:
                                try:
                                    player_array.remove(5)
                                    player_array.remove(3)
                                    player_array.remove(2)
                                    print(value_dice + "5, 3 and 2.")
                                except ValueError:
                                    print(value_dice + value_error)
    elif dice_sum == 11:
        # try to remove 9,2 or 8,3 or 7,4 or 6,5
        # or 7,3,1 or 6,4,1 or 6,3,2 or 5,4,2
        try:
            player_array.remove(9)
            player_array.remove(2)
            print(value_dice + "9 and 2.")
        except ValueError:
            try:
                player_array.remove(8)
                player_array.remove(3)
                print(value_dice + "8 and 3.")
            except ValueError:
                try:
                    player_array.remove(7)
                    player_array.remove(4)
                    print(value_dice + "7 and 4.")
                except ValueError:
                    try:
                        player_array.remove(6)
                        player_array.remove(5)
                        print(value_dice + "6 and 5.")
                    except ValueError:
                        try:
                            player_array.remove(7)
                            player_array.remove(3)
                            player_array.remove(1)
                            print(value_dice + "7, 3 and 1.")
                        except ValueError:
                            try:
                                player_array.remove(6)
                                player_array.remove(4)
                                player_array.remove(1)
                                print(value_dice + "6, 4 and 1.")
                            except ValueError:
                                try:
                                    player_array.remove(6)
                                    player_array.remove(3)
                                    player_array.remove(2)
                                    print(value_dice + "6, 3 and 2.")
                                except ValueError:
                                    try:
                                        player_array.remove(5)
                                        player_array.remove(4)
                                        player_array.remove(2)
                                        print(value_dice + "5, 4 and 2.")
                                    except ValueError:
                                        print(value_dice + value_error)
    elif dice_sum == 12:
        # try to remove 9,3 or 9,2,1 or 8,4 or 8,3,1 or 7,5
        # or 7,4,1 or 7,3,2 or 6,4,2 or 6,5,1 or 5,4,3
        try:
            player_array.remove(9)
            player_array.remove(3)
            print(value_dice + "9 and 3.")
        except ValueError:
            try:
                player_array.remove(9)
                player_array.remove(2)
                player_array.remove(1)
                print(value_dice + "9, 2 and 1.")
            except ValueError:
                try:
                    player_array.remove(8)
                    player_array.remove(4)
                    print(value_dice + "8 and 4.")
                except ValueError:
                    try:
                        player_array.remove(8)
                        player_array.remove(3)
                        player_array.remove(1)
                        print(value_dice + "8, 3 and 1.")
                    except ValueError:
                        try:
                            player_array.remove(7)
                            player_array.remove(5)
                            print(value_dice + "7 and 5.")
                        except ValueError:
                            try:
                                player_array.remove(7)
                                player_array.remove(4)
                                player_array.remove(1)
                                print(value_dice + "7, 4 and 1.")
                            except ValueError:
                                try:
                                    player_array.remove(7)
                                    player_array.remove(3)
                                    player_array.remove(2)
                                    print(value_dice + "7, 3 and 2.")
                                except ValueError:
                                    try:
                                        player_array.remove(6)
                                        player_array.remove(4)
                                        player_array.remove(2)
                                        print(value_dice + "6, 4 and 2.")
                                    except ValueError:
                                        try:
                                            player_array.remove(6)
                                            player_array.remove(5)
                                            player_array.remove(1)
                                            print(value_dice + "6, 5 and 1.")
                                        except ValueError:
                                            try:
                                                player_array.remove(5)
                                                player_array.remove(4)
                                                player_array.remove(3)
                                                print(value_dice + "5, 4 and 3.")
                                            except ValueError:
                                                print(value_dice + value_error)

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
        player_tiles(dice_sum)

        print("Python is rolling the dice...\n")
        dice_one = dice_roll()
        dice_two = dice_roll()
        print(f"Python rolled {dice_one} and a {dice_two}")

        dice_sum = dice_one + dice_two
        print(f"The sum of the dices is: {dice_sum}\n")
        computer_tiles(dice_sum)

        input("Please press any key to continue.\n")
        if player_array == [] or computer_array == []:
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
