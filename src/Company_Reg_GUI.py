import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Registeration
from src.loginSystem import LoginSystem
from src.Company import Company
from src.accountClasses import CompanyAcc

class Company_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.loginControl = LoginSystem()
        self.user_ui = ui_py.Company_Registeration.Ui_Form()
        self.user_ui.setupUi(self)

        self.user_ui.confirm_b.clicked.connect(self.com_reg)

    def com_reg(self):
        cname = self.user_ui.register_company_name.text()
        email = self.user_ui.register_email.text()
        tel = self.user_ui.register_tel.text()

        usr = self.user_ui.register_username.text()
        pwd = self.user_ui.register_password.text()
        rpwd = self.user_ui.register_rePassword.text()

        if cname == "" or email == "" or tel == "" or usr =="" or pwd == "" or rpwd =="":
            self.user_ui.error_label.setText("Please fill (*) info")
            return
        if pwd != rpwd:
            self.user_ui.error_label.setText("Passwords dont match!")
            return
        else:
            rettext = self.loginControl.createCompany(usr,pwd,cname,email,tel)
            self.user_ui.error_label.setText(rettext)

            self.close()  ##for close after click 'confirm' by bill
            return



