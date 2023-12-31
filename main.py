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
    pyautogui.click(384, 738)
    pyautogui.click(540, 446)
    time.sleep(5)

def checkForDefaultExit():
    defaultExit = pyautogui.locateOnScreen('icons/defaultexiticon.png', confidence=0.8)
    if defaultExit != None:
        pyautogui.click(defaultExit)

def checkForPopupExit():
    popup = pyautogui.locateOnScreen('icons/popupexit.png', confidence=0.8)
    if popup != None:
        pyautogui.click(popup)

def checkForJuggIcon():
    juggIcon = pyautogui.locateOnScreen('icons/juggernaut.png', confidence=0.7)
    if juggIcon != None:
        return True

def checkForExitButton(button):
    for position in button:
        if checkForJuggIcon():
            return False
        else:
            pyautogui.click(position)
            checkForDefaultExit()
            checkForCancelButton()

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
    victory = pyautogui.locateOnScreen('icons/victory.png', confidence=0.8)
    defeat = pyautogui.locateOnScreen('icons/defeat.png', confidence=0.8)
    myTurn = pyautogui.locateOnScreen('icons/myturn.png', confidence=0.9)
    battleDrop = pyautogui.locateOnScreen('icons/battledrop.png', confidence=0.8)

    if myTurn:
        # edit build here
        myStats.totalRounds += 1
        reflex = pyautogui.locateOnScreen('skills/bh/reflex.png', confidence=0.85, region=(201, 387, 1516, 583))
        multi = pyautogui.locateOnScreen('skills/bh/multi.png', confidence=0.8, region=(201, 387, 1516, 583))
        engBooster = pyautogui.locateOnScreen('skills/engbooster.png', confidence=0.80, region=(201, 387, 1516, 583))
        sidearm = pyautogui.locateOnScreen('skills/sidearm.png', confidence=0.85, region=(201, 387, 1516, 583))
        strike = pyautogui.locateOnScreen('skills/strike.png', confidence=0.8, region=(201, 387, 1516, 583))

        if reflex != None:
            useSkillSelf(reflex)
        elif multi != None:
            useSkillEnemy(multi)
        elif sidearm != None:
            useSkillEnemy(sidearm)
        elif engBooster != None:
            useSkillEnemy(engBooster)
        elif strike != None:
            useSkillEnemy(strike)

    if battleDrop:
        pyautogui.click(battleDrop)

    checkForPopupExit()

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
    exitbutton5 = pyautogui.locateAllOnScreen('icons/exiticon5.png', confidence=0.55, grayscale=True)

    if checkForJuggIcon():
        exitStatus = False
        return exitStatus

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
    elif checkForExitButton(exitbutton5) == False:
        exitStatus = False
        return exitStatus
    else:
        exitStatus = False
        return exitStatus

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

def checkForCancelButton():
    cancel = pyautogui.locateOnScreen('icons/cancel.png', confidence=0.7)

    if cancel != None:
        pyautogui.click(cancel)

def useWarBomb(target):

    for x in range(10):
        pyautogui.click(target)
        time.sleep(0.5)
        warBomb = pyautogui.locateOnScreen('icons/warbomb.png', confidence=0.7)
        if warBomb != None:
            pyautogui.click(warBomb)
            time.sleep(1)
            checkForDefaultExit()
            checkForCancelButton()
        else:
            checkForDefaultExit()
            checkForCancelButton()

def dropAllWarBombs():
    warTarget = pyautogui.locateOnScreen('icons/wartarget.png', confidence=0.7)
    warTarget2 = pyautogui.locateOnScreen('icons/wartarget2.png', confidence=0.7)
    warTarget3 = pyautogui.locateOnScreen('icons/wartarget3.png', confidence=0.7)
    warIcon = pyautogui.locateOnScreen('icons/waricon.png', confidence=0.7)

    checkForCancelButton()
    checkForDefaultExit()

    if warTarget != None:
        useWarBomb(warTarget)
    elif warTarget2 != None:
        useWarBomb(warTarget2)
    elif warTarget3 != None:
        useWarBomb(warTarget3)
    else:
        pyautogui.click(384, 738) # to see if current avatar is in front of war target
        time.sleep(2)
        checkForDefaultExit()
        checkForCancelButton()
        pyautogui.click(warIcon)
        time.sleep(1)
        checkForMiniWarIcons()
        time.sleep(1)
        dropAllWarBombs()

def main():
    myStats = stats.CurrentSession()
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

        checkForPopupExit()

        while exitting(exitStatus):
            pass

        searchingStatus = False

        time.sleep(3)

        checkForDefaultExit()
        checkForCancelButton()
        
        if (myStats.wins > 0) and (myStats.wins % 10 == 0):
            dropAllWarBombs()

        time.sleep(1)

if __name__ == "__main__":
    main()
