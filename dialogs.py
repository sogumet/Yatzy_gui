"""Module name_dialog with class NameDialog"""
from PyQt6.QtWidgets import QDialog, QMessageBox
from nameDialogUi import Ui_Dialog
from numberOfPlayerDialogUi import Ui_DialogNumbers

class NameDialog(QDialog, Ui_Dialog):
    """Class NameDialog"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # uic.loadUi(("nameDialog.ui"), self)
        self.setWindowTitle("Names")

class NumberOfPlayerDialog(QDialog, Ui_DialogNumbers):
    """Class Number of player dialog"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # uic.loadUi(("numberOfPlayerDialog.ui"), self)
        self.setupUi(self)
        self.setWindowTitle("Players")

class HelpDialog(QDialog):
    """Class Help dialog"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")

    def help(self):
        """Help message"""
        mess = QMessageBox
        mess.information(
            self,
            "Help",
            "1. Press start to begin play\n"
            "2. Enter number of player\n"
            "3. Enter the names of the players\n"
            "4. Press roll to roll the dices\n"
            "5. To hold the dices use buttons or key 1-5\n"
            "6. Press the save button where you want to save your score,\n"
            "   if the score is not valid you will get a stroke.\n"
            "7. The game will automaticly calculate the bonus and total score.",
            buttons=QMessageBox.StandardButton.Close
            
        )
class AboutDialog(QDialog):
    """Class About dialog"""

    def help(self):
        """About message"""
        mess = QMessageBox
        mess.information(
            self,
            "About",
            "Yatzy version 1.0.0 2022\n"
            "Created by Kent Sjöberg",
            buttons=QMessageBox.StandardButton.Close
            
        )
