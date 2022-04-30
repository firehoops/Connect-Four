import const
import time

#Handle Logic
class Model:
    def __init__(self):
        self.playerValue = 1
        self.board = [[0] * const.COL_COUNT for r in range(const.ROW_COUNT)]
        self.moveCount = 0

    #Returns the board
    def getBoard(self):
        return self.board

    #Returns true if a one of the players has 4 pieces vertically, horizontally, or diagonally.
    def winnerExists(self):

        # Check Horizontal
        for row in range(const.ROW_COUNT):
            for col in range(const.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row][col + 1] == self.playerValue \
                        and self.board[row][col + 2] == self.playerValue \
                        and self.board[row][col + 3] == self.playerValue:
                    return True

        # Check Vertical
        for row in range(const.ROW_COUNT - 3):
            for col in range(const.COL_COUNT):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col] == self.playerValue \
                        and self.board[row + 2][col] == self.playerValue \
                        and self.board[row + 3][col] == self.playerValue:
                    return True

        # Check Diagonal \
        for row in range(const.ROW_COUNT - 3):
            for col in range(const.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col + 1] == self.playerValue \
                        and self.board[row + 2][col + 2] == self.playerValue \
                        and self.board[row + 3][col + 3] == self.playerValue:
                    return True

        # Check Diagonal /
        for row in range(3, const.ROW_COUNT):
            for col in range(const.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row - 1][col + 1] == self.playerValue \
                        and self.board[row - 2][col + 2] == self.playerValue \
                        and self.board[row - 3][col + 3] == self.playerValue:
                    return True


    #Checking if row is free
    #Params: Board - the game board, colChoice - users selected col , and amount of rows
    #Returns: Returns the row number if valid by checking each row in that col and seeing if there is an open space indicated by a 0
    def checkRow(self, board ,colChoice):
        for rowNum in range(const.ROW_COUNT):
            if board[rowNum][colChoice] == 0:
                return rowNum
    #Params: colChoice - user selected col
    #Returns: Checks that user inputs a valid row# then checks if the board is full, then if there is a winner, otherwise it changes player and returns True
    def makeMove(self, colChoice):

        #Makes sure the column is valid
        try:
            row = self.checkRow(self.getBoard(), colChoice)
            self.getBoard()[row][colChoice] = self.playerValue
            self.moveCount += 1

            if self.moveCount == 43:
                print("No Winner")

            if self.winnerExists():
                self.endGame()
                return False
            if self.playerValue == 1:
                self.playerValue += 1
            else:
                self.playerValue -= 1
            return True
        except:
            print("Please Enter A Valid Column \n")
            time.sleep(.5)
            return True
    #Returns: Ends the game and prints out who the winner is
    def endGame(self):
        print(f"Player {self.playerValue} is the winner!!")
        time.sleep(.5)