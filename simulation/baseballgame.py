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
        self.bases = [0,0,0]
        self.outs = 0
        
    
    def play(self):
        
        while not self.isGameOver():
            self.playInning()
            
            
    
    def playInning(self):
        print("Inning: "+str(self.inning))
        print("Score: "+str(self.homeScore)+"-"+str(self.awayScore))
        while self.outs < 3:
            if self.inningBottom:
                self.playAtBat(self.homeTeam.lineup[self.homePositionInOrder-1])
                if self.homePositionInOrder == 9:
                    self.homePositionInOrder = 1
                else:
                    self.homePositionInOrder = self.homePositionInOrder+1
            else:
                self.playAtBat(self.awayTeam.lineup[self.awayPositionInOrder-1])
                if self.awayPositionInOrder == 9:
                    self.awayPositionInOrder = 1
                else:
                    self.awayPositionInOrder = self.awayPositionInOrder+1

        
        if self.inningBottom:
            self.inningBottom = False
            self.inning = self.inning + 1
        else:
            self.inningBottom = True
        self.bases = [0,0,0]
        self.outs = 0
    
    def playAtBat(self, player):
        import numpy.random as random
        print(player+" batting")
        if random.random() <= 0.5:
            self.updateBases(2, player)
            print("Hit")
            print(self.bases)
            print("Score: "+str(self.homeScore)+"-"+str(self.awayScore))
        else:
            self.outs = self.outs+1
            print("Out")
            print(self.bases)
            print("Score: "+str(self.homeScore)+"-"+str(self.awayScore))
    
    

    def updateBases(self, hit, player):
        
        if hit == 4:
            if self.inningBottom:
                self.homeScore = self.homeScore + sum(self.bases) + 1
            else:
                self.awayScore = self.awayScore + sum(self.bases) + 1
        
        if self.inningBottom:
            self.homeScore = self.homeScore + sum(self.bases[0-hit:])
        else:
            self.awayScore = self.awayScore + sum(self.bases[0-hit:])
        
        for i in range(-1,-4,-1):
            if hit == 4:
                self.bases = [0,0,0]
            elif i - hit >= -3:
                self.bases[i] = self.bases[i-hit]
            else:
                self.bases[hit-1] = 1
                for j in range(hit-1):
                    self.bases[j]=0
                break
        




    def isGameOver(self):
        if self.inning >= 9 and self.inningBottom:
            return True
        else:
            return False


class Team():
    def __init__(self, name, playerNames):
        self.name = name
        self.players = {}
        self.lineup = playerNames
        i=1
        for name in playerNames:
            self.players[name] = {"hits":0, "positionInOrder":i}
            i=i+1