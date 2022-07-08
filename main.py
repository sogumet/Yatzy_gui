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
    faces = {"1": "window.dice1.setPixmap"}
    play = Play()

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        basedir = os.path.dirname(__file__)
        uic.loadUi(os.path.join(basedir, "dicetest.ui"), self)
        self.button1_is_checked = False
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.toggled1)
        self.button2_is_checked = False
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.toggled2)
        self.button3_is_checked = False
        self.button3.setCheckable(True)
        self.button3.clicked.connect(self.toggled3)
        self.button4_is_checked = False
        self.button4.setCheckable(True)
        self.button4.clicked.connect(self.toggled4)
        self.button5_is_checked = False
        self.button5.setCheckable(True)
        self.button5.clicked.connect(self.toggled5)
        self.dices = ""

    def start_timer(self, count=5, interval=100):
        """Start timer"""
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

    def update_faces(self):
        """Update label"""
        if self.button1_is_checked is False:
            self.faces1()
        if self.button2_is_checked is False:
            self.faces2()
        if self.button3_is_checked is False:
            self.faces3()
        if self.button4_is_checked is False:
            self.faces4()
        if self.button5_is_checked is False:
            self.faces5()

    def faces1(self):
        window.dice1.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces2(self):
        window.dice2.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces3(self):
        window.dice3.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces4(self):
        window.dice4.setPixmap(QPixmap(random.choice(self.dice_grafhics)))

    def faces5(self):
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

    def toggled1(self, checked):
        """Toggled button1"""
        self.button1_is_checked = checked
        print(self.button1_is_checked)
        self.dice_control(self.button1_is_checked, "1")

    def toggled2(self, checked):
        """Toggled button2"""
        self.button2_is_checked = checked
        print(self.button2_is_checked)
        self.dice_control(self.button2_is_checked, "2")

    def toggled3(self, checked):
        """Toggled button3"""
        self.button3_is_checked = checked
        print(self.button3_is_checked)
        self.dice_control(self.button3_is_checked, "3")

    def toggled4(self, checked):
        """Toggled button4"""
        self.button4_is_checked = checked
        print(self.button4_is_checked)
        self.dice_control(self.button4_is_checked, "4")

    def toggled5(self, checked):
        """Toggled button5"""
        self.button5_is_checked = checked
        print(self.button5_is_checked)
        self.dice_control(self.button5_is_checked, "5")

    def dice_control(self, checked, dice):
        """Dice controller"""
        if checked:
            self.hold_dice(dice)
            return
        self.unhold_dice(dice)

app = QApplication(sys.argv)
window = MainWindow()
window.pusher.pressed.connect(window.start_timer)
window.show()
app.exec()
