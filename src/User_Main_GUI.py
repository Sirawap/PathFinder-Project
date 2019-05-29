import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_main_screen
import src.login_GUI

class User_Main_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.user_ui = ui_py.User_main_screen.Ui_MainWindow()
        self.user_ui.setupUi(self)

        self.user_ui.actionLog_Out.triggered.connect(self.logOut)

    def logOut(self):
        self.login_ui = src.login_GUI.Login_GUI()
        self.login_ui.show()
        self.close()

    def openEditProfile(self):
        self.userE_P_ui = src.EditComp_Profile_GUI.Edit_Company_Profile_GUI()
        self.userE_P_ui.show()

    def openViewProfile(self):
        self.userV_P_ui = src.Company_Profile_GUI.Edit_Company_Profile_GUI()
        self.userV_P_ui.show()
