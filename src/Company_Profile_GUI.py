from PySide2.QtWidgets import *
import ui_py.Company_view_profile
import src.Company

class View_Company_Profile_GUI(QWidget):
    def __init__(self,company = src.Company.Company()):
        QWidget.__init__(self,None)

        self.mainCompany = company

        self.ui = ui_py.Company_view_profile.Ui_Form()
        self.ui.setupUi(self)

        self.ui.label_5.setText(self.mainCompany.getCompanyName())
        self.ui.label_5.setText(self.mainCompany.getCompanyName())
