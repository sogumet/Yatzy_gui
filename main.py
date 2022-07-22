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

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        basedir = os.path.dirname(__file__)
        uic.loadUi(os.path.join(basedir, "dicetest.ui"), self)
        self.button1_is_checked = False
        self.button2_is_checked = False
        self.button3_is_checked = False
        self.button4_is_checked = False
        self.button5_is_checked = False
        self.button1.clicked.connect( lambda checked: self.button_clicked(checked, "1"))
        self.button2.clicked.connect( lambda checked: self.button_clicked(checked, "2"))
        self.button3.clicked.connect( lambda checked: self.button_clicked(checked, "3"))
        self.button4.clicked.connect( lambda checked: self.button_clicked(checked, "4"))
        self.button5.clicked.connect( lambda checked: self.button_clicked(checked, "5"))
        self.dices = ""

    def start_timer(self, count=7, interval=100):
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
        
    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])

    def button_clicked(self, checked, button):
        """Button handler"""
        if button == "1":
            self.button1_is_checked = checked
            self.dice_control(self.button1_is_checked, button, self.button1)
        if button == "2":
            self.button2_is_checked = checked
            self.dice_control(self.button2_is_checked, button, self.button2)
        if button == "3":
            self.button3_is_checked = checked
            self.dice_control(self.button3_is_checked, button, self.button3)
        if button == "4":
            self.button4_is_checked = checked
            self.dice_control(self.button4_is_checked, button, self.button4)
        if button == "5":
            self.button5_is_checked = checked
            self.dice_control(self.button5_is_checked, button, self.button5)
    
    
    def dice_control(self, checked, dice, button):
        """Dice controller"""
        if checked:
            self.hold_dice(dice)
            button.setText("Holding")
            return
        self.unhold_dice(dice)
        button.setText("Hold")

app = QApplication(sys.argv)
window = MainWindow()
window.pusher.pressed.connect(window.start_timer)
window.show()
app.exec()
