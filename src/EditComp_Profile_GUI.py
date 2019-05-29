import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Edit_Profile2

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Company_Edit_Profile2.Ui_Form()
        self.ui.setupUi(self)
