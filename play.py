"""Module play with class Play"""
from dice import Hand
from save_score import SaveScore
from score import Score


class Play:
    """Class play with methods to manage the roll, and the players turn"""
    game_counter = 0
    counter = 0
    scoreList = []              #list with scoreobject
    hand = Hand()
    save = SaveScore
    player = Score("Kent")

    def roll(self, choise):
        "Rolling dices"
        dices = []
        all_dice = [0, 1, 2, 3, 4]
        for _ in choise:
            all_dice.remove(int(_)-1)
        for val in all_dice:
            self.hand.hand[val].roll()
        for val in self.hand.hand:
            print(val.value, end=" ")
            dices.append(val.value - 1)
        self.counter += 1
        return dices
    

    def save_rools(self, choice):
        """Save method"""
        print("saving one")
        self.save(self.player, self.hand, choice) # init savescore
        self.counter = 0
        self.game_counter += 1
        self.player.count += 1

    def finish(self):
        "Calculating sum when game is finished"
        for player in self.scoreList:
            player.board["total"] = player.board["hidden"]
            if player.board["bonus"] != "":
                player.board["total"] += 50
        

       