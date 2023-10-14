import pyautogui
import time
import keyboard
import stats

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

def checkForExitButton(button):
    menuButtons = pyautogui.locateOnScreen('icons/menubuttons.png', confidence=0.8)
    defaultExit = pyautogui.locateOnScreen('icons/defaultexiticon.png', confidence=0.8)

    for position in button:
        if menuButtons == None:
            pyautogui.click(position)
            time.sleep(0.5)
            if defaultExit != None:
                pyautogui.click(defaultExit)
                time.sleep(0.5)
        else:
            return False


# Search for a match first
def searchForBattle(searching):
    juggIcon = pyautogui.locateOnScreen('icons/juggernaut.png', confidence=0.7)
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
def battling(battleStatus, myStats):
    # 1516 x 583, 201, 387
    # skill variables
    botspecial = pyautogui.locateOnScreen('skills/botspecial.png', confidence=0.8, region=(201, 387, 1516, 583))
    maelstrom = pyautogui.locateOnScreen('skills/maelstrom.png', confidence=0.85, region=(201, 387, 1516, 583))
    plasma = pyautogui.locateOnScreen('skills/plasmacannon.png', confidence=0.8, region=(201, 387, 1516, 583))
    reflex = pyautogui.locateOnScreen('skills/reflexboost.png', confidence=0.7, region=(201, 387, 1516, 583))
    strike = pyautogui.locateOnScreen('skills/strike.png', confidence=0.6, region=(201, 387, 1516, 583))
    energyparasite = pyautogui.locateOnScreen('skills/energyparasite.png', confidence=0.8, region=(201, 387, 1516, 583))


    # all icons
    # player = pyautogui.locateOnScreen('icons/player.png', confidence=0.8)
    victory = pyautogui.locateOnScreen('icons/victory.png', confidence=0.8)
    defeat = pyautogui.locateOnScreen('icons/defeat.png', confidence=0.8)
    myTurn = pyautogui.locateOnScreen('icons/myturn.png', confidence=0.9)
    battleDrop = pyautogui.locateOnScreen('icons/battledrop.png', confidence=0.8)
    
    if myTurn:
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

    if battleDrop:
        pyautogui.click(battleDrop)
        print("Claimed battle drop")

    if victory:
        myStats.wins += 1
        myStats.viewStats()
        battleStatus = False
    elif defeat:
        myStats.losses += 1
        myStats.viewStats()
        battleStatus = False
    else:
        battleStatus = True
    
    return battleStatus


# Look for the x icons 
def exitting(exitStatus):
    exitbutton = pyautogui.locateAllOnScreen('icons/exiticon1.png', confidence=0.55, grayscale=True)
    exitbutton2 = pyautogui.locateAllOnScreen('icons/exiticon2.png', confidence=0.55, grayscale=True)
    exitbutton3 = pyautogui.locateAllOnScreen('icons/exiticon3.png', confidence=0.55, grayscale=True)

    if checkForExitButton(exitbutton) == False:
        print("Found exit button and exited")
        exitStatus = False
        return exitStatus
    elif checkForExitButton(exitbutton2) == False:
        print("Found exit button and exited")
        exitStatus = False
        return exitStatus
    elif checkForExitButton(exitbutton3) == False:
        print("Found exit button and exited")
        exitStatus = False
        return exitStatus
    else:
        print("Couldn't find exit button, terminating")
        exit


def main():
    myStats = stats.Stats(0, 0)
    searchingStatus = False
    battlingStatus = False
    exitStatus = False

    while keyboard.is_pressed('q') == False:

        # if not searchingStatus:
        #     searchForBattle(searchingStatus)

        # searchingStatus = True

        # while searchingCheck(searchingStatus):
        #     print("Searching for a battle still")

        # battlingStatus = True

        # print("Starting battle")

        # while battling(battlingStatus, myStats):
        #     print("Still opponent's turn")
        #     time.sleep(1)

        # print("Exitting battle now")

        exitStatus = True

        while exitting(exitStatus):
            print("Trying to exit")

        searchingStatus = False

if __name__ == "__main__":
    main()
