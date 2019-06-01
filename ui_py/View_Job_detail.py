# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View_Job_detail.ui',
# licensing of 'View_Job_detail.ui' applies.
#
# Created: Sat Jun  1 12:22:45 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 532)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    color: white;\n"
"}")
        self.pushButton_request_Job = QtWidgets.QPushButton(Form)
        self.pushButton_request_Job.setGeometry(QtCore.QRect(320, 470, 121, 28))
        self.pushButton_request_Job.setObjectName("pushButton_request_Job")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 10, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 170, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(100, 230, 221, 16))
        self.label_10.setObjectName("label_10")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(100, 440, 371, 41))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(100, 330, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 100, 431, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(100, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(100, 360, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 140, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(100, 390, 81, 16))
        self.label_12.setObjectName("label_12")
        self.label_jobName = QtWidgets.QLabel(Form)
        self.label_jobName.setGeometry(QtCore.QRect(420, 80, 121, 16))
        self.label_jobName.setObjectName("label_jobName")
        self.label_Position = QtWidgets.QLabel(Form)
        self.label_Position.setGeometry(QtCore.QRect(170, 140, 151, 16))
        self.label_Position.setObjectName("label_Position")
        self.label_salary = QtWidgets.QLabel(Form)
        self.label_salary.setGeometry(QtCore.QRect(170, 170, 141, 16))
        self.label_salary.setObjectName("label_salary")
        self.textEdit_description = QtWidgets.QTextEdit(Form)
        self.textEdit_description.setGeometry(QtCore.QRect(100, 250, 391, 71))
        self.textEdit_description.setObjectName("textEdit_description")
        self.label_education = QtWidgets.QLabel(Form)
        self.label_education.setGeometry(QtCore.QRect(170, 330, 261, 16))
        self.label_education.setObjectName("label_education")
        self.label_field = QtWidgets.QLabel(Form)
        self.label_field.setGeometry(QtCore.QRect(170, 360, 311, 16))
        self.label_field.setObjectName("label_field")
        self.textEdit_experience = QtWidgets.QTextEdit(Form)
        self.textEdit_experience.setGeometry(QtCore.QRect(170, 390, 321, 51))
        self.textEdit_experience.setObjectName("textEdit_experience")
        self.pushButton_view_company_profile = QtWidgets.QPushButton(Form)
        self.pushButton_view_company_profile.setGeometry(QtCore.QRect(140, 470, 121, 28))
        self.pushButton_view_company_profile.setObjectName("pushButton_view_company_profile")
        self.label_company = QtWidgets.QLabel(Form)
        self.label_company.setGeometry(QtCore.QRect(170, 80, 121, 16))
        self.label_company.setObjectName("label_company")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 61, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton_request_Job.setText(QtWidgets.QApplication.translate("Form", "Request this job", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Job Detail", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Salary   :", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Short description (100 characters)", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Job name         :", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Education   :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "_____________________________________________________________", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "Required Skill", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Major field :", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Position :", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "Experience :", None, -1))
        self.label_jobName.setText(QtWidgets.QApplication.translate("Form", "Txt", None, -1))
        self.label_Position.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.label_salary.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.textEdit_description.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.label_education.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.label_field.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.textEdit_experience.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.pushButton_view_company_profile.setText(QtWidgets.QApplication.translate("Form", "View company profile", None, -1))
        self.label_company.setText(QtWidgets.QApplication.translate("Form", "txt", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Company:", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

