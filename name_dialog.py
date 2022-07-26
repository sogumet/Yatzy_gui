"""Module name_dialog with class NameDialog"""
from PyQt6 import  uic
from PyQt6.QtWidgets import QDialog

class NameDialog(QDialog):
    """Class NameDialog"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(("nameDialog.ui"), self)
