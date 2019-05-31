import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Edit_Profile

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = ui_py.Company_Edit_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_confirm_profile.clicked.connect(self.user_edit)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_Company_Profile_GUI()
    w.show()
    sys.exit(app.exec_())