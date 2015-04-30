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
        choiceGold1()
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
    messagebox.showinfo("Wise selection",
                        "Paper money means nothing nowadays. As you have opted for\n"
                        "the gold riches, you are a very rich man. You can afford most\n"
                        "supplies on the way to Amador City, California.")
    choice = simpledialog.askinteger("Drug Dealer",
                                     "As you walk to the city, you encounter a Jamaican drug dealer\n"
                                     "dolphin with a lead pipe. Do you fight? And when you fight, do\n"
                                     "you praise the almighty Shrek before battles?\n\nFight without praying (1)"
                                     "\nPray to Shrek before you fight (2)\nRun (3)")
    if (choice == 1):
        endingGold1()
    elif (choice == 2):
        choiceGold2()
    elif (choice == 3):
        endingGold2()
    else:
        choiceGold1()

def choiceGold2():
    messagebox.showinfo("Battle",
                        "Shrekalujah! You go into battles with the drug dealing scum.")
    messagebox.showinfo("Battle",
                        "The dolphin takes the first swing at you and misses.")
    messagebox.showinfo("Victory",
                        "You smell onions. Out of the corner of your\n"
                        "eye, you see Shrek come to your aid, picking\n"
                        "up the dolphin and tearing him to pieces.")
    messagebox.showinfo("Proceed",
                        "After thanking Shrek for his help, you continue towards Amador City.")
    choice = simpledialog.askinteger("Store",
                                     "After 40 minutes of walking, you see a store. Do you enter?\n\n"
                                     "Yes (1)\nNo (2)")
    if (choice == 1):
        choiceStore1()
    elif (choice == 2):
        endingGold3()
    else:
        choiceGold2()

def choiceStore1():
    messagebox.showinfo("Chef",
                        "The owner of the store, Chef, looks at you suspiciously, with a gun\n"
                        "in hand. He quickly puts it away, realizing you are not a raider.")
    choice = simpledialog.askinteger("Chef",
                                     "Chef asks if you are looking to buy anything.\n\nYes (1)\nNo (2)")
    if (choice == 1):
        choicegun()
    elif (choice == 2):
        ChefFarewell()
    else:
        choiceStore1()

def ChefFarewell():
    messagebox.showinfo("Leave",
                            "You give Chef your farewells and exit the store.")
    endingGold3()
def endingGold1():
    messagebox.showinfo("Death",
                        "You do not pray? You get hit in the back when you are\n"
                        "not looking, and you get shrekt. You go to Shrekven,\n"
                        "and the almighty Shrek puts you into purgatory.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 7 of 13 endings. Ending Type: Death")
    restart()
    
def endingGold2():
    messagebox.showinfo("Death",
                        "The dolphin destroys you with a lead pipe, because it can use more\n"
                        "of its brain. It outsmarts you and discovers an MLG stratz.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 8 of 13 endings. Ending Type: Death")
    restart()

def endingGold3():
    messagebox.showinfo("Walk",
                        "You continue your walk towards Amador City.")
    messagebox.showinfo("Arrival",
                        "You arrive at Amador, but you do not have enough power to take\n"
                        "over. Instead, you buy a large house, heavily protected by traps,\n"
                        "fencing, and is supplied with all your daily needs.")
    messagebox.showinfo("Couch Potato",
                        "You spend most of your time watching TV from 15 years ago...")
    messagebox.showinfo("Ending",
                        "You have reached Ending 9 of 13 endings. Ending Type: Fatty")
    restart()
                    
################ Brad's Functions #####################

def choicegun():
    messagebox.showinfo("Choice",
                        "Chef shows you the loadouts he sells.")
    choice = simpledialog.askinteger("Choice",
                                     "= Loadout 1 =\n+ AR-15 w/ bumpfire stock\n"
                                     "+ M1911\n+ Combat knife\n+ Kevlar\n+ Ammunition:\n   ~ AR-15: 10 magazines (300 rounds)\n"
                                     "   ~ M1911: 7 magazines (49 rounds)\nCost: 1 gold bar\n\n"
                                     "= Loadout 2 =\n+ 12-Guage Shotgun\n+ .357 Revolver\n+ Stab proof vest\n"
                                     "+ Bandolier\n+ Ammunition:\n   ~ Shotgun: 24 shells\n   ~ .357 Revolver: 36 rounds\n"
                                     "Cost: 40 gold coins (0.4 gold bar)\n\nBuy your loadout:\nLoadout 1 (1)\nLoadout 2 (2)")
    if (choice == 1):
        choiceLoadout1()
    elif (choice == 2):
        choiceLoadout2()
    else:
        choicegun()

def choiceLoadout1():
    messagebox.showinfo("Loadout 1",
                        "You buy Loadout 1 for 1 gold bar. You have 4 bars remaining.")
    choice = simpledialog.askinteger("Choice",
                                      "After you checkout your supplies, you contemplate on whether to kill\n"
                                      "the store owner and the guards to take over the supply shop. Do you\n"
                                      "wish to carry an attack or proceed towards the city?\n\nTake over the store (1)\n"
                                      "Exit the store and continue walking to the city (2)")
    if (choice == 1):
        messagebox.showinfo("Take Over (Loadout 1)",
                            "You attack the shop owner as soon as you get your gear.\n"
                            "Stabbing him in the neck, you load your AR-15 and proceed\n"
                            "to eliminate the rest of the guards, gaining control of the shop.")
        choiceExplore()
    elif (choice == 2):
        ChefFarewell()
    else:
        choiceAttack()
def choiceLoadout2():
    messagebox.showinfo("Loadout 2",
                        "You buy Loadout 2 for 40 gold coins. As you hand Chef\n"
                        "a gold bar, he gives you back 60 coins in change.")
    messagebox.showinfo("Money",
                        "You have 4 bars and 60 coins remaining.")
    choice = simpledialog.askinteger("Choice",
                                      "After you checkout your supplies, you contemplate on whether to kill\n"
                                      "the store owner and the guards to take over the supply shop. Do you\n"
                                      "wish to carry an attack or proceed towards the city?\n\nTake over the store (1)\n"
                                      "Exit the store and continue walking to the city (2)")
    if (choice == 1):
        messagebox.showinfo("Take Over (Loadout 2)",
                            "You load your shotgun with the provided buckshot shells, quickly\n"
                            "aiming and firing on Chef, instantly killing him. A guard swiftly shoots\n"
                            "you in the back with his handgun. You roll over and shoot both the guards.")
        messagebox.showinfo("Medical Aid",
                            "You feel extreme pain from the bullet, and you realize\n"
                            "that you need intensive medical aid to survive.")
        messagebox.showinfo("Medical Bot",
                            "You catch something in the corner of the room that seems to be a medical bot.")
        messagebox.showinfo("Medical Bot",
                            "You crawl over to it and onto the gurney. It\n"
                            "injects anesthetics into you as you get drowsy...")
        time.sleep(2)
        messagebox.showinfo("Awake",
                            "When you wake up it is bright outside.")
        choiceExplore()
    elif (choice == 2):
        ChefFarewell()
    else:
        choiceLoudout2()
    
def choiceExplore():
    messagebox.showinfo("Explore",
                        "You decide to explore the shop. After seeing through it completely,\n"
                        "you make a second pass down a flight of stairs that interested you.")
    messagebox.showinfo("Vault",
                        "You come across a partially open giant steel door. It appears to be a vault door.")
    choice = simpledialog.askinteger("Vault",
                                      "You enter the vault and find a huge stockpile of weapons in gun cases, and\n"
                                      "ammunition. There is also a small bedroom in here. The room seals from\n"
                                      "inside and has a small keypad on the outside. Do you wish to stay in the\n"
                                      "room, or leave?\n\nStay (1)\nLeave (2)")
    if (choice == 1):
        endingGold4()
    elif (choice == 2):
        choiceLeave()
    else:
        choiceExplore()
        
def choiceLeave():
    messagebox.showinfo("Leave",
                        "You choose to stock up on weapons and ammo, and exit the vault.")
    choice = simpledialog.askinteger("Mercs",
                                      "You leave the store and continue onto Amador city. While traveling,\n"
                                      "you find several mercenaries standing beside their dead employer,\n"
                                      "a caravaner. Do you hire them?\n\nYes (1)\nNo (2)")
    if (choice == 1):
        choiceHire()
    elif (choice == 2):
        endingGold5()                
    else:
        choiceLeave()
                            
def choiceHire():
    messagebox.showinfo("Hire",
                        "You choose to hire the mercs, despite their former employer\n"
                        "being dead. You ask them if they would be interested in work.")
    messagebox.showinfo("Hire",
                        "They agree and you give them 3 gold coins each.\n"
                        "You walk with them until you see a small city.")                  
    choice = simpledialog.askinteger("Amador City",
                                     "You choose to walk into the town with the mercs. You have talked\n"
                                     "about taking over for several days with them. Do you wish to take\n"
                                     "over?\n\nTake over Amador City (1)\nStay in the town peacefully (2)")
    if (choice == 1):
        endingGold7()
    elif (choice == 2):
        endingGold6()
    else:
        choiceHire()
                            
def endingGold4():
    messagebox.showinfo("Stay",
                        "You choose to stay inside the vault, sealing yourself in.")
    messagebox.showinfo("Sealed",
                        "You decide you need to go to the bathroom. As you start to head\n"
                        "out, you realize the door is sealed.. You stay in the vault for\n"
                        "several days with no water before you die of dehydration.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 10 of 13 endings. Ending Type: Death")
    restart()

def endingGold5():
    messagebox.showinfo("Wasted",
                        "One of the mercs hears the gold clinking in your bag. He\n"
                        "swiftly pulls out his shotgun, and blasts you. You are dead.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 11 of 13 endings. Ending Type: Death")
    restart()
                        
def endingGold6():
    messagebox.showinfo("Busted",
                        "A guard hears two of your mercs conversing about a possible plan at\n"
                        "the bar. The guard comes to your house and arrests you, taking you\n"
                        "to jail.")
    messagebox.showinfo("Starved",
                        "After a few weeks in jail, devoid of refreshments, you die of starvation.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 12 of 13 endings. Ending Type: Death")
    restart()
                        
def endingGold7():
    messagebox.showinfo("Take over",
                        "You plan to use your grand wealth to start campaigning in\n"
                        "the town... You manage to get most several hundred people\n"
                        "in the town behind your back, but not all of them.")
    messagebox.showinfo("Continued",
                        "You raid the armory, getting several Omega death lasers and several\n"
                        "plasma rifles. You give these to your highest generals, and distribute\n"
                        "normal guns to the people.")
    messagebox.showinfo("Continued",
                        "You decide to take over the town. You have\n"
                        "many of the guards on your side as well.")
    messagebox.showinfo("Continued",
                        "You go into the town center, blitzkreiging it. You manage to capture\n"
                        "several town leaders. You order them to be executed and buried in a\n"
                        "discreet location. Not without many casualties, the townspeople are\n"
                        "glad to be rid of them. You are unanimously elected the new leader.")
    messagebox.showinfo("Ending",
                        "You have reached Ending 13 of 13 endings. Ending Type: Best")
    restart()
                        
################ Steven's Functions #####################
def choiceMoney1():
    messagebox.showinfo("GG",
                        "Good news, you have $1,000,000 in paper money.")
    messagebox.showinfo("GG",
                        "Bad news, paper money means nothing in the apocalypse.")
    messagebox.showinfo("Plains",
                        "You walk into a dusty plain, and you can see\n"
                        "nothing. You have your giant bag of money;\n"
                        "however, you don't know what's ahead.")
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
                                      "asks what you are doing around here.\n\n"
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
                        "You say you are here for supplies. He asks\n"
                        "you what is in the bag over your shoulder.")
    messagebox.showinfo("Supplies",
                        "He searches your bag and comments on how\n"
                        "stupid you are for having paper money.")
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
                        "The Sheriff hands you a revolver known for\n"
                        "being used by Rangers. It is full loaded.")
    messagebox.showinfo("Revolver",
                        "He warns 'Careful...there's only six bullets in that.\n"
                        "Bullets are on low supply around here. If you ever find\n"
                        "some ammo lying around and want to sell it, go to\n"
                        "Joseph the gun store owner.")
    messagebox.showinfo("Takeout",
                        "You go to the house in the outskirts where\n"
                        "it says he is. You sneak in through the back,\n"
                        "crouching behind the counter.")
    messagebox.showinfo("Takeout",
                        "You pull out your gun, using the counter to help you\n"
                        "aim. You shoot him once.")
    messagebox.showinfo("Takeout",
                        "He falls over. You walk towards his limp form, shooting\n"
                        "him once more, eliminating your target. You search his\n"
                        "body and find ammo, but it's not for your gun.")
    messagebox.showinfo("Proof",
                        "You take his ring off and his necklace, as proof of your kill.")
    messagebox.showinfo("Proof",
                        "You walk back to the town, slightly shaken up. You present\n"
                        "the proof to the sheriff, who pays you one gold coin.")
    messagebox.showinfo("Joseph",
                        "You go to Joseph and he asks if you want to buy\n"
                        "more rounds for the Peacekeeper revolver. You\n"
                        "buy six more rounds, spending your gold coin.")
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
                        "You sell the rare sniper ammo, the .338\n"
                        "round. You obtain 10 coins from Joseph.")
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
                        "multiple papers and says he needs you to take down a\n"
                        "local gang in the area that is expanding in members.")
    messagebox.showinfo("Mission",
                        "They destroyed many towns with their 'Jet' (drug),\n"
                        "which is extremely addictive. You see that the bounty\n"
                        "is two gold bars, which is worth 200 gold coins.")
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
                        "Cesium gets into your body. Due to the high amount\n"
                        "of cesium, your muscles slowly deteriorate.")
    messagebox.showinfo("Death",
                        "You collapse. You die because of\n"
                        "the intense heat and radiation.")
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
                        "You say no and live the rest of your life\n"
                        "peacefully in a favela style shack.")
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
                        "You wire it to a car battery and a receiver, then squeeze\n"
                        "out and quickly sneak a few hundred feet away.")
    messagebox.showinfo("Chaos",
                        "You activate the detonator (a makeshift garage door opener),\n"
                        "causing the house to explode a lot more violently than you\n"
                        "expected. Debris flies everywhere as the house is enveloped\n"
                        "in engulfing flames. You must have struck a gas line...")
    messagebox.showinfo("Luxury",
                        "You go back to the town. The sheriff says, 'I could feel\n"
                        "that explosion from here! I thought you were killed...'")
    messagebox.showinfo("Luxury",
                        "'Well, good work. I have no more bounties at the moment.\n"
                        "Everything seems to be pretty calm in these parts, now\n"
                        "that we have a fierce peacekeeper.' He hands you two\n"
                        "gold bars, and you buy a nice place in town.")
    messagebox.showinfo("Ending",
                        "You reached Ending 5 of 13 endings. Ending Type: Great")
    restart()
    
def endingMoney6():
    messagebox.showinfo("Stealth",
                        "You sneak in, taking one out with a knife.")
    messagebox.showinfo("Stealth",
                        "Someone hears you. They snatch their rifle and\n"
                        "storm into the room you are in. He shoots you.")
    messagebox.showinfo("Stealth",
                        "The bullet connects with your left shoulder, wounding you.\n"
                        "You shoot him multiple times very quickly with your blowback.")
    messagebox.showinfo("Stealth",
                        "You move to the living room and annihilate\n"
                        "two with your revolver. You hear several in the\n"
                        "garage, sneaking in and hiding behind a bench.")
    messagebox.showinfo("Stealth",
                        "When you are sure they cannot see you, you fire\n"
                        "at the bench. Your bullets penetrate the bench\n"
                        "and leave tennis ball sized holes in their chests.")
    messagebox.showinfo("Stealth",
                        "You check the house a few more times and find nobody else.\n"
                        "Walking back into the garage, you find a stockpile of gold,\n"
                        "drugs, and ammunition. You take the gold and ammo.")
    messagebox.showinfo("Stealth",
                        "You find a medical bot in the corner. You switch it to\n"
                        "the bullet wound setting, and it puts you to sleep.")
    time.sleep(2)
    messagebox.showinfo("Gold",
                        "You wake up two hours later. Fully healed, you walk\n"
                        "back to the sheriff, carrying your loot with you\n"
                        "in a sack. He has somehow confirmed your kills.")
    messagebox.showinfo("Gold",
                        "He gives you the bounty of two gold bars and you\n"
                        "live outside the town, making your own fortress\n"
                        "with your gold and the help of the townspeople.")
    messagebox.showinfo("Ending",
                        "You reached Ending 6 of 13 endings. Ending Type: Second Best")
    restart()
    
################ Main #####################
intro()

root.destroy()
