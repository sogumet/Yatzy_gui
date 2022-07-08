import os
import sys
import random

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QTimer



basedir = os.path.dirname(__file__)

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi(os.path.join(basedir, "dicetest.ui"))
window.show()


def start_timer(count=5, interval=100):
    timer = QTimer()
    counter = 0
    timer.start(interval)
    def handler():
        nonlocal counter
        counter += 1
        # update_label()
        if counter >= count:
            timer.stop()
            # timer.deleteLater()
    timer.timeout.connect(update_label)       
    timer.timeout.connect(handler)
    

def update_label():

        n = random.randint(1, 6)
        window.labbel.setText(f"{n}")
        print("Hej")

window.pusher.pressed.connect(start_timer)


app.exec()

