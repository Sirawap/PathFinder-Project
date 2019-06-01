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
        self.ui.pushButton_request_Job.clicked.connect(self.requestJob)

        ##Edit duao
        ###########
        self.ui.label_company.setText("PornHub")
        self.ui.label_jobName.setText("Project Manhattan")
        self.ui.label_Position.setText("Pornstar(M)")
        self.ui.label_salary.setText("7000THB per film")
        self.ui.textEdit_description.setText("Require highly physical and numerous of cemen aaaaaaaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooo")
        self.ui.label_education.setText("Associate diploma or higher")
        self.ui.label_field.setText("Arts Program Classical Dance and Drama will get more concern")
        self.ui.textEdit_experience.setText("48Hr with 10 women")



    def viewCompanyProfile(self):
        pass

    def requestJob(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = View_Job_detail_GUI()
    w.show()
    sys.exit(app.exec_())


