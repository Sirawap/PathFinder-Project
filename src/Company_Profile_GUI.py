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
        self.ui.label_comp_type.setText(self.mainCompany.type)
        if self.comadr != None:

            self.ui.label_10.setText(self.comadr.number)
            self.ui.label_18.setText(self.comadr.soi)
            self.ui.label_19.setText(self.comadr.street)
            self.ui.label_20.setText(self.comadr.district)
            self.ui.label_21.setText(self.comadr.city)
            self.ui.label_22.setText(self.comadr.province)
            self.ui.label_23.setText(self.comadr.zipcode)
