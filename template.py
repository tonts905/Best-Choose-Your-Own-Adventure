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
         messagebox.showinfo("Goodbye",
                             "Thanks for playing! Have a nice day.")
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
     elif (choice == 2):
         choiceWork()
     else:
         choiceMoney2()

def choiceSupplies():
    choice = simpledialog.askinteger("Supplies",
                                     "You say you are here for supplies. He asks you what is in\n"
                                     "the bag over your shoulder. He searches your bag and\n"
                                     "comments on how stupid you are for having paper money.\n"
                                     "He asks if you are interested in working for him as a\n"
                                     "'Peacekeeper', which is practically a bounty hunter.\n\n"
                                     "Accept (1)\nDecline (2)")
    if (choice == 1):
        choicePeacekeeper()
    elif (choice == 2):
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
    elif (choice == 2):
        endingMoney2()
    else:
        choiceWork()

def choicePeacekeeper():
    messagebox.showinfo("Bounty",
                        "You agree to the offer, then the sheriff hands you a paper\n"
                        "and says 'Ask me for another paper when you're done.' You\n"
                        "look at the paper with a small picture of the target, his crime\n"
                        "and his bounty on him, in gold coins.")
    messagebox.showinfo("Revolver",
                        "The Sheriff hands you a revolver known for being used by\n"
                        "Rangers. It is full loaded. He says 'Careful...there's only six\n"
                        "bullets in that. Bullets are on low supply around here. If you\n"
                        "ever find some ammo lying around and want to sell it, go to\n"
                        "Joseph the gun store owner.")
    messagebox.showinfo("Takeout",
                        "You go to the house in the outskirts where\n"
                        "it says he is, sneaking in through the back, crouching behind\n"
                        "the counter. You pull our your gun, using the counter to help\n"
                        "you aim. You shoot him once. He falls over and you walk towards\n"
                        "his limp form, shooting him once more...eliminating your target.\n"
                        "You search his body and find ammo...but it's not for your gun.\n"
                        "You take his ring off and his necklace, as proof of your kill. You\n"
                        "walk back to the town, slightly shaken up. You present the proof\n"
                        "to the sheriff, who pays you one gold coin.")
    choice = simpledialog.askinteger("Sell",
                                     "You go to Joseph and he asks if you want to buy more\n"
                                     "rounds for the Peacekeeper revolver. You buy six more\n"
                                     "rounds, spending your gold coin. He asks if you have \n"
                                     "unneeded ammo.\n\nSell your ammo (1)\nKeep your ammo (2)")
    if (choice == 1):
        choicePeacekeeper2()
    elif (choice == 2):
        endingMoney3()
    else:
        choicePeacekeeper()

def choicePeacekeeper2():
    choice = simpledialog.askinteger("Next",
                                     "You sell the rare sniper ammo, the .338 round. You obtain\n"
                                     "10 coins from Joseph. He offers you a Tec-9 gun for sale.\n"
                                     "\nPurchase the Tec-9 (1)\nReject the offer (2)")
    if (choice == 1):
        choicePeacekeeper3()
    elif (choice == 2):
        endingMoney4()
    else:
        choicePeacekeeper2()

def choicePeacekeeper3():
    messagebox.showinfo("Tec-9",
                        "You buy the Tec-9 and two magazines for 10 coins.")
    choice = simpledialog.askinteger("Mission",
                                     "You go to the sheriff for another bounty. He hands you\n"
                                     "multiple papers and says he needs you to take down a local\n"
                                     "gang in the area that is expanding in members. They destroyed\n"
                                     "many towns with their 'Jet' (drug), which is extremely\n"
                                     "addictive. You see that the bounty is two gold bars, which is\n"
                                     "worth 200 gold coins. You scout their hideout. Do you use\n"
                                     "the bomb the sheriff gave you and take them out quickly, or\n"
                                     "do you enter and terminate them silently?\n\nUse the C4 (1)\n"
                                     "Silently kill each raider (2)")
    if (choice == 1):
        endingMoney5()
    elif (choice == 2):
        endingMoney6()
    else:
        choicePeacekeeper3()

def endingMoney1():
    messagebox.showinfo("Radiation",
                        "Cesium gets into your body. Due to the high amount of\n"
                        "cesium, your muscles slowly deteriorate.")
    messagebox.showinfo("Death",
                        "You collapse. You die because of the intense heat and\n"
                        "radiation.")
    messagebox.showinfo("Ending",
                        "You reached Ending 1 of 13 endings. Ending Type: Death")
    restart()

def endingMoney2():
    messagebox.showinfo("Decline",
                        "You decline the offer. He says, 'Your loss.'")
    messagebox.showinfo("Busser",
                        "You choose to stay in the town, working as a busser at the\n"
                        "only bar. You live the rest of your boring life in this town.")
    messagebox.showinfo("Ending",
                        "You reached Ending 2 of 13 endings. Ending Type: Poor")
    restart()

def endingMoney3():
    messagebox.showinfo("Peace",
                        "You say no and live the rest of your life peacefully in a favela\n"
                        "style shack.")
    messagebox.showinfo("Ending",
                        "You reached Ending 3 of 13 endings. Ending Type: Mediocre")
    restart()
    
def endingMoney4():
    messagebox.showinfo("Life",
                        "You buy a house with your large amount of coins and become\n"
                        "renowned as a wealthy man in the town. You have great power.")
    messagebox.showinfo("Ending",
                        "You reached Ending 4 of 13 endings. Ending Type: Good")
    restart()
    
def endingMoney5():
    messagebox.showinfo("Chaos",
                        "You see a crawlspace entrance on the side of the house. You\n"
                        "manage to squeeze through...placing the C4 under a pipe.")
    messagebox.showinfo("Chaos",
                        "You wire it to a car battery and a receiver, then squeeze out\n"
                        "and quickly sneak a few hundred feet away.")
    messagebox.showinfo("Chaos",
                        "You activate the detonator (a makeshift garage door opener),\n"
                        "causing the house to explode a lot more violently than you\n"
                        "expected. Debris flies everywhere as the house is enveloped\n"
                        "in engulfing flames. Youmust have struck a gas line...")
    messagebox.showinfo("Luxury",
                        "You go back to the town. The sheriff says, 'I could feel that\n"
                        "explosion from here! I thought you were killed...'")
    messagebox.showinfo("Luxury",
                        "'Well, good work. I have no more bounties at the moment.\n"
                        "Everything seems to be pretty calm in these parts, now that\n"
                        "we have a fierce peacekeeper.' He hands you two gold bars,\n"
                        "and you buy a nice place in town.")
    messagebox.showinfo("Ending",
                        "You reached Ending 5 of 13 endings. Ending Type: Great")
    restart()
    
def endingMoney6():
    messagebox.showinfo("Stealth",
                        "You sneak in, taking one out with a knife.")
    messagebox.showinfo("Stealth",
                        "Someone hears you. They snatch their rifle and storm into the room\n"
                        "you are in. He shoots you.")
    messagebox.showinfo("Stealth",
                        "The bullet connects with your left shoulder, wounding you. You\n"
                        "shoot him multiple times very quickly with your blowback.")
    messagebox.showinfo("Stealth",
                        "You move to the living room and annihilate two with your revolver.\n"
                        "You hear several in the garage, sneaking in and hiding behind a bench.")
    messagebox.showinfo("Stealth",
                        "When you are sure they cannot see you, you fire at the bench, your\n"
                        "bullets penetrate the bench and leave tennis ball sized holes in their\n"
                        "chests.")
    messagebox.showinfo("Stealth",
                        "You check the house a few more times and find nobody else. Walking\n"
                        "back into the garage, you find a stockpile of gold, drugs, and\n"
                        "ammunition. You take the gold and ammo.")
    messagebox.showinfo("Stealth",
                        "You find a medical bot in the corner. You switch it to the bullet wound\n"
                        "setting, and it puts you to sleep.")
    time.sleep(5)
    messagebox.showinfo("Gold",
                        "You wake up two hours later. Fully healed, you walk back to the sheriff,\n"
                        "carry your loot with you in a sack. He has somehow confirmed your kills.")
    messagebox.showinfo("Gold",
                        "He gives you the bounty of two gold bars and you live outside the\n"
                        "town, making your own fortress with the help of your gold and the\n"
                        "townspeople.")
    messagebox.showinfo("Ending",
                        "You reached Ending 6 of 13 endings. Ending Type: Second Best")
    restart()
    
################ Main #####################
intro()

root.destroy()
