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
        self.ui.pushButton_2.clicked.connect(self.closed)

    def post_job(self):
        job_name = self.ui.lineEdit_job_name.text()
        position = self.ui.lineEdit_position.text()
        salary = self.ui.lineEdit_salary.text()
        description = self.ui.textEdit_description.toPlainText()
        education = self.ui.comboBox_Degree.currentText()
        field = self.ui.comboBox_major.currentText()
        experience = self.ui.lineEdit_experience1.text()
        str = ''
        if job_name == '':
            str = "Please enter the job offer a name\n"
            self.ui.error_label.setText(str)
            return

        if position == '' or salary == '':
            str = "Please enter position and salary\n"
            self.ui.error_label.setText(str)
            return
            #plus short description
        if education == '' or field == '  --None--':
            str = "Please enter education background"
            self.ui.error_label.setText(str)
            return
            #plus experience

        str = self.mainControl.addJob(self.mainCompany,job_name,salary,description,education,field,experience,position)
        self.ui.error_label.setText(str)



    def closed(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Post_New_Job()
    w.show()
    sys.exit(app.exec_())


