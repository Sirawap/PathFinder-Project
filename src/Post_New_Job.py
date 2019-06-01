import sys
from PySide2.QtWidgets import *
import ui_py.Create_Job_Criteria_UI
from src.mainSystem import MainSystem

class Post_New_Job(QWidget):
    def __init__(self,company):
        QWidget.__init__(self,None)

        self.ui = ui_py.Create_Job_Criteria_UI.Ui_Form()
        self.ui.setupUi(self)
        self.mainControl = MainSystem()
        self.mainCompany = company
        self.ui.pushButton.clicked.connect(self.post_job)

    def post_job(self):
        job_name = self.ui.lineEdit_job_name.text()
        position = self.ui.lineEdit_position.text()
        salary = self.ui.lineEdit_salary.text()
        #description = self.ui.textEdit_description.text()
        education = self.ui.comboBox_Degree.currentText()
        field = self.ui.comboBox_major.currentText()
        experience = self.ui.lineEdit_experience1.text()
        str = ''
        if job_name == '':
            str += "Please enter the job offer a name\n"
        else:
            pass
        if position == '' or salary == '':
            str += "Please enter position and salary\n"
        else:
            pass
            #plus short description
        if education == '' or field == '  --None--':
            str += "Please enter education background"
        else:
            pass
            #plus experience
        self.ui.error_label.setText(str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Post_New_Job()
    w.show()
    sys.exit(app.exec_())


