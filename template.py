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
    messagebox.showinfo("MLG APOCALYPSE SIMULATOR 2015",
                        "You are a survivor of the apocalypse in the year 2031. WWIII\n"
                        "has occured, resulting in worldwide chemical, biological\n"
                        "and nuclear war. You stand in front of a duffle bag of money\n"
                        "and a duffle bag of gold riches. Which do you take?")
    choice = simpledialog.askinteger("Choose wisely","Gold Riches (1)\nPaper Money (2)")
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
def choiceGold1():
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

def choicegun():
    choice = simpledialog.askinteger("LoadoutChoice",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("",
                            "")
    else (choice == 3):
        messagebox.showinfo("You choose to take over the store with loadout 2",
                            "You load your shotgun with the provided buckshot shells, quickly aiming and firing",
                            "On the owner, instantly killing him. A guard swiftly shoots you in the back with his handgun.",
                            "You roll over, Shooting both the guards.")
        messagebox.showinfo("You feel extreme pain from the bullet, You realize that you need intensive medical aid to survive.n\"
                           "You catch something in the corner of the room that seems to be a medical bot.\n"
                           "You crawl over to it, onto the gurney and it injects anesthetics into you. You fall asleep…")
        messagebox.showinfo("When you wake up it is bright outside.")
        

def choiceExplore():
        choiceExplore = simpledialog.askinteger("You take over the store. Do you choose to explore the store")
    

if (choice == 1):
    messagebox.showinfo("Explore",
                        "You decide to explore the store. You see a giant vault door after going down a flight of stairs.\n"
                        "You enter, Realizing theres a small bedroom in there, But seeing a huge stock pile of guns in gun cases with ammunition.\n"
                        "Do you wish to stay in this room or leave?")
def ChoiceVault
if (choice == 1 )
    messagebox.showinfo("Stay",
                        "You choose to stay inside the vault, Sealing yourself in.\n"
                        "You decide you need to go to the bathroom. As you start to head out you realize the door is sealed.. n\"
                        "You stay in the vault for several days with no water before you die of dehydration.")

(choice == 2):
    messagebox.showinfo("Leave",
                        "You choose to stock up on weapons and ammo.\n"
                        "You leave the store and continue onto amador city. While traveling to Amador city \n"
                        "You find several mercenaries standing beside their dead employer, a caravaner. Do you hire them?)"
def ChoiceHire
if (choice == 1):
    messagebox.showinfo("Hire",
                        "You choose to hire the mercs despite their former employer being dead. You ask them if they would be interested in work.\n"
                        "They agree and you give them 3 gold coins each. You walk with them until you see a small city.")
                    
messagebox.showinfo("Amador City",
                     "You choose to walk into the town with the mercs. You have talked about taking over for several days with them.\n"
                     "Do you wish to take over?Take over Amador City(1) Stay in the town peacefully(2)")
def ChoiceAmador
if (choice == 1):
messagebox.showinfo("Take over",
                    "You plan to use your grand wealth to start campaigning in the town… \n"
                    "You manage to get the several hundred people in the town behind you back but not all of them.\n"
                    "You raid the armory in the town, getting several Omega death lasers and several plasma rifles.\n"
                    "These are a good thing you give to your highest generals. You give the rest of the people normal guns.\n"
  messagebox.showinfo("Continued",
                      "You decide to take over the town. You have many of the guards on your side as well. \n"
                      "You go to the town center, Blitzkreiging it. You manage to capture several town leaders, Executing and burying them in a discreet location.\n"
                       "The people are glad to be rid of that but not without many casualties… You are elected unanimously the leader)
                    


################ Steven's Functions #####################
                            
def choiceMoney1():
    messagebox.showinfo("GG",
                        "Good news, you have $1,000,000 in paper money.")
    messagebox.showinfo("GG",
                        "Bad news, paper money means nothing in the apocalypse.")
    messagebox.showinfo("Plains",
                        "You walk into a dusty plain, and you can see nothing.\n"
                        "You have your giant bag of money, however, you don't\n"
                        "know what's ahead.")
    choice = simpledialog.askinteger("Choose wisely",
                                     "Continue (1)\nWalk Back (2)")
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
     messagebox.showinfo("Sheriff",
                            "You enter the town.")
     choice = simpledialog.askinteger("Sheriff",
                                      "The town sheriff walks up to you and\n"
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
    messagebox.showinfo("Supplies",
                        "You say you are here for supplies. He asks you what is in\n"
                        "the bag over your shoulder.")
    messagebox.showinfo("Supplies",
                        "He searches your bag and comments on how stupid you are\n"
                        "for having paper money.")
    choice = simpledialog.askinteger("Peacekeeper",
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
                        "You agree to the offer. The sheriff hands you a paper\n"
                        "and says 'Ask me for another paper when you're done.'\n")
    messagebox.showinfo("Bounty",
                        "You look at the paper with a small picture of the target,\n"
                        "his crime and his bounty on him, in gold coins.")
    messagebox.showinfo("Revolver",
                        "The Sheriff hands you a revolver known for being used\n"
                        "by Rangers. It is full loaded.")
    messagebox.showinfo("Revolver",
                        "He warns 'Careful...there's only six bullets in that.\n"
                        "Bullets are on low supply around here. If you ever find\n"
                        "some ammo lying around and want to sell it, go to\n"
                        "Joseph the gun store owner.")
    messagebox.showinfo("Takeout",
                        "You go to the house in the outskirts where it says\n"
                        "he is. You sneak in through the back, crouching behind\n"
                        "the counter.")
    messagebox.showinfo("Takeout",
                        "You pull out your gun, using the counter to help you\n"
                        "aim. You shoot him once.")
    messagebox.showinfo("Takeout",
                        "He falls over. You walk towards his limp form, shooting\n"
                        "him once more, eliminating your target. You search his\n"
                        "body and find ammo, but it's not for your gun.")
    messagebox.showinfo("Proof",
                        "You take his ring off and his necklace, as proof of your\n"
                        "kill.")
    messagebox.showinfo("Proof",
                        "You walk back to the town, slightly shaken up. You present\n"
                        "the proof to the sheriff, who pays you one gold coin.")
    messagebox.showinfo("Joseph",
                        "You go to Joseph and he asks if you want to buy more\n"
                        "rounds for the Peacekeeper revolver. You buy six more\n"
                        "rounds, spending your gold coin.")
    choice = simpledialog.askinteger("Sell",
                                     "He asks if you have unneeded ammo.\n\n"
                                     "Sell your ammo (1)\nKeep your ammo (2)")
    if (choice == 1):
        choicePeacekeeper2()
    elif (choice == 2):
        endingMoney3()
    else:
        choicePeacekeeper()

def choicePeacekeeper2():
    messagebox.showinfo("Sell",
                        "You sell the rare sniper ammo, the .338 round. You\n"
                        "obtain 10 coins from Joseph.")
    choice = simpledialog.askinteger("Tec-9",
                                     "He offers you a Tec-9 gun for sale.\n\n"
                                     "Purchase the Tec-9 (1)\nReject the offer (2)")
    if (choice == 1):
        choicePeacekeeper3()
    elif (choice == 2):
        endingMoney4()
    else:
        choicePeacekeeper2()

def choicePeacekeeper3():
    messagebox.showinfo("Tec-9",
                        "You buy the Tec-9 and two magazines for 10 coins.")
    messagebox.showinfo("Mission",
                        "You go to the sheriff for another bounty. He hands you\n"
                        "multiple papers and says he needs you to take down a local\n"
                        "gang in the area that is expanding in members.")
    messagebox.showinfo("Mission",
                        "They destroyed many towns with their 'Jet' (drug), which is\n"
                        "extremely addictive. You see that the bounty is two gold\n"
                        "bars, which is worth 200 gold coins.")
    messagebox.showinfo("Mission",
                        "You make your way towards the target location. You find a\n"
                        "small complex at the site, in which you deduce is their base.")
    choice = simpledialog.askinteger("Mission",
                                     "You scout their hideout. After a rough diagnosis, you realize\n"
                                     "you have two options. Do you use the bomb the sheriff gave\n"
                                     "you and take them out quickly, or do you enter and terminate\n"
                                     "them silently?\n\nUse the C4 (1)\nSilently kill each raider (2)")
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
                        "in engulfing flames. You must have struck a gas line...")
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
                        "When you are sure they cannot see you, you fire at the bench. Your\n"
                        "bullets penetrate the bench and leave tennis ball sized holes in their\n"
                        "chests.")
    messagebox.showinfo("Stealth",
                        "You check the house a few more times and find nobody else. Walking\n"
                        "back into the garage, you find a stockpile of gold, drugs, and\n"
                        "ammunition. You take the gold and ammo.")
    messagebox.showinfo("Stealth",
                        "You find a medical bot in the corner. You switch it to the bullet wound\n"
                        "setting, and it puts you to sleep.")
    time.sleep(2)
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
