import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_main_screen

class Comp_Main_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.user_ui = ui_py.Company_main_screen.Ui_MainWindow()
        self.user_ui.setupUi(self)
