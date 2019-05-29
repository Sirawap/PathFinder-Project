import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_View_profile_UI

class View_User_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.User_View_profile_UI.Ui_Form()
        self.ui.setupUi(self)
