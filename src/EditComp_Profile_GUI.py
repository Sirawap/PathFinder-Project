from PySide2.QtWidgets import *
import ui_py.Company_Edit_Profile

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Company_Edit_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_OK.clicked.connect(self.commitChange)
        self.ui.pushButton_Cancle.clicked.connect(self.cancleChange)
        self.ui.pushButton.clicked.connect(self.chooseLogo)

    def commitChange(self):
        ##please add more
        self.close()

    def cancleChange(self):
        ##please add more
        self.close()

    def chooseLogo(selfself):
        ##please add more
        pass
