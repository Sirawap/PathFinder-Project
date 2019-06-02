import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_main_screen
import src.login_GUI
import src.Company_Profile_GUI
import src.EditComp_Profile_GUI
import src.Post_New_Job

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
        self.comp_ui.actionView_Recived_Job_Offer.triggered.connect(self.openRecivedJobOffer)
        self.allJob =  self.mainControl.getAllJob(self.mainCompany)
        #self.allRequest = self.mainControl.getAllRequest(self.mainCompany)

        self.addTable()

    def logOut(self):
        self.login_ui = src.login_GUI.Login_GUI()
        self.login_ui.show()
        self.close()

    def openEditProfile(self):
        self.compE_P_ui = src.EditComp_Profile_GUI.Edit_Company_Profile_GUI(self.mainCompany)
        self.compE_P_ui.show()

    def openViewProfile(self):
        self.compV_P_ui = src.Company_Profile_GUI.View_Company_Profile_GUI(self.mainCompany)
        self.compV_P_ui.show()

    def openPostJob(self):
        self.post_job_ui = src.Post_New_Job.Post_New_Job(self.mainCompany)
        self.post_job_ui.show()


    def openRecivedJobOffer(self):
        self.viewReply_ui = src.View_All_recived_job_offer_GUI.View_All_Reply()
        self.viewReply_ui.show()
    def deleteJob(self):

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

# if __name__ == '__main__':
#     app = QApplication(sys.argv);
#     w = Comp_Main_GUI()
#     w.show()
#
#     sys.exit(app.exec_())
