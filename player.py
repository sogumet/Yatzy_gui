"""Modul player with class player"""
class Player:
    """Player class with score board"""
    def __init__(self, name):
        """ Initialize class """
        self.score = {"name": name, "1": "", "2": "", "3": "", "4": "",
        "5": "", "6": "", "sum": "", "bonus": "", "pair": "", "twoPair": "",
        "three": "", "four": "", "fullHouse": "", "small": "",
        "large": "", "chanse": "", "yatzy": "", "total": "", "hidden": 0 }

        self.count = 0  # counting saves

        self.used = []
