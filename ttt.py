# Tic Tac Toe AI and game player.
import random
import time
# symbolDict will be set based on whether the player chooses X or O
symbolDict = {}
# Score counters
aiScore = 0
playerScore = 0
drawScore = 0
totalGames = 0


def drawBoard(c):
    """
    Given a configuration of a board draws it
        Input:
            config -> List of integers
            0 = Empty Space
            1 = "X"
            2 = "O"
        Output:
            void. Prints board to the console
    """

    print ""
    print "-------------"  # Top Border
    for i in range(3):  # for each row
        n = i*3
        print "| {} | {} | {} |".format(
            symbolDict[c[n]], symbolDict[c[n+1]], symbolDict[c[n+2]])
        print "-------------"
    print ""


def gameIsFinished(c):
    """
    Given a board configuration, returns whether the game is over.
    If the game is over, returns True if agent wins, false otherwise
        In  : config -> board configuration
        Out : (bool, bool)
            0th element -> Is the game finished
            1st element -> Is the agent the winner, T/F, or None if draw
    """

    # Check rows and columns
    for i in range(3):

        rowsum = sum(c[i*3:i*3+3])
        if abs(rowsum) == 3:
            if rowsum > 0:
                return (True, True)  # Game is over, agent wins
            else:
                return (True, False)  # Game is over, player wins

        colsum = sum(c[i::3])
        if abs(colsum) == 3:
            if colsum > 0:
                return (True, True)  # Game is over, agent wins
            else:
                return (True, False)  # Game is over, player wins
            return True

    # Check diagonals
    diag1 = sum(c[0::4])
    diag2 = sum(c[2:7:2])
    if abs(diag1) == 3:
        if diag1 > 0:
            return (True, True)  # Game is over, agent wins
        else:
            return (True, False)  # Game is over, player wins
    if abs(diag2) == 3:
        if diag2 > 0:
            return (True, True)  # Game is over, agent wins
        else:
            return (True, False)  # Game is over, player wins

    # Check for a draw - i.e., all spces occupied
    if sum([abs(i) for i in c]) == 9:  # then every space is occupied
        return (True, None)

    return (False, False)  # Game is not finished


def scoreForState(c):
    """
    Given a configuration of a board, returns the score.
    The score is 10 for an agent win, -10 for a player win, 0 for a draw
    None is returned if the game is not over
    """

    gameFin = gameIsFinished(c)
    if gameFin[0]:  # Game is over
        if gameFin[1]:  # Agent wins
            return 10
        elif gameFin[1] is False:
            return -10  # Player wins
        else:
            return 0  # Draw
    else:  # Game is not over
        return None  # No score, because game is continuing


def boardIsValid(c):
    """
    Is the board a valid configuration?
    The number of occurrences of Xs and Os must not differ by more than 1
    """

    return abs(c.count(1) - c.count(-1)) <= 1


def generateValidNextState(c):
    """
    Given a configuration, generates all valid next configurations of the board
        Input: Board configuration -> List of integers
        Output: List of Board configurations -> List of List of Integers
    """

    validNextStates = []
    for i, e in enumerate(c):
        if e == 0:
            d = list(c)  # clone c
            d[i] = 1  # Replace the empty space
            validNextStates.append(d)  # Add it to the list of valid configs
    return validNextStates


def getValidMovesFor(c):
    """
    Given a configuration, returns all valid next moves.
        Input: Board configuration -> List of integers
        Output: List of valid positions to place a piece
    """

    validNextMoves = []
    for i, e in enumerate(c):
        if e == 0:
            validNextMoves.append(i+1)
    return validNextMoves


def playGame():
    """
    Plays the game from picking a piece to playing the game to updating score
    """
    global totalGames, aiScore, playerScore, drawScore, symbolDict
    # Print stats
    print "STATS:", totalGames, "total games"
    print "AI   :", aiScore
    print "You  :", playerScore
    print "Draw :", drawScore
    print ""

    # Get an input from the player
    valid = False
    while not valid:
        playerChar = raw_input("Play X or O? ")  # Ask user to pick play
        if not playerChar.upper() in ["X", "O"]:
            if playerChar.lower() == "exit":
                exit()
            print "Input is invalid, please pick X or O"
        else:
            playerChar = playerChar.upper()  # Convert to upper
            if playerChar == "X":  # Player wants to play X
                symbolDict = {0: " ", 1: "O", -1: "X"}
            elif playerChar == "O":  # Player wants to play O
                symbolDict = {0: " ", 1: "X", -1: "O"}
            valid = True
    print "You have chosen to play", playerChar, "\n"

    # Pick who goes first
    print "Picking who goes first..."
    if round(random.random()) > 0:
        print "Agent goes first"
        agentsMove = True
    else:
        print "You go first"
        agentsMove = False

    # Play the game
    gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while not gameIsFinished(gameBoard)[0]:

        if agentsMove:  # Agent's move
            # The agent's move
            print "Agent Moving"
            # PALCEHOLDER - PICK A RANDOM MOVE
            gameBoard[random.choice(getValidMovesFor(gameBoard))-1] = 1
            agentsMove = not agentsMove  # Alternate move

        else:  # Player's move
            validPlayerMoves = getValidMovesFor(gameBoard)

            # Get a valid move from the player
            enteredValidMove = False
            while not enteredValidMove:
                print "Your Move. Valid moves are", validPlayerMoves
                position = input("Move? ")
                if not position in validPlayerMoves:
                    print "Invalid move entered."
                else:
                    enteredValidMove = True
            gameBoard[position - 1] = -1  # Make the move for the player
            agentsMove = not agentsMove  # Alternate move

        drawBoard(gameBoard)  # Draw the board after every move

    # Game is over, evalute the result
    gameStatus = gameIsFinished(gameBoard)
    if gameStatus[1]:  # Agent wins
        print "AI wins in", str(9 - len(getValidMovesFor(gameBoard))), "moves"
        aiScore += 1
    elif gameStatus[1] is False:  # Player wins
        print "You won in", str(9 - len(getValidMovesFor(gameBoard))), "moves"
        playerScore += 1
    else:  # None... Draw
        print "DRAW"
        drawScore += 1
    totalGames += 1

"""MAIN LOOP"""
print "Tic Tac Toe\n"

while True:
    playGame()

# Test cases
# print gameIsFinished([0,0,0,0,0,0,0,0,0])
# print gameIsFinished([1,0,-1,0,-1,1,-1,1,0])
# print scoreForState([0,0,0,0,0,0,0,0,0])
# print scoreForState([1,0,-1,0,-1,1,-1,1,0])
# print boardIsValid([0,0,0,0,0,0,0,0,0])
# print boardIsValid([1,0,-1,0,-1,1,-1,1,0])
# print boardIsValid([1,1,1,1,1,1,1,1,1])
# x = generateValidNextState([1,0,-1,0,-1,1,-1,1,0])
# for config in x:
#     drawBoard(config)
