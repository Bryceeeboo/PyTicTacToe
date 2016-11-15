# symbolDict will be set based on whether the player chooses X or O
symbolDict = {0: " ", 1: "X", -1: "O"}


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

    print "-------------"  # Top Border
    for i in range(3):  # for each row
        n = i*3
        print "| {} | {} | {} |".format(
            symbolDict[c[n]], symbolDict[c[n+1]], symbolDict[c[n+2]])
        print "-------------"


def gameIsFinished(c):
    """
    Given a board configuration, returns whether the game is over.
    If the game is over, returns True if agent wins, false otherwise
        In  : config -> board configuration
        Out : (bool, bool)
            0th element -> Is the game finished
            1st element -> Is the agent the winner, T/F, or None if draw
    """

    drawBoard(c)
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
    if abs(sum(c)) == 9:  # then every space is occupied
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
    for i, e in enumerate(c):  # Clone c
        if e == 0:
            d = list(c)
            d[i] = 1  # Replace the empty space
            validNextStates.append(d)  # Add it to the list of valid configs
    return validNextStates


# Test cases
print gameIsFinished([0,0,0,0,0,0,0,0,0])
print gameIsFinished([1,0,-1,0,-1,1,-1,1,0])
print scoreForState([0,0,0,0,0,0,0,0,0])
print scoreForState([1,0,-1,0,-1,1,-1,1,0])
print boardIsValid([0,0,0,0,0,0,0,0,0])
print boardIsValid([1,0,-1,0,-1,1,-1,1,0])
x = generateValidNextState([1,0,-1,0,-1,1,-1,1,0])
for config in x:
    drawBoard(config)
