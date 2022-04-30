from tkinter import *
import tkinter.font
import tkinter.messagebox
import time
import const


class Controller:

    def __init__(self, root, view, model):
        # x0, y0, x1, y1
        self.col_to_coords = {
            0: [5, 500, 105, 600],
            1: [120, 500, 220, 600],
            2: [235, 500, 335, 600],
            3: [355, 500, 455, 600],
            4: [470, 500, 570, 600],
            5: [585, 500, 685, 600],
            6: [700, 500, 800, 600]
        }
        self.track_moves = []
        self.root = root
        self.c = Canvas(self.root, width=800, height=600, bg="lightsky blue")
        self.buttonFrame = Frame(self.root, width=800, height=200)
        self.playerScoreFrame = Frame(self.root, width=800, height=50)
        self.bottomFrame = Frame(self.root, width=800, height=50)
        
        self.view = view
        self.model = model
        # Starting the game
        option = self.view.getUserInput("Type text or gui for your version of Connect Four\n")
        if option.lower() == "gui":
            self.gui()
        else:
            self.text_view()
    # Creates the gui
    # Returns: Creates a gui by adding frames and buttons to the self.root window
    def gui(self):
        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(self.root, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=3)

        # Create Seperation from Board to have buttons and exit/switch self.view buttons

        self.c.grid(row=1, column=0, rowspan=6, columnspan=7)
        self.buttonFrame.grid(row=8, column=0, columnspan=7)
        self.playerScoreFrame.grid(row=9, column=0, columnspan=7)
        self.bottomFrame.grid(row=10, column=0, columnspan=7)
        colTracker = [*range(const.COL_COUNT)]

        Button(self.buttonFrame, text="Row 1", relief = "groove", width= 12,command=lambda: \
            self.addPiece(colTracker[0])).grid(row=8, column=0, padx = 3)
        Button(self.buttonFrame, text="Row 2", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[1])).grid(row=8, column=1, padx =3)
        Button(self.buttonFrame, text="Row 3", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[2])).grid(row=8, column=2, padx =3)
        Button(self.buttonFrame, text="Row 4", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[3])).grid(row=8, column=3, padx =3)
        Button(self.buttonFrame, text="Row 5", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[4])).grid(row=8, column=4, padx =3)
        Button(self.buttonFrame, text="Row 6", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[5])).grid(row=8, column=5, padx =3)
        Button(self.buttonFrame, text="Row 7", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[6])).grid(row=8, column=6, padx =3)


        Button(self.bottomFrame, text="Exit", relief = "groove",width=15,command=lambda: self.quit()).grid(row=10, column=2, pady = 30, padx = 15)
        Button(self.bottomFrame, text="Switch views", relief = "groove",width= 15,command=lambda: self.switchToText()).grid(row=10,column=4)
        

    #Returns: Runs the text self.view of the game and gets the user input and continues the game based on their choice.
    def text_view(self):
        run = True
        #Game Loop
        while run:

            #User Input Loop
            while True:

                # make sure user gives valid input
                try:
                    self.view.displayBoard(self.model.getBoard())

                    colChoice = int(
                        self.view.getUserInput("Select a Column 0,1,2,3,4,5, or 6 (or type 8 to exit) & press enter\n"))
                    if colChoice == 8:
                        run = False
                        break
                    if colChoice == 9:
                        self.gui()

                    run = self.model.makeMove(colChoice)

                    break #Exits the User Input Loop
                except:
                    print("Please Enter A Valid Column \n")
                    time.sleep(.5)
        self.root.quit()
        exit()

    #Adds a piece to the board
    #Params: col - user selected col
    #Returns: adds a piece to the canvas as well as adding it to the game board to track the text self.view and keep game logic
    def addPiece(self, col):
        #Starting coord for row 1 , x0 = 0 , y0 = 500 , x1 = 100 , y1= 600
        
        self.track_moves.append(self.col_to_coords[col])
        playerValueFont = tkinter.font.Font(size=15, weight=tkinter.font.BOLD)

        if self.model.playerValue == 1:
            self.c.create_oval(self.col_to_coords[col][0], self.col_to_coords[col][1], self.col_to_coords[col][2], self.col_to_coords[col][3], fill="black")
            Label(self.root, text="Player " + str(self.model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
        else:
            self.c.create_oval(self.col_to_coords[col][0], self.col_to_coords[col][1], self.col_to_coords[col][2], self.col_to_coords[col][3], fill="red")
            Label(self.root, text="Player " + str(self.model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
        self.col_to_coords[col][1] -= 100
        self.col_to_coords[col][3] -= 100
        self.model.makeMove(col)

    #Switches the veiw from the GUI to the text self.view
    #Returns: Closes the GUI and runs the text self.view
    def switchToText(self):
        self.root.destroy()
        self.text_view()
    
    #Switches the veiw from the GUI to the text self.view
    #Returns: Closes the GUI and runs the text self.view
    def switchToGui(self):
        self.root.update()
        self.root.deiconify()


    # Closes the GUI
    # Returns: destroys the self.root window
    def quit(self):
        self.root.quit()