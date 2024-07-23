GameBoard = [[" * "," * "," * "," * "," * "," * "," * "], [" * "," * "," * "," * "," * "," * "," * "], [" * "," * "," * "," * "," * "," * "," * "], [" * "," * "," * "," * "," * "," * "," * "], [" * "," * "," * "," * "," * "," * "," * "], [" * "," * "," * "," * "," * "," * "," * "]]
row = []

player2turnValid = False
player1turnValid = False
xHorizRow = 0
yHorizRow = 0
xVertiRow = 0
yVertiRow = 0
xDiagRow = 0
yDiagRow = 0
xWin = False
yWin = False
drawCheck = False

def printBoard():
    for i in GameBoard:

        for n in i:
            row.append(n)
        
        print(row)
        row.clear()

def player1turn():
    global player1turnValid
    playerChoice = int(input("Which column do you want to drop into? Choose 1 to 7"))
    if playerChoice > 0 or playerChoice < 8:
        for i in reversed(GameBoard):
            if i[playerChoice-1] == " * ":
                i[playerChoice-1] = " X "
                player1turnValid = True
                printBoard()
                break

            elif GameBoard[0][playerChoice-1] != " * ":
                print("You fucked it! You can't drop more in here! :3")
                break

        else:
            pass
    else:
        print("Input error!")

def player2turn():
    global player2turnValid
    playerChoice = int(input("Which column do you want to drop into? Choose 1 to 7"))
    if playerChoice > 0 or playerChoice < 8:
        for i in reversed(GameBoard):
            if i[playerChoice-1] == " * ":
                i[playerChoice-1] = " Y "
                player2turnValid = True
                printBoard()
                break

            elif GameBoard[0][playerChoice-1] != " * ":
                print("You fucked it! You can't drop more in here! :3")
                break
        
        else:
            pass
    else:
        print("Input error!")

def HorizontalWinCheck():
    global yHorizRow
    global xHorizRow
    global xWin
    global yWin
    xHorizRow = 0
    yHorizRow = 0
    for i in GameBoard:
        for n in i:
            if n == " X ":
                yHorizRow = 0
                xHorizRow += 1
                if xHorizRow == 4:
                    xWin = True
                    print("xWin HORI")
            elif n == " Y ":
                xHorizRow = 0
                yHorizRow += 1
                if yHorizRow == 4:
                    yWin = True
                    print("yWin HORI")
            else:
                xHorizRow = 0
                yHorizRow = 0

def VerticalWinCheck():
    global yVertiRow
    global xVertiRow
    global xWin
    global yWin
    xVertiRow = 0
    yVertiRow = 0

    for x in range(0, 6):
        for i in GameBoard:
            if i[x] == " X ":
            
                yVertiRow = 0
                xVertiRow += 1
                if xVertiRow == 4:
                    xWin = True
                    print("xWin VERT")
            elif i[x] == " Y ":

                xVertiRow = 0
                yVertiRow += 1
                if yVertiRow == 4:
                    yWin = True
                    print("yWin VERT")
            elif i[x] == " * ":
                
                xVertiRow = 0
                yVertiRow = 0

def DiagonalWinCheck():
    global yDiagRow
    global xDiagRow
    global xWin
    global yWin
    xDiagRow = 0
    yDiagRow = 0

    for i in range(0, 6):
        for x in range(0, 6):
            try:
                #print(GameBoard[i][x])
                if GameBoard[i][x] == GameBoard[i-1][x+1] == GameBoard[i-2][x+2] == GameBoard[i-3][x+3] == " X ":
                    xWin = True
                    print("xWin DIAG")
                    return True
                elif GameBoard[i][x] == GameBoard[i-1][x-1] == GameBoard[i-2][x-2] == GameBoard[i-3][x-3] == " X ":
                    xWin = True
                    print("xWin DIAG")
                    return True                   
                if GameBoard[i][x] == GameBoard[i-1][x+1] == GameBoard[i-2][x+2] == GameBoard[i-3][x+3] == " Y ":
                    yWin = True
                    print("yWin DIAG")     
                    return True
                elif GameBoard[i][x] == GameBoard[i-1][x-1] == GameBoard[i-2][x-2] == GameBoard[i-3][x-3] == " Y ":
                    yWin = True
                    print("yWin DIAG")
                    return True   

            except IndexError:
                continue

def DrawCheck():
    global drawCheck
    drawCheck = True
    for i in GameBoard:
        for n in i:
            if n == " * ":
                drawCheck = False
                return drawCheck


def GeneralWinCheck():
    HorizontalWinCheck()
    VerticalWinCheck()
    DiagonalWinCheck()
    DrawCheck()



while True:
    while player1turnValid == False and xWin == False and yWin == False:
        player1turn()
    player1turnValid = False

    GeneralWinCheck()

    if drawCheck == True:
        print("No more available moves!")
        break

    while player2turnValid == False and xWin == False and yWin == False:
        player2turn()
    player2turnValid = False

    GeneralWinCheck()

    if xWin == True:
        print("Xs win!")
        break

    elif yWin == True:
        print("Ys win!")
        break

    if drawCheck == True:
        print("No more available moves!")
        break
