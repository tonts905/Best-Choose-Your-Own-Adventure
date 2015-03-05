# template.py
# by SpamBot
# Description: Template for our CYOP

# Import Statements

import math
import random
import time
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

# Create a window
root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you are a _____ from ____. " + \
                        "You stumble across such and such.")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1 or 2.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Brad's Fuctions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Steven's Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Joseph's Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()
        
################ Main #####################
intro()

root.destroy()
