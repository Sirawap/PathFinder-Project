import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import Company_Registeration

class Company_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.user_ui = Company_Registeration.Ui_Form()
        self.user_ui.setupUi(self)



