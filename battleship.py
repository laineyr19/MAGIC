from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    print "* * * * *"
    for row in board:
        print " ".join(row)
    print "* * * * *"

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
    print "Turn", turn + 1
    guess_row = raw_input("Guess Row:")
    guess_col = raw_input("Guess Col:")
    if guess_row == "" or guess_col == "":
        print "Not a valid guess."
        print_board(board)
        continue
    else:
        guess_row = int(guess_row)
        guess_col = int(guess_col)

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            
        elif guess_row == ship_row or \
        guess_col == ship_col:
            if guess_row == ship_row:
                print "You got the row correct."
            if guess_col == ship_col:
                print "you got the column right."
            board[guess_row][guess_col] = "X"
            print_board(board)
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
        
        if turn == 3:
            print "Game Over"
            print "The correct row was " + \
            str(ship_row) + \
            " and the correct column was " + \
            str(ship_col)
        
