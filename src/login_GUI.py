import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from src.loginSystem import LoginSystem
from src.Company import Company
from src.Jobseeker import Jobseeker
from src.accountClasses import CompanyAcc
from src.accountClasses import UserAcc
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker,relationship
# s
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
import src.Company_Main_UI
import src.User_Main_GUI

class Login_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Login_UI.Ui_Form()
        self.ui.setupUi(self)
        self.usr = ''
        self.psd = ''
        self.loginControl = LoginSystem()
        self.ui.reg_b.clicked.connect(self.checkRadioR)
        self.ui.login_b.clicked.connect(self.checkRadioM)

    def checkRadioR(self):
        self.checkInput(self.ui.username.text(),self.ui.password.text())
        if(self.ui.radioButton_2.isChecked() == True):
            self.openUser_Reg_UI()
        elif(self.ui.radioButton.isChecked() == True):
            self.openComp_Reg_UI()
    def checkRadioM(self):
        self.checkInput(self.ui.username.text(),self.ui.password.text())
        if(self.ui.radioButton_2.isChecked() == True):
            self.openUser_Main_UI()
        elif(self.ui.radioButton.isChecked() == True):
            self.openComp_Main_UI()

    def openComp_Reg_UI(self):
        self.__compR_ui = src.Company_Reg_GUI.Company_GUI() ##
        self.__compR_ui.show()

    def openUser_Reg_UI(self):
        self.__userR_ui = src.User_Reg_GUI.User_GUI() ##
        self.__userR_ui.show()

    def openComp_Main_UI(self):

        response = self.loginControl.loginCompany(self.ui.username.text(),self.ui.password.text())
        if type(response) == str :
            self.ui.error_label.setText(response)
            return
        else:
            self.__compM_ui = src.Company_Main_UI.Comp_Main_GUI(response) ##
            self.__compM_ui.show()
            self.close()

    def openUser_Main_UI(self):

        response = self.loginControl.loginUser(self.ui.username.text(),self.ui.password.text())
        if type(response) == str :
            self.ui.error_label.setText(response)
            return
        else:
            self.__userM_ui = src.User_Main_GUI.User_Main_GUI(response)  ##
            self.__userM_ui.show()
            self.close()

    def checkInput(self,usr,psd):
        unvalidInput = ["!","'","/",".","=","!"]
        if(type(usr) == str) and (type(psd) == str):
            for x in unvalidInput:
                if(x in usr) or (x in psd):
                    raise Exception
            self.usr = usr
            self.psd = psd


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = Login_GUI()
#     w.show()
#
#     sys.exit(app.exec_())

