import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import Login_UI
import temp_company_GUI
import temp_User_GUI

class Login_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = Login_UI.Ui_Form()
        self.ui.setupUi(self)
        self.usr = ''
        self.psd = ''

        self.ui.reg_b.clicked.connect(self.checkRadio)

    def checkRadio(self):
        self.checkInput(self.ui.username.text(),self.ui.password.text())
        if(self.ui.radioButton.isChecked() == True):
            self.openUser_Reg_UI()
        elif(self.ui.radioButton_2.isChecked() == True):
            self.openCompany_Reg_UI()
    def openCompany_Reg_UI(self):
        self.__comp_ui = temp_company_GUI.Company_GUI() ##
        self.__comp_ui.show()

    def openUser_Reg_UI(self):
        self.__user_ui = temp_User_GUI.User_GUI() ##
        self.__user_ui.show()

    def checkInput(self,usr,psd):
        self.usr = usr
        self.psd = psd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login_GUI()
    w.show()

    sys.exit(app.exec_())