import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_View_profile_UI
import src.Jobseeker
from src.mainSystem import MainSystem
class View_User_Profile_GUI(QWidget):
    def __init__(self,usr):
        QWidget.__init__(self,None)

        self.ui = ui_py.User_View_profile_UI.Ui_Form()
        self.ui.setupUi(self)
        self.mainControl = MainSystem()
        self.usr = usr
        self.ui.label_Firstname.setText(self.usr.fname)
        self.ui.label_Surname.setText(self.usr.surname)
        # self.ui.frame_experience
        self.ui.label_home.setText(self.usr.surname)
        self.ui.label_mail.setText(self.usr.email)
        self.ui.label_tel.setText(self.usr.tel)
        self.ui.label_12.setText(self.usr.age)
        self.allEdu = self.mainControl.getAllEdu(self.usr)
        self.addTable()


    def addTable(self, column_size=4, header=['Field', 'Degree', 'Major', 'Uni']):
            self.ui.tableWidget_educatio_background.setColumnCount(column_size)
            self.ui.tableWidget_educatio_background.setRowCount(len(self.allEdu))
            self.ui.tableWidget_educatio_background.setHorizontalHeaderLabels(header)

            for i in range(len(self.allEdu)):
                for j in range(column_size):
                    self.ui.tableWidget_educatio_background.setItem(i, j, QTableWidgetItem(self.allEdu[i][j]))

