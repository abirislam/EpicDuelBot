# EpicDuel Juggernaut Bot for Blood Mage by Blade
# This bot assumes a full tech build;
# Max Bloodlust, Max Energy Parasite, 5 in Maelstrom, 3 in Reflex Boost
# Also assumes ED to be full screen on the primary window
# You must also change the player.png to your player.


import pyautogui
import time
import keyboard


def useSkillSelf(skill):
    pyautogui.click(skill)
    pyautogui.click(534, 446)
    time.sleep(7)

def useSkillEnemy(skill):
    pyautogui.click(skill)
    time.sleep(0.5)
    pyautogui.click(408, 547)
    pyautogui.click(534, 446)
    time.sleep(7)


# Search for a match first
def searchForBattle(searching):
    juggIcon = pyautogui.locateOnScreen('icons/juggernaut.png', confidence=0.8)
    if juggIcon != None:
        print("Starting Juggernaut Mode")
        pyautogui.click(juggIcon)
        searching = True
        time.sleep(0.5)
    else:
        print("Juggernaut icon not found")
        time.sleep(0.5)
    return searching
    
def searchingCheck(searching):
    searchIcon = pyautogui.locateOnScreen('icons/searching.png', confidence=0.9)
    if searchIcon:
        time.sleep(10)
        searching = True
    else:
        print("Found a battle")
        searching = False

    return searching



# Check if its our turn, use a skill, wait
# Always targets left enemy first
def battling(battleStatus, wins, losses):
    print("Beginning battle phase")

    # 1516 x 583, 201, 387
    # skill variables
    botspecial = pyautogui.locateOnScreen('skills/botspecial.png', confidence=0.8, region=(201, 387, 1516, 583))
    maelstrom = pyautogui.locateOnScreen('skills/maelstrom.png', confidence=0.8, region=(201, 387, 1516, 583))
    plasma = pyautogui.locateOnScreen('skills/plasmacannon.png', confidence=0.8, region=(201, 387, 1516, 583))
    reflex = pyautogui.locateOnScreen('skills/reflexboost.png', confidence=0.7, region=(201, 387, 1516, 583))
    strike = pyautogui.locateOnScreen('skills/strike.png', confidence=0.6, region=(201, 387, 1516, 583))
    energyparasite = pyautogui.locateOnScreen('skills/energyparasite.png', confidence=0.8, region=(201, 387, 1516, 583))


    # all icons
    player = pyautogui.locateOnScreen('icons/player.png', confidence=0.8)
    victory = pyautogui.locateOnScreen('icons/victory.png', confidence=0.8)
    defeat = pyautogui.locateOnScreen('icons/defeat.png', confidence=0.8)
    myturn = pyautogui.locateOnScreen('icons/myturn.png', confidence=0.85)
    
    if myturn:
        print("Watashi no turn, draw")
        if reflex != None:
            print("Using skill reflex")
            useSkillSelf(reflex)
        elif plasma != None:
            print("Using skill plasma cannon")
            useSkillEnemy(plasma)
        elif botspecial != None:
            print("Using skill bot special")
            useSkillEnemy(botspecial)
        elif energyparasite != None:
            print("Using energy parasite")
            useSkillEnemy(energyparasite)
        elif maelstrom != None:
            print("Using skill maelstrom")
            useSkillEnemy(maelstrom)
        elif strike != None:
            print("Using skill basic strike")
            useSkillEnemy(strike)

    if victory:
        wins += 1
        print("Wins: " + str(wins))
        battleStatus = False
    elif defeat:
        losses += 1
        print("Losses: " + str(losses))
        battleStatus = False
    else:
        battleStatus = True
    
    return battleStatus


# Look for the x icons 
def exitting(exitStatus):
    juggIcon = pyautogui.locateOnScreen('icons/juggernaut.png', confidence=0.8)
    exitbutton = pyautogui.locateAllOnScreen('icons/exiticon1.png', confidence=0.55, grayscale=True)
    for position in exitbutton:
        pyautogui.click(position)

    if juggIcon != None:
        print("Jugg icon found")
        exitStatus = False
        return exitStatus

    exitbutton2 = pyautogui.locateAllOnScreen('icons/exiticon2.png', confidence=0.55, grayscale=True)
    for position2 in exitbutton2:
        pyautogui.click(position2)
    if juggIcon != None:
        print("Jugg icon found")
        exitStatus = False
        return exitStatus

    exitbutton3 = pyautogui.locateAllOnScreen('icons/exiticon3.png', confidence=0.55, grayscale=True)
    for position3 in exitbutton3:
        pyautogui.click(position3)
    if juggIcon != None:
        print("Jugg icon found")
        exitStatus = False
        return exitStatus

    exitStatus = False
    return exitStatus

def main():
    wins = 0
    losses = 0
    searchingStatus = False
    battlingStatus = False
    exitStatus = False

    while keyboard.is_pressed('q') == False:

        if not searchingStatus:
            searchForBattle(searchingStatus)

        searchingStatus = True

        while searchingCheck(searchingStatus):
            print("Searching for a battle still")

        battlingStatus = True

        while battling(battlingStatus, wins, losses):
            print("Still battling")

        print("Exitting battle now")

        exitStatus = True

        while exitting(exitStatus):
            print("Trying to exit")

        searchingStatus = False

if __name__ == "__main__":
    main()
