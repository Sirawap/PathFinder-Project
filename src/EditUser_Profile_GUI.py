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
        self.ui.pushButton_confirm_profile.clicked.connect(self.user_edit)
        self.ui.lineEdit_name.setText(self.mainUser.fname)
        self.ui.lineEdit_name_2.setText(self.mainUser.surname)
        self.ui.lineEdit_name_3.setText(self.mainUser.email)
        self.ui.lineEdit_name_4.setText(self.mainUser.age)
        self.ui.lineEdit_userTel.setText(self.mainUser.tel)

        self.clickedRow = 0
        self.clickedColumn = 0
        self.addTable() ######edited by bill

        self.ui.tableWidget.cellClicked.connect(self.itemClicked)######edited by bill

    def user_edit(self):
        name = self.ui.lineEdit_name.text()
        surname = self.ui.lineEdit_name_2.text()
        age = self.ui.lineEdit_name_4.text()
        tel = self.ui.lineEdit_userTel.text()
        email = self.ui.lineEdit_name_3.text()

        degree = self.ui.comboBox_degree.currentText()
        field = self.ui.comboBox_subject.currentText()
        major = self.ui.lineEdit_major.text()
        uni = self.ui.lineEdit_university.text()

        self.mainControl.editUserProfile(self.mainUser,name,surname,age,tel,email)
        self.mainControl.addUserEducation(self.mainUser,field,degree,major,uni)
        print("F for reespect")

    ######edited by bill
    def addTable(self,column_size = 5,row_size = 2,header = ['No','Name','Surname','age','tel'],data = [["1.","Bill",'n','20','069696969'],["2.","Jia",'S','20','09696969696']]):
        self.ui.tableWidget.setColumnCount(column_size)
        self.ui.tableWidget.setRowCount(row_size)
        self.ui.tableWidget.setHorizontalHeaderLabels(header)

        for i in range(row_size):
            for j in range(column_size):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(data[i][j]))

    def itemClicked(self,row,column):######edited by bill
        self.clickedColumn = column
        self.clickedRow = row

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_User_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
