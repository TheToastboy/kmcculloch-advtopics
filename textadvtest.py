import time
import sys

class Warrior():
    def __init__(self, classname, strengthstat, intstat, agilitystat, bowdmg, meleedmg, magicdmg):
        classname="Warrior"
        strengthstat=5
        intstat=1
        agilitystat=1
        bowdmg=0
        meleedmg=2
        magicdmg=0
class Mage():
    def __init__(self, classname, strengthstat, intstat, agilitystat, bowdmg, meleedmg, magicdmg):
        classname="Mage"
        strengthstat=1
        intstat=5
        agilitystat=1
        bowdmg=0
        meleedmg=0
        magicdmg=2
class Rogue():
    def __init__(self, classname, strengthstat, intstat, agilitystat, bowdmg, meleedmg, magicdmg):
        classname="Rogue"
        strengthstat=1
        intstat=1
        agilitystat=5
        bowdmg=2
        meleedmg=0
        magicdmg=0
class Fool():
    def __init__(self, classname, strengthstat, intstat, agilitystat, bowdmg, meleedmg, magicdmg):
        classname="Soiled Fool"
        strengthstat=0
        intstat=0
        agilitystat=0
        bowdmg=0
        meleedmg=0
        magicdmg=0

def main():
    #MISC
    foolcount=0
    charclass="null"
    askagain=0
    inventory=["string","dust"]
    totalmoney=0
    #GAME
    firstnamein=raw_input("Enter your first name: ")
    lastnamein=raw_input("Enter your last name: ")
    firstname=firstnamein.upper()
    lastname=lastnamein.upper()
    instdispin=""
    instdispin=raw_input("Would you like to view the instructions? ")
    instdispin=instdispin.upper()
    instdispin1=instdispin[0]
    if instdispin1=="N":
        print"okay.\n\n\n"
    else:
        print("The instructions are simple. You will be one of three characters on an adventure. What you do is up to you, but there are only so many commands that I, the computer, can understand. These include: attack, dodge, hide, eat, run, talk, look, burn, jump, get [item] and check inventory.\n\n\n\n")
    print"Welcome,",firstname,lastname,"."
    classrestart=1
    while classrestart==1 and foolcount<=4:
        classchoicein=raw_input("What class will you be? Warrior, Mage, or Rogue? ")
        classchoice=classchoicein.upper()
        if classchoice=="WARRIOR":
            charclass = Warrior()
            classrestart=0
        elif classchoice=="MAGE":
            charclass = Mage()
            classrestart=0
        elif classchoice=="ROGUE":
            charclass=classchoice
            classrestart=0
        else:
            foolcount=foolcount+1
            print"That is not a valid choice.\nPick one of the three listed."
    if foolcount==5:
        charclass = Fool()
        print"Because you can't listen, you are now the Soiled Fool."
    if charclass != "null":
        print"You are now a",charclass.classname,"\nYour stats are as follows:","\nSTRENGTH:",charclass.strengthstat,"\nINTELLIGENCE:",charclass.intstat,"\nAGILITY:",charclass.agilitystat,"\nBOW DAMAGE:",charclass.bowdmg,"\nMELEE DAMAGE:",charclass.meleedmg,"\nMAGIC DAMAGE:",charclass.magicdmg
    print"\nTHE ADVENTURE BEGINS\n"
    while askagain==0:
        action=raw_input("You are in a large clearing, surrounded by woods. You cannnot see very far into the trees. What do? ")
        action0=action.upper()
        actionwordlist=action0.split()
        print actionwordlist
        if action1=="CHECK INVENTORY":
            print"You've got:"
            for item in inventory:
                print item
        elif action1=="HIDE":
            print"You hide behind a rock, until you realize there's nothing to hide from."
        elif action1=="RUN":
            print"You run north. You soon end up in another equally-sized clearing."
        elif action1=="LOOK":
            print"You look around and find a small chest of various items. You take all of it."
        else:
            print"I dont know what you said. Try something else."
main()

"""
if action1=="CHECK INVENTORY":
    print"You've got:"
    for item in inventory:
        print item
elif action1=="ATTACK":
elif action1=="DODGE":
elif action1=="HIDE":
elif action1=="EAT":
elif action1=="RUN":
elif action1=="TALK":
elif action1=="LOOK":
elif action1=="BURN":
elif action1=="JUMP":
elif
else:
    print"I dont know what you said. Try something else."
"""
