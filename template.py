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

def restart():
    choice = simpledialog.askinteger("Restart",
                            "Would you like to do the adventure again?\n\nYes (1)\nNo (2)")
    if (choice == 1):
         intro()
    elif (choice == 2):
         root.destroy()
    else:
         restart()
            
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
        endingMoney1()
    elif (choice == 2):
        choiceMoney2()
    else:
        choiceMoney1()

def choiceMoney2():
     messagebox.showinfo("The Town",
                            "You walk back from where you came, but you cannot see\n"
                            "where you are. After a long walk you see a small town built\n"
                            "out of steel and spare parts from a fighter jet. Houses are\n"
                            "almost favela in their appearance.")
     choice = simpledialog.askinteger("Sheriff",
                                      "You enter the town. The town sheriff walks up to you and\n"
                                      "asks you what you are doing around here.\n\n"
                                      "Say you are here for supplies. (1)\n"
                                      "Say you are looking for work. (2)")
     if (choice == 1):
         choiceSupplies()
     if (choice == 2):
         choiceWork()
     else:
         choiceMoney2()

def choiceSupplies():
    choice = simpledialog.askinteger("Supplies",
                                     "You say you are her for supplies. He asks you what is in\n"
                                     "the bag over your shoulder. He searches your bad and\n"
                                     "comments on how stupid you are for having paper money.\n"
                                     "He asks if you are interested in working for him as a\n"
                                     "'Peacekeeper', which is practically a bounty hunter.\n\n"
                                     "Accept (1)\nDecline (2)")
    if (choice == 1):
        choicePeacekeeper()
    if (choice == 2):
        endingMoney2()
    else:
        choiceSupplies()
    
def choiceWork():
    choice = simpledialog.askinteger("Work",
                                     "You say you are looking for work. He offers you a position\n"
                                     "as a 'Peackeeper', which is practically a bounty hunter.\n\n"
                                     "Accept the offer (1)\nDecline the offer (2)")
     if (choice == 1):
        choicePeacekeeper()
    if (choice == 2):
        endingMoney2()
    else:
        choiceWork()

def choicePeacekeeper():
    messagebox.showinfo("Bounty",
                        "You agree to the offer, then the sheriff hands you a paper\n"
                        "and says 'Ask me for another paper when you're done.' You\n"
                        "look at the paper with a small picture of the target, His crime\n"
                        "and his bounty on him in gold coins.")
    messagebox.showinfo("Revolver",
                        "The Sheriff hands you a Revolver known for being used by\n"
                        "Rangers. It is full loaded. He says 'careful...there's only six\n"
                        "bullets in that. Bullets are on low supply around here. If you\n"
                        "ever find some ammo lying around and want to sell it, go to\n"
                        "Joseph the gun store owner.")

def endingMoney1():
    messagebox.showinfo("Death by Radiation",
                        "Cesium gets into your body. Due to the high amount of\n"
                        "cesium, your muscles slowly deteriorate. You collapse.\n"
                        "You die because of the intense heat and radiation.")
    messagebox.showinfo("Ending",
                        "You reached Ending 1 of 13 endings. Ending Type: Death")
    restart()

def endingMoney2():
    messagebox.showinfo("Decline",
                        "You decline the offer. He says, 'Your loss.' You choose to stay\n"
                        "in the town, working as a busser at the only bar. You live the\n"
                        "rest of your boring life in this town.")
    messagebox.showinfo("Ending",
                        "You reached Ending 2 of 13 endings. Ending Type: Poor")
    restart()

def endingMoney3():
    
def endingMoney4():
    
def endingMoney5():
    
def endingMoney6():

    
################ Main #####################
intro()

root.destroy()
