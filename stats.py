class CurrentSession:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.totalRounds = 0

    def calculateAverage(self):
        totalBattles = self.wins + self.losses
        newTotal = self.currentRounds / (totalBattles + 1)
        print("Average # of Rounds: " + str(newTotal))

    def viewStats(self):
        print("Total Wins: " + str(self.wins))
        print("Total Losses: " + str(self.losses))
        print("Current Winrate: " + str((self.wins / (self.wins + self.losses)) * 100) + "%")
        print("Average # of Rounds: " + str(self.totalRounds / (self.wins + self.losses)))
