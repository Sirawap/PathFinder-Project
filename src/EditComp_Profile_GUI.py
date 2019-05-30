from PySide2.QtWidgets import *
import ui_py.Company_Edit_Profile

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Company_Edit_Profile.Ui_Form()
        self.ui.setupUi(self)
