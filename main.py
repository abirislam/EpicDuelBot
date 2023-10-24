import pyautogui
import time
import keyboard
import stats

def useSkillSelf(skill):
    pyautogui.click(skill)
    pyautogui.click(534, 446)
    time.sleep(5)

def useSkillEnemy(skill):
    pyautogui.click(skill)
    time.sleep(0.5)
    pyautogui.click(408, 547)
    pyautogui.click(540, 446)
    time.sleep(5)

def checkForDefaultExit():
    defaultExit = pyautogui.locateOnScreen('icons/defaultexiticon.png', confidence=0.8)

    if defaultExit != None:
        pyautogui.click(defaultExit)

def checkForExitButton(button):
    menuButtons = pyautogui.locateOnScreen('icons/menubuttons.png', confidence=0.8)

    for position in button:
        if menuButtons == None:
            pyautogui.click(position)
            checkForDefaultExit()
        else:
            return False
        

# Search for a match first
def searchForBattle(searching):
    juggIcon = pyautogui.locateOnScreen('icons/juggernaut.png', confidence=0.7)
    if juggIcon != None:
        for x in range(4):
            pyautogui.click(juggIcon)
        searching = True
        time.sleep(0.5)
    else:
        time.sleep(0.5)
    return searching
    
def searchingCheck(searching):
    searchIcon = pyautogui.locateOnScreen('icons/searching.png', confidence=0.9)
    if searchIcon:
        time.sleep(5)
        searching = True
    else:
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
    strike = pyautogui.locateOnScreen('skills/strike.png', confidence=0.8, region=(201, 387, 1516, 583))
    energyparasite = pyautogui.locateOnScreen('skills/energyparasite.png', confidence=0.8, region=(201, 387, 1516, 583))

    # all icons
    # player = pyautogui.locateOnScreen('icons/player.png', confidence=0.8)
    victory = pyautogui.locateOnScreen('icons/victory.png', confidence=0.8)
    defeat = pyautogui.locateOnScreen('icons/defeat.png', confidence=0.8)
    myTurn = pyautogui.locateOnScreen('icons/myturn.png', confidence=0.9)
    battleDrop = pyautogui.locateOnScreen('icons/battledrop.png', confidence=0.8)
    
    if myTurn:
        if reflex != None:
            useSkillSelf(reflex)
        elif plasma != None:
            useSkillEnemy(plasma)
        elif botspecial != None:
            useSkillEnemy(botspecial)
        elif energyparasite != None:
            useSkillEnemy(energyparasite)
        elif maelstrom != None:
            useSkillEnemy(maelstrom)
        elif strike != None:
            useSkillEnemy(strike)

    if battleDrop:
        pyautogui.click(battleDrop)

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
    exitbutton4 = pyautogui.locateAllOnScreen('icons/exiticon4.png', confidence=0.55, grayscale=True)

    if checkForExitButton(exitbutton) == False:
        exitStatus = False
        return exitStatus
    elif checkForExitButton(exitbutton2) == False:
        exitStatus = False
        return exitStatus
    elif checkForExitButton(exitbutton3) == False:
        exitStatus = False
        return exitStatus
    elif checkForExitButton(exitbutton4) == False:
        exitStatus = False
        return exitStatus
    else:
        exit

def checkForMiniWarIcons():
    miniWarIcon = pyautogui.locateOnScreen('icons/miniwartarget1.png', confidence=0.7)
    miniWarIcon2 = pyautogui.locateOnScreen('icons/miniwartarget2.png', confidence=0.7)
    miniWarIcon3 = pyautogui.locateOnScreen('icons/miniwartarget3.png', confidence=0.7)

    if miniWarIcon != None:
        pyautogui.click(miniWarIcon)
    elif miniWarIcon2 != None:
        pyautogui.click(miniWarIcon2)
    elif miniWarIcon3 != None:
        pyautogui.click(miniWarIcon3)

def warBombDrop():
    warTarget = pyautogui.locateOnScreen('icons/wartarget.png', confidence=0.7)
    warTarget2 = pyautogui.locateOnScreen('icons/wartarget2.png', confidence=0.7)
    warTarget3 = pyautogui.locateOnScreen('icons/wartarget3.png', confidence=0.7)
    warBomb = pyautogui.locateOnScreen('icons/warbomb.png', confidence=0.7)
    warIcon = pyautogui.locateOnScreen('icons/waricon.png', confidence=0.7)

    if warTarget != None:
        pyautogui.click(warTarget)
        time.sleep(1)
        pyautogui.click(warBomb)
    elif warTarget2 != None:
        pyautogui.click(warTarget2)
        time.sleep(1)
        pyautogui.click(warBomb)
    elif warTarget3 != None:
        pyautogui.click(warTarget3)
        time.sleep(1)
        pyautogui.click(warBomb)
    else:
        checkForDefaultExit()
        pyautogui.click(warIcon)
        time.sleep(1)
        checkForMiniWarIcons()
        time.sleep(1)
        warBombDrop()


def main():
    myStats = stats.Stats(0, 0)
    searchingStatus = False
    battlingStatus = False
    exitStatus = False

    while keyboard.is_pressed('q') == False:

        if not searchingStatus:
            searchForBattle(searchingStatus)

        searchingStatus = True

        while searchingCheck(searchingStatus):
            pass

        battlingStatus = True

        while battling(battlingStatus, myStats):
            time.sleep(1)

        exitStatus = True

        while exitting(exitStatus):
            pass

        searchingStatus = False

        time.sleep(3)

        warBombDrop()

if __name__ == "__main__":
    main()
