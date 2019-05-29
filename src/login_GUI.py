import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker,relationships
from ui_py.Login_UI import Ui_Form
#from src.loginSystem import LoginSystem
# class LoginArea(QWidget):
#     def __init__(self):
#         QWidget.__init__(self,None)
#         # self.loginControl = LoginSystem()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#         self.ui.reg_b.clicked.connect(self.register)



import ui_py.Login_UI
import src.Company_Reg_GUI
import src.User_Reg_GUI

class Login_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Login_UI.Ui_Form()
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
        self.__comp_ui = src.Company_Reg_GUI.Company_GUI() ##
        self.__comp_ui.show()

    def openUser_Reg_UI(self):
        self.__user_ui = src.User_Reg_GUI.User_GUI() ##
        self.__user_ui.show()

    def checkInput(self,usr,psd):
        self.usr = usr
        self.psd = psd

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login_GUI()
    w.show()

    sys.exit(app.exec_())

