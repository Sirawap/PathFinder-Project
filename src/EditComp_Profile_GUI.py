import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_Edit_Profile

class Edit_Company_Profile_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = ui_py.Company_Edit_Profile.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_OK.clicked.connect(self.comp_edit)

    def comp_edit(self):
        name = self.ui.lineEdit_comp_name.text()
        tel = self.ui.lineEdit_tel.text()
        mail = self.ui.lineEdit_web.text()
        no = self.ui.lineEdit_houseNo.text()
        soi = self.ui.lineEdit_soi.text()
        street = self.ui.lineEdit_street.text()
        district = self.ui.lineEdit_district.text()
        city = self.ui.lineEdit_city.text()
        province = self.ui.lineEdit_state.text()
        zip = self.ui.lineEdit_zip.text()
        business = self.ui.comboBox_Business.currentText()
        if name == '':
            print("Please enter your company name")
        if tel == '' or mail == '':
            print("Please enter your company contact")
        if no == '' or street== '' or city == '' or province == '' or zip == '':
            print("Please filled your company address")
        if business == "  -- None --":
            print("Please select business")
        print("F for reespect")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_Company_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
