# Connect-Four
Connect-four game that can switch between command line and gui gameplay!

Inspiration: The idea and main logic comes from a school project I had to do involving a model, view, controller (MVC) architecture. This has now been refactored in 2022, in which I moved this app away from one large file into a more readable and maintainble application.

Note: This uses tkinter as the gui and when swapping into gui view the tkinter gui window will go to your primary monitor and appear as a tab in your taskbar.

The game currently only supports switching from gui -> text view mid game not vice versa due to a tkinter window bug.

## Starting the app

``` 
python src/main.py
```
