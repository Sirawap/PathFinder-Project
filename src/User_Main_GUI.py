import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_main_screen

class User_Main_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.user_ui = ui_py.User_main_screen.Ui_Form()
        self.user_ui.setupUi(self)



