"""Module play with class Play"""
from dice import Hand


class Play:
    """Class play with methods to manage the roll, and the players turn"""
    game_counter = 0
    counter = 0
    scoreList = []              #list with scoreobject
    hand = Hand()
   

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
        return dices
       