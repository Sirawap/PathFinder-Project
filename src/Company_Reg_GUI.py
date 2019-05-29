import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Registeration

class Company_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Company_Registeration.Ui_Form()
        self.ui.setupUi(self)



