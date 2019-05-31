import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Edit_Create_User_Profile

class Edit_User_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = ui_py.Edit_Create_User_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_confirm_profile.clicked.connect(self.user_edit)

    def user_edit(self):
        name = self.ui.lineEdit_name.text()
        surname = self.ui.lineEdit_name_2.text()
        age = self.ui.lineEdit_name_4.text()
        tel = self.ui.lineEdit_userTel.text()
        email = self.ui.lineEdit_name_3.text()
        no = self.ui.lineEdit_houseNo.text()
        soi = self.ui.lineEdit_soi.text()
        street = self.ui.lineEdit_street.text()
        district = self.ui.lineEdit_district.text()
        city = self.ui.lineEdit_city.text()
        province = self.ui.lineEdit_state.text()
        zip = self.ui.lineEdit_zip.text()
        home_tel = self.ui.lineEdit_homeTel.text()
        degree = self.ui.comboBox_degree.currentText()
        subject = self.ui.comboBox_subject.currentText()
        langugage = self.ui.register_language.currentText()
        print("F for reespect")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_User_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
