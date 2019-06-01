import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Edit_Create_User_Profile
from src.mainSystem import MainSystem

class Edit_User_Profile_GUI(QWidget):
    def __init__(self,mainUser):
        QWidget.__init__(self,None)
        self.ui = ui_py.Edit_Create_User_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.mainUser = mainUser
        self.mainControl = MainSystem()
        #self.ui.pushButton_confirm_profile.clicked.connect(self.confirm)
        self.ui.lineEdit_name.setText(self.mainUser.fname)
        self.ui.lineEdit_name_2.setText(self.mainUser.surname)
        self.ui.lineEdit_name_3.setText(self.mainUser.email)
        self.ui.lineEdit_name_4.setText(self.mainUser.age)
        self.ui.lineEdit_userTel.setText(self.mainUser.tel)
        self.allEdu = self.mainControl.getAllEdu(self.mainUser)
        print(self.allEdu)
        self.clickedRow = 0
        self.clickedColumn = 0
        self.addTable() ######edited by bill
        self.ui.pushButton.clicked.connect(self.addEdu)
        self.ui.pushButton_confirm_profile.clicked.connect(self.confirm)
        self.ui.tableWidget.cellClicked.connect(self.itemClicked)######edited by bill
        self.ui.del_button.clicked.connect(self.deleteEducation)
        self.ui.backButton.clicked.connect(self.cancel)
    def confirm(self): ######edited method name by bill
        name = self.ui.lineEdit_name.text()
        surname = self.ui.lineEdit_name_2.text()
        age = self.ui.lineEdit_name_4.text()
        tel = self.ui.lineEdit_userTel.text()
        email = self.ui.lineEdit_name_3.text()



        self.mainControl.editUserProfile(self.mainUser,name,surname,age,tel,email)

        print("F for reespect")


        self.close() ##close after confirm
    def addEdu(self):
        degree = self.ui.comboBox_degree.currentText()
        field = self.ui.comboBox_subject.currentText()
        major = self.ui.lineEdit_major.text()
        uni = self.ui.lineEdit_university.text()

        self.mainControl.addUserEducation(self.mainUser, field, degree, major, uni)


    def cancel(self):
        self.close()

    ######edited by bill
    def addTable(self,column_size = 4,header = ['Field','Degree','Major','Uni']):
        self.ui.tableWidget.setColumnCount(column_size)
        self.ui.tableWidget.setRowCount(len(self.allEdu))
        self.ui.tableWidget.setHorizontalHeaderLabels(header)

        for i in range(len(self.allEdu)):
            for j in range(column_size):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(self.allEdu[i][j]))

    def itemClicked(self,row,column):######edited by bill
        self.clickedColumn = column
        self.clickedRow = row

    def deleteEducation(self):######edited by bill

        field = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()
        degree =self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),1).text()
        self.mainControl.deleteEdu(self.mainUser,field,degree)
        self.ui.tableWidget.removeRow(self.clickedRow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_User_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
