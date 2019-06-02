import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_Registeration_UI
from src.loginSystem import LoginSystem
from src.Jobseeker import Jobseeker
from src.accountClasses import UserAcc
class User_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.loginControl = LoginSystem()
        self.user_ui = ui_py.User_Registeration_UI.Ui_register_user()
        self.user_ui.setupUi(self)
        self.user_ui.confirm_b.clicked.connect(self.user_reg)

    def user_reg(self):
        usr = self.user_ui.register_user_2.text()
        pwd = self.user_ui.register_password.text()
        rpwd = self.user_ui.register_rePassword.text()
        fname = self.user_ui.register_firstname.text()
        surname = self.user_ui.register_surname.text()
        age = self.user_ui.register_age.text() if self.user_ui.register_age.text() != "" else None
        email = self.user_ui.register_email.text() if self.user_ui.register_email.text() != "" else None
        tel = self.user_ui.register_age.text() if self.user_ui.register_tel.text() != "" else None


        if fname == "" or surname == "" or usr =="" or pwd=="" or rpwd =="":
            self.user_ui.error_label.setText("Please fill (*) info")
            return


        if pwd != rpwd:
            self.user_ui.error_label.setText("Passwords dont match!")
            return
        else:
            rettext = self.loginControl.createUser(usr,pwd,fname,surname,age,email,tel)
            self.user_ui.error_label.setText(rettext)

            return




