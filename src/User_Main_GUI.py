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
        self.user_ui.pushButton_sendRequest.clicked.connect(self.sendRequest)
        self.user_ui.pushButton_refresh.clicked.connect(self.refresh)
        self.allEdu = self.mainControl.getAllEdu(self.mainUser)
        self.allJob = None
        self.allReq = self.mainControl.getAllRequestUser(self.mainUser)
        self.addReqTable()

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
        elif self.user_ui.radioButton_search__keyword.isChecked():
            compname = self.user_ui.lineEdit_comapnyName.text()
            position = self.user_ui.lineEdit_position.text()
            minSalary = float(self.user_ui.lineEdit_salary.text()) if self.user_ui.lineEdit_salary.text() != "" else ""
            if compname == "" and position == "" and minSalary == "":
                return
            self.allJob = self.mainControl.getKeywordJobUser(compname,position,minSalary)
        elif self.user_ui.radioButton_search_user_profile.isChecked():
            self.allJob = self.mainControl.getRecommendJobUser(self.mainUser)
        else:
            return

        self.addTable()
        return
    def sendRequest(self):

        companyName = self.user_ui.tableWidget.item(self.user_ui.tableWidget.currentRow(),0).text()
        jobName = self.user_ui.tableWidget.item(self.user_ui.tableWidget.currentRow(),2).text()
        self.mainControl.sendRequest(self.mainUser,companyName,jobName)
        self.allReq = self.mainControl.getAllRequestUser(self.mainUser)



    def refresh(self):
        self.allReq = self.mainControl.getAllRequestUser(self.mainUser)
        self.addReqTable()

    def addTable(self, column_size=6, header=['Company', 'Job Name',"Field", 'Position', 'Salary','Background Education']):
         self.user_ui.tableWidget.setColumnWidth(3, 200)  ### ADDED BY BILL FOR DESCRIPTION COLUMN SIZE
         style = "::section {""background-color: gray;" \
                "color: red; }"
         self.user_ui.tableWidget.horizontalHeader().setStyleSheet(style)
         self.user_ui.tableWidget.setColumnCount(column_size)
         self.user_ui.tableWidget.setRowCount(len(self.allJob))
         self.user_ui.tableWidget.setHorizontalHeaderLabels(header)
         print(self.allJob)

         for i in range(len(self.allJob)):
             for j in range(column_size):
                 self.user_ui.tableWidget.setItem(i, j, QTableWidgetItem(self.allJob[i][j]))

    def addReqTable(self, column_size=4,header=['Company', 'Name', "Job Name", 'Status']):
        self.user_ui.tableWidget_requested_job.setColumnWidth(3, 200)  ### ADDED BY BILL FOR DESCRIPTION COLUMN SIZE
        style = "::section {""background-color: gray;" \
                    "color: red; }"
        self.user_ui.tableWidget_requested_job.horizontalHeader().setStyleSheet(style)
        self.user_ui.tableWidget_requested_job.setColumnCount(column_size)
        self.user_ui.tableWidget_requested_job.setRowCount(len(self.allReq))
        self.user_ui.tableWidget_requested_job.setHorizontalHeaderLabels(header)
        print(self.allReq)

        for i in range(len(self.allReq)):
            for j in range(column_size):
                self.user_ui.tableWidget_requested_job.setItem(i, j, QTableWidgetItem(self.allReq[i][j]))



#
# if __name__ == '__main__':
#     app = QApplication(sys.argv);
#     w = User_Main_GUI()
#     w.show()
#
#     sys.exit(app.exec_())
