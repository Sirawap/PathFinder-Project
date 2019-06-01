from PySide2.QtWidgets import *
import ui_py.Company_view_profile
import src.Company
from src.mainSystem import MainSystem
class View_Company_Profile_GUI(QWidget):
    def __init__(self,company):
        QWidget.__init__(self,None)

        self.mainCompany = company

        self.ui = ui_py.Company_view_profile.Ui_Form()
        self.ui.setupUi(self)
        self.mainControl = MainSystem()
        self.mainCompany = company
        self.comadr = self.mainControl.getCompanyAddress(self.mainCompany)
        self.ui.label_5.setText(self.mainCompany.companyName)
        self.ui.label_7.setText(self.mainCompany.tel)
        self.ui.label_9.setText(self.mainCompany.email)
        self.ui.label_10.setText(self.mainCompany.AddNo)
        self.ui.label_18.setText(self.mainCompany.AddSoi)
        self.ui.label_19.setText(self.mainCompany.AddSt)
        self.ui.label_20.setText(self.mainCompany.AddDistrict)
        self.ui.label_21.setText(self.mainCompany.AddCity)
        self.ui.label_22.setText(self.mainCompany.AddProvince)
        self.ui.label_23.setText(self.mainCompany.AddZip)
