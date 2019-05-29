import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_main_screen

class Comp_Main_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.ui = ui_py.User_main_screen.Ui_MainWindow()
        self.ui.setupUi(self)



