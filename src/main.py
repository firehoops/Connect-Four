from tkinter import *
from src.controller import Controller
from src.view import View
from src.model import Model


if __name__ == "__main__":
    root = Tk()
    
    # Initialize View and Model
    model = Model()
    view = View()

    #Starts everything
    start = Controller(root=root, view=view, model=model)
    root.mainloop()