from kiwoom.kiwoom import Kiwoom

import sys
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print("UI 클래스입니다.")
        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()

        self.app.exec_()