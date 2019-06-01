import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import ui_py.temp2

class temp2(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.temp2.Ui_Form()
        self.ui.setupUi(self)

