class Game():
    def __init__(self, homeTeam, awayTeam):
        self.homeScore = 0
        self.awayScore = 0
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.inning = 1
        self.inningBottom = False
        self.first = []
        self.second = []
        self.third = []
        self.gameOver = False
    
    def play(self):
        while not self.gameOver:
            print("The Game Started")
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