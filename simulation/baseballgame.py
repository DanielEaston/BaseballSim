class Game():
    def __init__(self, homeTeam, awayTeam):
        self.homeScore = 0
        self.awayScore = 0
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.awayPositionInOrder = 1
        self.homePositionInOrder = 1
        self.inning = 1
        self.inningBottom = False
        self.first = []
        self.second = []
        self.third = []
        self.outs = 0
        
    
    def play(self):
        while not self.isGameOver():
            self.playInning()
            self.isGameOver()
            
    
    def playInning(self):
        while self.outs < 3:
            if self.inningBottom:
                self.playAtBat(self.homeTeam.players[self.homePositionInOrder-1])
            else:
                self.playAtBat(self.awayTeam.players[self.awayPositionInOrder-1])

        if self.inningBottom:
            self.inningBottom = False
            self.inning = self.inning + 1
        else:
            self.inningBottom = True
    
    def playAtBat(self, player):
        import numpy.random as random
        if random.random() <= 0.25:
            self.updateBases(1, player)
    
    def getPlayersOnBase(self):
        playersOnBase = []
        playersOnBase.extend(self.third)
        playersOnBase.extend(self.second)
        playersOnBase.extend(self.first)

    def updateBases(self, hit, player):
        playersOnBase = self.getPlayersOnBase()
        if self.inningBottom:
            self.homeScore = self.homeScore + len(playersOnBase[0:hit])
        else:
            self.awayScore = self.awayScore + len(playersOnBase[0:hit])
        




    def isGameOver(self):
        if self.inning >= 9 and self.inningBottom and self.homeScore != self.awayScore:
            self.gameOver = True

class Player():
    def __init__(self, name):
        self.name = name
        self.battingAverage = 0
        self.hits = 0

class Team():
    def __init__(self, name, players):
        self.name = name
        self.players = players