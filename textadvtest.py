import time
import sys

def main():
    #STATS
    strengthstat=0
    intstat=0
    agilitystat=0
    bowdmg=0
    meleedmg=0
    magicdmg=0
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
        print("The instructions are simple. You will be one of three characters on an adventure. What you do is up to you, but there are only so many commands that I, the computer, can understand. These include: attack, dodge, hide, eat, fight, run, talk, search, burn, kill, check inventory, and a few more.\n\n\n\n")
    print"Welcome,",firstname,lastname,"."
    classrestart=1
    while classrestart==1 and foolcount<=4:
        classchoicein=raw_input("What class will you be? Warrior, Mage, or Rogue? ")
        classchoice=classchoicein.upper()
        if classchoice=="WARRIOR":
            charclass=classchoice
            classrestart=0
            strengthstat+=5
            intstat+=1
            agilitystat+=1
            meleedmg+=2
        elif classchoice=="MAGE":
            charclass=classchoice
            classrestart=0
            intstat+=5
            strengthstat+=1
            agilitystat+=1
            magicdmg+=2
        elif classchoice=="ROGUE":
            charclass=classchoice
            classrestart=0
            agilitystat+=5
            strengthstat+=1
            intstat+=1
            bowdmg+=2
        else:
            foolcount=foolcount+1
            print"That is not a valid choice.\nPick one of the three listed."
    if foolcount==5:
        charclass="FOOL"
        print"Because you can't listen, you are now the Soiled Fool."
    if charclass != "null":
        print"You are now a",charclass,"\nYour stats are as follows:","\nSTRENGTH:",strengthstat,"\nINTELLIGENCE:",intstat,"\nAGILITY:",agilitystat,"\nBOW DAMAGE:",bowdmg,"\nMELEE DAMAGE:",meleedmg,"\nMAGIC DAMAGE:",magicdmg
    print"\nTHE ADVENTURE BEGINS\n"
    while askagain==0:
        action=raw_input("You are in a large clearing, surrounded by woods. You cannnot see very far into the trees. What do? ")
        action1=action.upper()
        if action1=="CHECK INVENTORY":
            print"You've got:"
            for item in inventory:
                print item
        elif action1=="HIDE":
            print"You hide behind a rock, until you realize there's nothing to hide from."
        elif action1=="RUN":
            print"You run north. You soon end up in another equally-sized clearing."
        elif action1=="SEARCH":
            print"You look around and find a small chest of various items. You take all of it."
        else:
            print"I dont know what you said. Try something else."
main()


# print"\nYour stats are as follows:","\nSTRENGTH:",strengthstat,"\nINTELLIGENCE:",intstat,"\nAGILITY:",agilitystat,"\nBOW DAMAGE:",bowdmg,"\nMELEE DAMAGE:",meleedmg,"\nMAGIC DAMAGE:",magicdmg
