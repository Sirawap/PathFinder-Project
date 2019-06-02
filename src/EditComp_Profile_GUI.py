import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Edit_Profile
from src.mainSystem import MainSystem

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self,company):
        QWidget.__init__(self,None)
        self.ui = ui_py.Company_Edit_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_updateCompany.clicked.connect(self.comp_edit)
        self.ui.pushButton_UpdateCompAdd.clicked.connect(self.addr_edit)
        self.mainCompany = company
        self.mainControl = MainSystem()
        self.ui.lineEdit_comp_name.setText(self.mainCompany.companyName)
        self.ui.lineEdit_tel.setText(self.mainCompany.tel)
        self.ui.lineEdit_web.setText(self.mainCompany.email)
        self.ui.pushButton_CancelCompAdd.clicked.connect(self.closed)

    def comp_edit(self):
        name = self.ui.lineEdit_comp_name.text()
        tel = self.ui.lineEdit_tel.text()
        mail = self.ui.lineEdit_web.text()
        business = self.ui.comboBox_Business.currentText()
        str = ''
        if name == '':
            str += "Please enter your company name\n"
            self.ui.error_label_prof.setText(str)
            return
        if tel == '' or mail == '':
            str += "Please enter your company contact\n"
            self.ui.error_label_prof.setText(str)
            return
        if not tel.isdecimal():
            self.ui.error_label_prof.setText("Tel number must be an integer")
            return

        if "@" not in mail:
            self.ui.error_label_prof.setText("Unvalid email form")
            return
        str = self.mainControl.editCompanyProfile(self.mainCompany,name,tel,mail,business)
        self.ui.error_label_prof.setText(str)
        return

    def addr_edit(self):
        no = self.ui.lineEdit_houseNo.text()
        soi = self.ui.lineEdit_soi.text()
        street = self.ui.lineEdit_street.text()
        district =self.ui.lineEdit_district.text()
        city = self.ui.lineEdit_city.text()
        province = self.ui.lineEdit_state.text()
        zipcode = self.ui.lineEdit_zip.text()

        text = self.mainControl.editCompanyAddress(self.mainCompany,no,soi,street,district,city,province,zipcode)

        self.ui.error_label_add.setText(text)
        return
    def closed(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_Company_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
