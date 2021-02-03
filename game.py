
from player import Player

class Game:
    def __init__(self, player_names):

        self.landlords = []
        self.farmer_basicScore = 0
        self.landlords_basicScore = 0
        self.booms = 0
        self.player1 = Player(player_names[0])
        self.player2 = Player(player_names[1])
        self.player3 = Player(player_names[2])
        self.player4 = Player(player_names[3])
        self.player5 = Player(player_names[4])
        self.players = [self.player1, self.player2,
                        self.player3, self.player4, self.player5]

    def farmer_win(self):
        self.set_basicScore()
        total_score = self.farmer_basicScore * (2**self.booms)
        landlord_num = len(self.landlords)
        farmer_num = len(self.players) - landlord_num

        for player in self.players:
            if player.name in self.landlords:
                player.score = int(player.score - total_score * farmer_num / landlord_num)
            else:
                player.score = int(player.score + total_score)



    def landlord_win(self):
        self.set_basicScore()
        total_score = self.landlords_basicScore * (2**self.booms)
        landlord_num = len(self.landlords)
        farmer_num = len(self.players) - landlord_num

        for player in self.players:
            if player.name in self.landlords:
                player.score = int(player.score + total_score)
            else:
                player.score = int(player.score - total_score * landlord_num / farmer_num)



    def setLandlord(self, plyer_name):
        if plyer_name in self.landlords:
            self.landlords.remove(plyer_name)

        elif len(self.landlords) < 2:
            self.landlords.insert(0, plyer_name)

        else:
            self.landlords.pop()
            self.landlords.insert(0, plyer_name)


    def set_basicScore(self):

        if len(self.landlords) == 2:
            self.farmer_basicScore = 2
            self.landlords_basicScore = 3

        elif len(self.landlords) == 1:
            self.farmer_basicScore = 1
            self.landlords_basicScore = 4

        else:
            pass
