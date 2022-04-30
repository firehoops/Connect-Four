"""Text-Based and GUI"""

import const

class View:
    def __init__(self):
        self.board = []

    # Params: Message - takes in the user input message
    # Return: returns the userinput as a string
    def getUserInput(self, message: str) -> str:
        userInput = input(message)
        return userInput

    """
    Params: game_board
    Result: prints out the gameboard"""
    def displayBoard(self,board):
        printBoard = ""

        # Reverse board for printing
        boardRotate = board[::-1]
        for r in range(const.ROW_COUNT):
            for c in range(const.COL_COUNT):
                printBoard += "|" + str(boardRotate[r][c])
            printBoard += "|\n"
        print(printBoard)