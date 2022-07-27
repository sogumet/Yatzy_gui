"""module main with class MainWindow"""
from ntpath import samefile
import os
import sys
import random

from PyQt6 import  uic
from PyQt6.QtCore import QTimer, QProcess
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from play import Play
from name_dialog import NameDialog, NumberOfPlayerDialog

class MainWindow(QMainWindow):
    """"Main class"""

    dice_grafhics = ["dice_one60", "dice_two60","dice_three60",
            "dice_four60","dice_five60","dice_six60"]
    
    

    play = Play()
    # player = play.player
    save_count = 0
    app = QApplication(sys.argv)
    player = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        basedir = os.path.dirname(__file__)
        uic.loadUi(os.path.join(basedir, "yatzy.ui"), self)
        self.name_dialog = NameDialog()
        self.number_of_player_dialog = NumberOfPlayerDialog()
        self.hold_button_list = [self.button1, self.button2, self.button3, self.button4,
            self.button5]
        self.names = {0: self.name_1, 1: self.name_2, 2: self.name_3, 3: self.name_4}
        self.one = {0: self.one_1, 1: self.one_2, 2: self.one_3, 3: self.one_4}
        self.two = {0: self.two_1, 1: self.two_2, 2: self.two_3, 3: self.two_4}
        self.sum = {0: self.sum_1, 1: self.sum_2, 2: self.sum_3, 3: self.sum_4}
        self.bonus = {0: self.bonus_1, 1: self.bonus_2, 2: self.bonus_3, 3: self.bonus_4}
        self.save_button_list = [self.saveOne, self.saveTwo, self.saveThree, self.saveFour,
            self.saveFive, self.saveOne, self.saveSix, self.savePair, self.saveTwoPair,
            self.saveThreeOf, self.saveFourOf,self.saveFull, self.saveSmall, self.saveBig,
            self.saveChanse, self.saveYatzy]
        self.roll.pressed.connect(self.start_timer)
        self.start.clicked.connect(self.restart)
        self.button1.clicked.connect(lambda : self.hold_button_clicked("1"))
        self.button2.clicked.connect(lambda : self.hold_button_clicked("2"))
        self.button3.clicked.connect(lambda : self.hold_button_clicked("3"))
        self.button4.clicked.connect(lambda : self.hold_button_clicked("4"))
        self.button5.clicked.connect(lambda : self.hold_button_clicked("5"))
        self.saveOne.clicked.connect(lambda : self.save_as("1", self.one[self.play.activ_player_counter], self.saveOne, self.player))
        self.saveTwo.clicked.connect(lambda : self.save_as("2", self.two[self.play.activ_player_counter], self.saveTwo, self.player))
        # self.saveThree.clicked.connect(lambda : self.save_as("3", self.three,self.saveThree))
        # self.saveFour.clicked.connect(lambda : self.save_as("4", self.four, self.saveFour))
        # self.saveFive.clicked.connect(lambda : self.save_as("5", self.five, self.saveFive))
        # self.saveSix.clicked.connect(lambda : self.save_as("6", self.six, self.saveSix))
        # self.savePair.clicked.connect(lambda : self.save_as("pair", self.pair, self.savePair))
        # self.saveTwoPair.clicked.connect(lambda : self.save_as("twoPair", self.twoPair,
            # self.saveTwoPair))
        # self.saveThreeOf.clicked.connect(lambda : self.save_as("three", self.threeOf,
            # self.saveThreeOf))
        # self.saveFourOf.clicked.connect(lambda : self.save_as("four", self.fourOf, self.saveFourOf))
        # self.saveFull.clicked.connect(lambda : self.save_as("fullHouse", self.full, self.saveFull))
        # self.saveSmall.clicked.connect(lambda : self.save_as("small", self.small, self.saveSmall))
        # self.saveBig.clicked.connect(lambda : self.save_as("large", self.big, self.saveBig))
        # self.saveChanse.clicked.connect(lambda : self.save_as("chanse", self.chanse,
            # self.saveChanse))
        # self.saveYatzy.clicked.connect(lambda : self.save_as("yatzy", self.yatzy, self.saveYatzy))
        self.name_dialog.dialogOk.clicked.connect(self.ok_clicked)
        self.dices = ""
        self.show()
        self.game_prepare()
        self.app.exec()
        
        
    
    def game_prepare(self):
        """Game start"""
        self.number_of_player_dialog.exec()
        self.play.numb_of_player = self.number_of_player_dialog.numberOfPlayer.value()
        print("Number of player: ", self.play.numb_of_player)
        for x in range(self.play.numb_of_player):
            number = str(x+1)
            self.name_dialog.label.setText(f"Enter name of player {number}:")
            self.name_dialog.nameEdit.setText("")
            self.name_dialog.exec()
            self.player = self.play.player(self.name_dialog.nameEdit.text())
            self.names[x].setText(self.player.score["name"])
        self.player = self.play.active_player()     #start player
            

    def ok_clicked(self):
        """Dialog name ok clicked"""
        

    def restart(self):
        """Restart"""
        self.app.quit()
        status = QProcess.startDetached(sys.executable, sys.argv)
        print(status)

    def save_as(self, save_as, value, button, player):
        """Saving player and resetting buttons"""
        self.button_handler_save(button, player)
        self.play.save_rools(save_as, player)
        value.setText(str(player.score[save_as]))
        self.sum[self.play.activ_player_counter].setText(str(player.score["sum"]))
        self.bonus[self.play.activ_player_counter].setText(str(player.score["bonus"]))
        if player.count == 15:
            self.play.finish(player)
            self.total.setText(str(player.score["total"]))
            self.roll.setEnabled(False)
        self.play.activ_player_counter += 1
        self.player = self.play.active_player()
        

    def button_handler_save(self, button, player):
        """Button handler when save is clicked"""
        player.used.append(button)
        for button in self.hold_button_list:
            if button.isChecked():
                button.click()
            button.setEnabled(False)
        for button in self.save_button_list:
            button.setEnabled(False)
        self.roll.setEnabled(True)

    def button_handler_roll(self, player):
        """Button handler after roll is clicked"""
        for button in self.save_button_list:
            button.setEnabled(True)
        for button in player.used:
            button.setEnabled(False)
        for button in self.hold_button_list:
            button.setEnabled(True)
        if self.play.counter == 3:
            for button in self.hold_button_list:
                if button.isChecked():
                    button.click()
                button.setEnabled(False)
                self.roll.setEnabled(False)

    def start_timer(self, count=7, interval=100):
        """Start timer"""
        if self.play.counter < 3:
            timer = QTimer()
            counter = 0
            timer.start(interval)
            def handler():
                nonlocal counter
                counter += 1
                if counter >= count:
                    timer.stop()
                    timer.deleteLater()
                    self.set_dices(self.player)
                    print(self.dices)
            timer.timeout.connect(self.update_faces)
            timer.timeout.connect(handler)
        else: print("Save")

    def update_faces(self):
        """Update label"""
        if self.button1.isChecked() is False:
            self.faces1()
        if self.button2.isChecked() is False:
            self.faces2()
        if self.button3.isChecked() is False:
            self.faces3()
        if self.button4.isChecked() is False:
            self.faces4()
        if self.button5.isChecked() is False:
            self.faces5()

    def faces1(self):
        """Show dice 1"""
        self.dice1.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces2(self):
        """Show dice 2"""
        self.dice2.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces3(self):
        """Show dice 3"""
        self.dice3.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces4(self):
        """Show dice 4"""
        self.dice4.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces5(self):
        """Show dice 5"""
        self.dice5.setPixmap(QPixmap(random.choice(self.dice_grafhics)))


    def set_dices(self, player):
        """Set dices"""
        dices = self.play.roll(self.dices)
        self.dice1.setPixmap(QPixmap(self.dice_grafhics[dices[0]]))
        self.dice2.setPixmap(QPixmap(self.dice_grafhics[dices[1]]))
        self.dice3.setPixmap(QPixmap(self.dice_grafhics[dices[2]]))
        self.dice4.setPixmap(QPixmap(self.dice_grafhics[dices[3]]))
        self.dice5.setPixmap(QPixmap(self.dice_grafhics[dices[4]]))
        self.button_handler_roll(player)

    def hold_dice(self, dice):
        """Dices to hold"""
        self.dices = self.dices + dice

    def unhold_dice(self, dice):
        """Dices to unhold"""
        self.dices = self.dices.replace(dice, "")

    def hold_button_clicked(self, button):
        """Button handler"""
        if button == "1":
            self.dice_control(self.button1.isChecked(), button, self.button1)
        if button == "2":
            self.dice_control(self.button2.isChecked(), button, self.button2)
        if button == "3":
            self.dice_control(self.button3.isChecked(), button, self.button3)
        if button == "4":
            self.dice_control(self.button4.isChecked(), button, self.button4)
        if button == "5":
            self.dice_control(self.button5.isChecked(), button, self.button5)


    def dice_control(self, checked, dice_number, button):
        """Dice controller"""
        if checked:
            self.hold_dice(dice_number)
            button.setText("Holding")
            return
        self.unhold_dice(dice_number)
        button.setText("Hold")

if __name__ == "__main__":
    MainWindow()
