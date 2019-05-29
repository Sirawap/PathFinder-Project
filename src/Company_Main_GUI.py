import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_main_screen

class User_Main_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.ui = ui_py.User_main_screen.Ui_Form()
        self.ui.setupUi(self)



