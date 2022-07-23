"""module main with class MainWindow"""
import os
import sys
import random

from PyQt6 import  uic
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from play import Play

class MainWindow(QMainWindow):
    """"Main class"""

    dice_grafhics = ["dice_one60", "dice_two60","dice_three60",
            "dice_four60","dice_five60","dice_six60"]
    play = Play()
    score = play.player

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        basedir = os.path.dirname(__file__)
        uic.loadUi(os.path.join(basedir, "dicetest.ui"), self)
        self.button1.clicked.connect(lambda : self.button_clicked("1"))
        self.button2.clicked.connect(lambda : self.button_clicked("2"))
        self.button3.clicked.connect(lambda : self.button_clicked("3"))
        self.button4.clicked.connect(lambda : self.button_clicked("4"))
        self.button5.clicked.connect(lambda : self.button_clicked("5"))
        self.saveOne.clicked.connect(lambda : self.save_as("1", self.one))
        self.saveTwo.clicked.connect(lambda : self.save_as("2", self.two))
        self.saveThree.clicked.connect(lambda : self.save_as("3", self.three))
        self.saveFour.clicked.connect(lambda : self.save_as("4", self.four))
        self.saveFive.clicked.connect(lambda : self.save_as("5", self.five))
        self.saveSix.clicked.connect(lambda : self.save_as("6", self.six))

        self.dices = ""

    def save_as(self, save_as, value):
        """Saving score and reseting buttons"""
        self.play.save_rools(save_as)
        value.setNum(self.score.board[save_as])
        button_list = [self.button1, self.button2, self.button3, self.button4, self.button5]
        self.sum.setNum(self.score.board["sum"])
        for button in button_list:
            if button.isChecked():
                button.click()

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
                    self.set_dices()
                    print("Finish")
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
        window.dice1.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces2(self):
        """Show dice 2"""
        window.dice2.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces3(self):
        """Show dice 3"""
        window.dice3.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces4(self):
        """Show dice 4"""
        window.dice4.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces5(self):
        """Show dice 5"""
        window.dice5.setPixmap(QPixmap(random.choice(self.dice_grafhics)))


    def set_dices(self):
        """Set dices"""
        dices = self.play.roll(self.dices)
        window.dice1.setPixmap(QPixmap(self.dice_grafhics[dices[0]]))
        window.dice2.setPixmap(QPixmap(self.dice_grafhics[dices[1]]))
        window.dice3.setPixmap(QPixmap(self.dice_grafhics[dices[2]]))
        window.dice4.setPixmap(QPixmap(self.dice_grafhics[dices[3]]))
        window.dice5.setPixmap(QPixmap(self.dice_grafhics[dices[4]]))

    def hold_dice(self, dice):
        """Dices to hold"""
        self.dices = self.dices + dice

    def unhold_dice(self, dice):
        """Dices to unhold"""
        self.dices = self.dices.replace(dice, "")

    def button_clicked(self, button):
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

app = QApplication(sys.argv)
window = MainWindow()
window.pusher.pressed.connect(window.start_timer)
window.show()
app.exec()
