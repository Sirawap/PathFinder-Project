import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.View_Job_detail
# from src.mainSystem import MainSystem

class View_Job_detail_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.ui = ui_py.View_Job_detail.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_view_company_profile.clicked.connect(self.viewCompanyProfile)
        self.ui.pushButton_request_Job(self.requestJob)

    def viewCompanyProfile(self):
        pass

    def requestJob(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = View_Job_detail_GUI()
    w.show()
    sys.exit(app.exec_())


