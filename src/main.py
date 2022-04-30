from tkinter import *
from controller import Controller
from view import View
from model import Model


if __name__ == "__main__":
    root = Tk()
    
    # Initialize View and Model
    model = Model()
    view = View()

    #Starts everything
    start = Controller(root=root, view=view, model=model)
    root.mainloop()