import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import User_Registeration_UI

class User_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.user_ui = User_Registeration_UI.Ui_register_user()
        self.user_ui.setupUi(self)


