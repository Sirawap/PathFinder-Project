import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import Login_UI
import temp2
import temp3

class Login_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = Login_UI.Ui_Form()
        self.ui.setupUi(self)

        self.ui.login_b.clicked.connect(self.checkRadio)

    def checkRadio(self):
        if(self.ui.radioButton.isChecked() == True):
            self.openUser_UI()
        elif(self.ui.radioButton_2.isChecked() == True):
            self.openCompany_UI()
    def openCompany_UI(self):
        self.__comp_ui = temp3.Company_GUI()
        self.__comp_ui.show()

    def openUser_UI(self):
        self.__user_ui = temp2.User_GUI()
        self.__user_ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login_GUI()
    w.show()

    sys.exit(app.exec_())