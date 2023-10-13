class Stats:
    def __init__(self, wins, losses):
        self.wins = wins
        self.losses = losses

    def viewStats(self):
        print("Total Wins: " + str(self.wins))
        print("Total Losses: " + str(self.losses))
        print("Current Winrate: " + str((self.wins / (self.wins + self.losses)) * 100) + "%")
