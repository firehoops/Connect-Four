'''
Created on Mar 9, 2020

@author: yokow
'''
import unittest
import numbers
import decimal
import types
from tkinter import *
import tkinter.font
import tkinter.messagebox
import time
import os

class TestView(unittest.TestCase):

    def test___init__(self):
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
        
    def test_getUserInput(self):
        # Test that input is not empty string
        self.assertTrue(len(test_getUserInput()) > 0, "String is not empty")
        
    def test_displayBoard(self,board):
        printBoard = ""

        boardRotate = board[::-1]
        for r in range(self.ROW_COUNT):
            for c in range(self.COL_COUNT):
                printBoard += "|" + str(boardRotate[r][c])
            printBoard += "|\n"
        print(printBoard)
        
        self.assertTrue(len(printBoard) > 0, "printBoard String is not empty")


class test_Model(unittest.TestCase):
    def test___init__(self):

        self.playerValue = 1
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
        self.board = [[0] * self.COL_COUNT for r in range(self.ROW_COUNT)]
        self.moveCount = 0
        
    def test_getBoard(self):
        return self.board
        self.assertTrue(isinstance(self.board, numbers.Number) , "")

    def test_winnerExists(self):
        # Check Horizontal
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row][col + 1] == self.playerValue \
                        and self.board[row][col + 2] == self.playerValue \
                        and self.board[row][col + 3] == self.playerValue:
                    return True
        
        # Check Vertical
        for row in range(self.ROW_COUNT - 3):
            for col in range(self.COL_COUNT):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col] == self.playerValue \
                        and self.board[row + 2][col] == self.playerValue \
                        and self.board[row + 3][col] == self.playerValue:
                    return True
                
        self.assertEqual(test_winnerExists() , True)
         
  

         
    def test_checkRow(self, board ,colChoice, ROW_COUNT):
        for rowNum in range(ROW_COUNT):
            if board[rowNum][colChoice] == 0:
                return rowNum
            self.assertTrue(rowNum == 0, "rowNum should be 0")
    
    def test_makeMove(self, colChoice):
        row = model.checkRow(model.getBoard(), colChoice, self.ROW_COUNT)
        model.getBoard()[row][colChoice] = self.playerValue
        self.moveCount += 1
        #********need a  check that they can't go out of range*****
        if self.moveCount == 43:
            print("No Winner")
            self.assertTrue(self.moveCount == 43, "Should print No Winner")

        if model.winnerExists():
            start.c.grid_forget()
            start.bottomFrame.grid_forget()
            header = tkinter.font.Font(size=40, weight=tkinter.font.BOLD)
            if self.playerValue == 1:
                lab = Label(root, text = "Player 1 is the Winner!!",font = header).grid(row = 2, column = 2, rowspan = 4, columnspan = 4)
                print("Player 1 is the Winner!!")
                return False
            else:
                lab = Label(root, text="Player 2 is the Winner!!", font=header).grid(row=2, column=2, rowspan=4, columnspan=4)
                print("Player 2 is the Winner!!")
                return False

        if self.playerValue == 1:
            self.playerValue += 1
        else:
            self.playerValue -= 1
        return True
    
        self.assertTrue(type(test_makeMove()) == bool, msg)
        

 # Initialize View and Model
model = test_Model()
view = TestView()

class test_Controller(unittest.TestCase):
    #Main method
    def __init__(self, master):
        self.coords_col_1 = [0, 500, 100, 600]
        self.coords_col_2 = [100, 500, 200, 600]
        self.coords_col_3 = [200, 500, 300, 600]
        self.coords_col_4 = [300, 500, 400, 600]
        self.coords_col_5 = [400, 500, 500, 600]
        self.coords_col_6 = [500, 500, 600, 600]
        self.coords_col_7 = [600, 500, 700, 600]
        self.c = Canvas(master, width=700, height=600, bg="gray")
        self.bottomFrame = Frame(master, width=700, height=200)
        #Starting the game
        option = view.test_getUserInput("Type text or gui for your version of Connect Four\n")
        if option.lower() == "gui":
            self.gui(master)
        else:
            #not pulling up gui for some reason
            self.gui(master)
            self.textView(master)

     #The remaining funcs and classes test cases are not written because they have no return value

   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()