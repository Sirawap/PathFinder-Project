import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.View_Job_detail
# from src.mainSystem import MainSystem

class View_Job_detail_GUI(QWidget):
    def __init__(self,job):
        QWidget.__init__(self,None)
        self.ui = ui_py.View_Job_detail.Ui_Form()
        self.ui.setupUi(self)
        self.job = job


        ##Edit duao
        ###########
        self.ui.label_company.setText(job[0])
        self.ui.label_jobName.setText(job[1])
        self.ui.label_Position.setText(job[2])
        self.ui.label_salary.setText(job[3])
        self.ui.textEdit_description.setText(job[4])
        self.ui.label_education.setText(job[5])
        self.ui.label_field.setText(job[6])
        self.ui.textEdit_experience.setText(job[7])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = View_Job_detail_GUI()
    w.show()
    sys.exit(app.exec_())


