# This Python file is a very basic version of a battleship game!
# The user is prompted for guessing the row and column in as many
# guesses as they see fit for a 5 x 5 grid! This was mostly made in
# CodEcademy but I thought it would be cool to save my work

from random import randint

from pip._vendor.distlib.compat import raw_input

board = []
max_turns = int(raw_input("How many guesses would you like? :"))

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board_in):
    for row in board_in:
        print(" ".join(row))


print_board(board)


def random_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(max_turns + 1):
    # Checks if we have reached max numbers of guesses
    if turn == max_turns:
        print("Game Over")
        print("My ship was located at row = " + str(ship_row) + " and at column = " + str(ship_col))
        break
    # Prints what turn you are on every cycle
    print("Turn", turn + 1)
    # Prompts for user guesses
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    # If statements for comparing user inputs
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        # If out of range
        if guess_row not in range(5) or \
                guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        # If you are guessing a spot that is taken
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        # If you are guessing a spot that is not where the ship is located
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
