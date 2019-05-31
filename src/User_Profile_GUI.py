import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_View_profile_UI
import src.Jobseeker

class View_User_Profile_GUI(QWidget):
    def __init__(self,usr = src.Jobseeker.Jobseeker()):
        QWidget.__init__(self,None)

        self.ui = ui_py.User_View_profile_UI.Ui_Form()
        self.ui.setupUi(self)

        self.usr = usr
        self.ui.label_Firstname.setText(self.usr.fname)
        self.ui.label_Surname.setText(self.usr.surname)
        # self.ui.frame_experience
        self.ui.label_home.setText(self.usr.surname)
        self.ui.label_mail.setText(self.usr.surname)
        self.ui.label_tel.setText(self.usr.surname)
        self.ui.label_12.setText(self.usr.surname)
        self.ui.label_13.setText(self.usr.surname)
