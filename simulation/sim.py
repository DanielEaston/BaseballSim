def run():
    from .baseballgame import Game
    
    from .baseballgame import Team

    philliesLineup = ["Odubel", "Jean", "JT", "Bryce", "Rhys", "Andrew", "Ronald", "Alec", "Zack"]
    metsLineup = ["Jeff", "Francisco", "Brad", "Dominic", "James", "Kevin", "Luis", "Albert", "Jacob"]

    phillies = Team("Phillies", philliesLineup)
    mets = Team("Mets", metsLineup)

    newGame = Game(phillies, mets)

    newGame.play()