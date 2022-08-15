"""Module play with class Play"""
from dice import Hand
from save_score import SaveScore
from player import Player


class Play:
    """Class play with methods to manage the roll, and the players turn"""
    game_counter = 0
    counter = 0
    activ_player_counter = 0
    player_list = []              #list with player object
    hand = Hand()
    save = SaveScore
    numb_of_player = 0

    def player(self, name):
        """Calling player to make player object"""
        player = Player(name)
        self.player_list.append(player)
        return player            # to show the name on gui

    def active_player(self):
        """Activ player"""
        if self.activ_player_counter == self.numb_of_player:
            self.activ_player_counter = 0
        player = self.player_list[self.activ_player_counter]
        return player


    def roll(self, choise):
        "Rolling dices"
        dices = []
        all_dice = [0, 1, 2, 3, 4]
        for _ in choise:
            all_dice.remove(int(_)-1)
        for val in all_dice:
            self.hand.hand[val].roll()
        for val in self.hand.hand:
            dices.append(val.value - 1)
        self.counter += 1
        return dices

    def save_rools(self, choice, player):
        """Save method"""
        self.save(player, self.hand, choice) # init savescore
        self.counter = 0
        self.game_counter += 1
        player.count += 1

    def finish(self, player):
        "Calculating sum when game is finished"
        player.score["total"] = player.score["hidden"]
        if player.score["bonus"] != "":
            player.score["total"] += 50
