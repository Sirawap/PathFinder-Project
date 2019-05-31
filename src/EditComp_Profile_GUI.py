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
        web = self.ui.lineEdit_web.text()
        no = self.ui.lineEdit_houseNo.text()
        soi = self.ui.lineEdit_soi.text()
        street = self.ui.lineEdit_street.text()
        district = self.ui.lineEdit_district.text()
        city = self.ui.lineEdit_city.text()
        province = self.ui.lineEdit_state.text()
        zip = self.ui.lineEdit_zip.text()
        
        '''business = ''
        if self.ui.checkBox_14.isChecked() :
            business += ","+self.ui.checkBox_14.text()
        if self.ui.checkBox_15.isChecked():
            business += ","+self.ui.checkBox_15.text()
        if self.ui.checkBox_17.isChecked():
            business += ","+self.ui.checkBox_17.text()
        if self.ui.checkBox_21.isChecked():
            business += ","+self.ui.checkBox_21.text()
        if self.ui.checkBox_22.isChecked():
            business += ","+self.ui.checkBox_22.text()
        if self.ui.checkBox_23.isChecked():
            business += ","+self.ui.checkBox_23.text()
        if self.ui.checkBox_24.isChecked():
            business += ","+self.ui.checkBox_24.text()
        if self.ui.checkBox_26.isChecked():
            business += ","+self.ui.checkBox_26.text()
        if self.ui.checkBox_29.isChecked():
            business += ","+self.ui.checkBox_29.text()
        if self.ui.checkBox_31.isChecked():
            business += ","+self.ui.checkBox_31.text()
        if self.ui.checkBox_33.isChecked():
            business += ","+self.ui.checkBox_33.text()
        if self.ui.checkBox_36.isChecked():
            business += ","+self.ui.checkBox_36.text()
        if self.ui.checkBox_37.isChecked():
            business += ","+self.ui.checkBox_37.text()
        if self.ui.checkBox_39.isChecked():
            business += ","+self.ui.checkBox_39.text()
        if self.ui.checkBox_40.isChecked():
            business += ","+self.ui.checkBox_40.text()
        if self.ui.checkBox_41.isChecked():
            business += ","+self.ui.checkBox_41.text()
        if self.ui.checkBox_47.isChecked():
            business += ","+self.ui.checkBox_47.text()
        business = business[1:]
        print(business)'''
        print("F for reespect")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_Company_Profile_GUI()
    w.show()
    sys.exit(app.exec_())
