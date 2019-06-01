import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.User_main_screen
import src.User_Profile_GUI
import src.EditUser_Profile_GUI
import src.login_GUI
from src.mainSystem import MainSystem

class User_Main_GUI(QMainWindow):
    def __init__(self,user):
        QMainWindow.__init__(self,None)

        self.user_ui = ui_py.User_main_screen.Ui_MainWindow()
        self.user_ui.setupUi(self)
        self.mainUser = user
        self.mainControl = MainSystem()
        self.user_ui.actionLog_Out.triggered.connect(self.logOut)
        self.user_ui.actionEdit_Profile.triggered.connect(self.openEditProfile)
        self.user_ui.actionView_Profile.triggered.connect(self.openViewProfile)
        self.user_ui.pushButton_commit_sen_method.clicked.connect(self.listJob)
        self.allEdu = self.mainControl.getAllEdu(self.mainUser)
        self.allJob = None

    def logOut(self):
        self.login_ui = src.login_GUI.Login_GUI()
        self.login_ui.show()
        self.close()

    def openEditProfile(self):
        self.userE_P_ui = src.EditUser_Profile_GUI.Edit_User_Profile_GUI(self.mainUser)
        self.userE_P_ui.show()

    def openViewProfile(self):
        self.userV_P_ui = src.User_Profile_GUI.View_User_Profile_GUI(self.mainUser)
        self.userV_P_ui.show()

    def listJob(self):

        if self.user_ui.radioButton_Show_all.isChecked():
            self.allJob = self.mainControl.getAllJobUser()

        self.addTable()
        return


    def addTable(self, column_size=6, header=['Company', 'Job Name',"Field", 'Position', 'Salary','Background Education']):
         self.user_ui.tableWidget.setColumnWidth(3, 200)  ### ADDED BY BILL FOR DESCRIPTION COLUMN SIZE
         self.user_ui.tableWidget.setColumnCount(column_size)
         self.user_ui.tableWidget.setRowCount(len(self.allJob))
         self.user_ui.tableWidget.setHorizontalHeaderLabels(header)

         for i in range(len(self.allJob)):
             for j in range(column_size):
                 self.user_ui.tableWidget.setItem(i, j, QTableWidgetItem(self.allJob[i][j]))


    def openView_Sended_Job_Request(self):
        pass

    def openView_Reply_Tray(self):
        pass
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv);
#     w = User_Main_GUI()
#     w.show()
#
#     sys.exit(app.exec_())
