import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_main_screen
import src.login_GUI
import src.Company_Profile_GUI
import src.EditComp_Profile_GUI
import src.Post_New_Job
import src.View_job_detail_GUI

from src.mainSystem import MainSystem

class Comp_Main_GUI(QMainWindow):
    def __init__(self,mainCompany):
        QMainWindow.__init__(self,None)

        self.comp_ui = ui_py.Company_main_screen.Ui_MainWindow()
        self.comp_ui.setupUi(self)
        self.mainControl = MainSystem()
        self.mainCompany = mainCompany
        self.comp_ui.actionLog_Out.triggered.connect(self.logOut)
        self.comp_ui.actionEdit_Profile.triggered.connect(self.openEditProfile)
        self.comp_ui.actionView_Profile.triggered.connect(self.openViewProfile)
        self.comp_ui.actionPost_Job.triggered.connect(self.openPostJob)
        self.comp_ui.pushButton_delete_job.clicked.connect(self.deleteJob)

        self.comp_ui.pushButton_refuresh.clicked.connect(self.refresh)
        self.comp_ui.pushButton_interest.clicked.connect(self.reqInterest)
        self.comp_ui.pushButton_not_interest.clicked.connect(self.reqNotIn)
        self.comp_ui.tableWidget.doubleClicked.connect(self.viewJobDetail)
        self.allJob =  self.mainControl.getAllJob(self.mainCompany)
        self.allReq = self.mainControl.getAllRequestCompany(self.mainCompany)

        self.addTable()
        self.addReqTable()

    def logOut(self):
        self.login_ui = src.login_GUI.Login_GUI()
        self.login_ui.show()
        self.close()

    def openEditProfile(self):
        self.compE_P_ui = src.EditComp_Profile_GUI.Edit_Company_Profile_GUI(self.mainCompany)

        self.compE_P_ui.show()

    def openViewProfile(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        self.compV_P_ui = src.Company_Profile_GUI.View_Company_Profile_GUI(self.mainCompany)
        self.compV_P_ui.show()

    def openPostJob(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        self.post_job_ui = src.Post_New_Job.Post_New_Job(self.mainCompany)
        self.post_job_ui.show()


    # def openRecivedJobOffer(self):
    #     self.viewReply_ui = src.View_All_recived_job_offer_GUI.View_All_Reply()
    #     self.viewReply_ui.show()
    def deleteJob(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        jobname = self.comp_ui.tableWidget.item(self.comp_ui.tableWidget.currentRow(),0).text()
        print(jobname)
        self.mainControl.deleteJob(self.mainCompany,jobname)
        self.comp_ui.tableWidget.removeRow(self.comp_ui.tableWidget.currentRow())

    def addTable(self, column_size=4, header=['Job Name', 'Position', 'Salary', 'description']):
        style = "::section {""background-color: gray; }" ##set header color
        self.comp_ui.tableWidget.horizontalHeader().setStyleSheet(style)


        self.comp_ui.tableWidget.setColumnWidth(3,200) ### ADDED BY BILL FOR DESCRIPTION COLUMN SIZE
        self.comp_ui.tableWidget.setColumnCount(column_size)
        self.comp_ui.tableWidget.setRowCount(len(self.allJob))
        self.comp_ui.tableWidget.setHorizontalHeaderLabels(header)

        for i in range(len(self.allJob)):
            for j in range(column_size):
                self.comp_ui.tableWidget.setItem(i, j, QTableWidgetItem(self.allJob[i][j]))
    def refresh(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        self.allReq = self.mainControl.getAllRequestCompany(self.mainCompany)
        self.addReqTable()

    def reqInterest(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        fname = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(), 1).text()
        username = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(), 2).text()
        jobName = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(),3).text()
        self.mainControl.acceptReq(self.mainCompany,fname,username,jobName)
        self.addReqTable()

    def reqNotIn(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        fname = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(), 1).text()
        username = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(), 2).text()
        jobName = self.comp_ui.tableWidget_request_from_jobseeker.item(self.comp_ui.tableWidget_request_from_jobseeker.currentRow(),3).text()
        self.mainControl.declineReq(self.mainCompany,fname,username,jobName)
        self.addReqTable()

    def addReqTable(self, column_size=5, header=['Company', 'Name',"Username", "Job Name", 'Status']):
        style = "::section {""background-color: lightblue; }"  ##set header color
        self.comp_ui.tableWidget_request_from_jobseeker.horizontalHeader().setStyleSheet(style)

        self.comp_ui.tableWidget_request_from_jobseeker.setColumnWidth(3, 200)  ### ADDED BY BILL FOR DESCRIPTION COLUMN SIZE
        self.comp_ui.tableWidget_request_from_jobseeker.setColumnCount(column_size)
        self.comp_ui.tableWidget_request_from_jobseeker.setRowCount(len(self.allReq))
        self.comp_ui.tableWidget_request_from_jobseeker.setHorizontalHeaderLabels(header)

        for i in range(len(self.allReq)):
            for j in range(column_size):
                self.comp_ui.tableWidget_request_from_jobseeker.setItem(i, j, QTableWidgetItem(self.allReq[i][j]))

    def viewJobDetail(self):
        self.mainCompany = self.mainControl.reloadCompany(self.mainCompany)
        jobName = self.comp_ui.tableWidget.item(self.comp_ui.tableWidget.currentRow(), 0).text()
        job = self.mainControl.getJobDetail(self.mainCompany,jobName)
        print(job)

        self.job_detail_ui = src.View_job_detail_GUI.View_Job_detail_GUI(job)
        self.job_detail_ui.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv);
#     w = Comp_Main_GUI()
#     w.show()
#
#     sys.exit(app.exec_())
