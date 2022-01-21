
def create_grid():
    # This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

# This function prints the board
def printNeat(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

# this function explains the rules and an intro for the program
def intro():
    print('welcome to tictactoe')
    print("Player 1 and player 2, represented by X and O, take turns")
    print("marking the spaces in a 3*3 grid. The player who succeeds in placing")
    print("three of their marks in a horizontal, vertical, or diagonal row wins")

# This function decides the players' symbols
def sym():
    player1 = input('player1 would you like to be X or O:')
    if player1 == 'X':
        player2 = 'O'
        print("player1 is X and player2 is O")
        return player1, player2
    else:
        player2 = 'X'
        print("player1 is O and player2 is X")
        return player1, player2


def isFull(board, symbol1, symbol2):
    count = 1
    winner = True
    # This function check if the board is full
    while count < 10 and winner == True:
        gameOn(board, symbol1, symbol2,count)
        printNeat(board)

        if count == 9:
            print("GAme Over")
            if winner == True:
                print("its a tie")
        winner = isWinner(board, symbol1, symbol2, count)
        count += 1
    # this function checks if theres a winner
    if winner == False:
        print("Game over")
        # This is function gives a report
        report(count, winner, symbol1, symbol2)





# This function checks if any winner is winning
def isWinner(board, symbol1, symbol2, count):
    # This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol1):
            winner = False
            print("Player " + symbol1 + ", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol2):
            winner = False
            print("Player " + symbol2 + ", you won!")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol1):
            winner = False
            print("Player " + symbol1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol2):
            winner = False
            print("Player " + symbol2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol1:
        winner = False
        print("Player " + symbol1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol2:
        winner = False
        print("Player " + symbol2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol1:
        winner = False
        print("Player " + symbol1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol2:
        winner = False
        print("Player " + symbol2 + ", you won!")

    return winner


# This function starts the game.
def gameOn(board, symbol1, symbol2, count):
    if count % 2 == 0:
        player = symbol1
    else:
        player = symbol2
    print("player " + player + " its your turn")
    row = int(input("please enter a row in the range of 1-2"))
    col = int(input("please enter a column in the range of 1-2"))
    while row > 2 or row < 0 or col > 2 or col < 0:
        outOfRange()
        row = int(input("please enter a row in the range of 1-2"))
        col = int(input("please enter a column in the range of 1-2"))
    while board[row][col] == symbol1 or board[row][col] == symbol2:
        filledAlready()
        row = int(input("please enter a row in the range of 1-2"))
        col = int(input("please enter a column in the range of 1-2"))
    if player == symbol1:
        board[row][col] = symbol1
    else:
        board[row][col] = symbol2
    return board


def filledAlready():
    print("this location already taken please try a diffrent one")


def outOfRange():
    print("out of range please try again")

def report(count, winner, symbol1, symbol2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner : Player " + symbol1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner : Player " + symbol2 + ".")
    else:
        print("There is a tie. ")

    restart()


# this function restars the game
def restart():
    print("would you like to restart?")
    input(print("Press enter to restart"))
    main()





def main():
    intro()
    board = create_grid()
    printNeat(board)
    symbol1, symbol2 = sym()
    isFull(board, symbol1, symbol2)  # The function that starts the game is also in here.


main()
