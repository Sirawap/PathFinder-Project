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
        self.mainCompany = company
        self.mainControl = MainSystem()
        self.ui.lineEdit_comp_name.setText(self.mainCompany.companyName)
        self.ui.lineEdit_tel.setText(self.mainCompany.tel)
        self.ui.lineEdit_web.setText(self.mainCompany.email)

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
        str = self.mainControl.editCompanyProfile(self.mainCompany,name,tel,mail,business)
        self.ui.error_label_prof.setText(str)
        return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_Company_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
