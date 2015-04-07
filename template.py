# template.py
# by BJS
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
    messagebox.showinfo("MLG APOCALYPSE SIMULATOR 2015", "\nYou are a survivor in the apocalypse in the year 2031."
                        "\nWWIII has happened, resulting in world wide chemical, biological"
                        "\nand nuclear war. You stand in front of a duffle bag of money and"
                        "\na duffle bag of gold riches. Which do you take?")
    choice = simpledialog.askinteger("Choose wisely","\nGold Riches (1)\nPaper Money (2).")
    if choice == 1:
        choice1()
    elif choice == 2:
        choiceMoney1()
    else:
        intro()

################ Joseph's Fuctions #####################
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

################ Brad's Functions #####################

""" Continue Joseph's functions """


################ Steven's Functions #####################
def choiceMoney1():
    messagebox.showinfo("Uh Oh!",
                        "Good news, you have $1,000,000 in paper money.\n"
                        "Bad news, paper money means nothing in the apocalypse.")
    choice = simpledialog.askinteger("Choose wisely",
                                     "You walk into a dusty plain, and you can see nothing.\n"
                                     "You have your giant bag of money, however...You don't\n"
                                     "know what's ahead.\n\nContinue (1)\nWalk Back (2)")
    if (choice == 1):
        messagebox.showinfo("Death by Radiation",
                            "Cesium gets into your body. Due to the high amount of\n"
                            "cesium, your muscles slowly deteriorate. You collapse.\n"
                            "You die because of the intense heat and radiation.")
        messagebox.showinfo("Ending",
                            "You reached Ending 1 of 13 endings. Ending Type: Death")

    elif (choice == 2):
        messagebox.showinfo("The Town",
                            "You walk back from where you came, but you cannot see\n"
                            "where you are. After a long walk you see a small town built\n"
                            "out of steel and spare parts from a fighter jet. Houses are\n"
                            "almost favela in their appearance.")
    else:
        choice2()

def choice

################ Main #####################
intro()

root.destroy()
