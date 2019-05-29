import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Edit_Create_User_Profile

class View_User_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Edit_Create_User_Profile.Ui_Form()
        self.ui.setupUi(self)
