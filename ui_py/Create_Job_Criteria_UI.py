# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_Job_Criteria_UI.ui',
# licensing of 'Create_Job_Criteria_UI.ui' applies.
#
# Created: Fri May 31 21:45:00 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 531)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    color: white;\n"
"    font: \"Arial\";\n"
"    \n"
"}\n"
"\n"
"QComboBox{\n"
"    \n"
"    background-color: rgb(65, 65, 65);\n"
"}"
'''QLabel#error_label{
    color: rgb(190,30,30);
}''')
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 431, 16))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 240, 221, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_description = QtWidgets.QTextEdit(Form)
        self.textEdit_description.setGeometry(QtCore.QRect(40, 260, 381, 71))
        self.textEdit_description.setObjectName("textEdit_description")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 340, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 400, 81, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 490, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(40, 440, 371, 41))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.lineEdit_job_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_job_name.setGeometry(QtCore.QRect(140, 90, 141, 22))
        self.lineEdit_job_name.setObjectName("lineEdit_job_name")
        self.lineEdit_salary = QtWidgets.QLineEdit(Form)
        self.lineEdit_salary.setGeometry(QtCore.QRect(110, 180, 113, 21))
        self.lineEdit_salary.setObjectName("lineEdit_salary")
        self.lineEdit_position = QtWidgets.QLineEdit(Form)
        self.lineEdit_position.setGeometry(QtCore.QRect(110, 150, 113, 22))
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.comboBox_Degree = QtWidgets.QComboBox(Form)
        self.comboBox_Degree.setGeometry(QtCore.QRect(120, 340, 181, 22))
        self.comboBox_Degree.setObjectName("comboBox_Degree")
        self.comboBox_Degree.addItem("")
        self.comboBox_Degree.addItem("")
        self.comboBox_Degree.addItem("")
        self.comboBox_Degree.addItem("")
        self.lineEdit_experience1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_experience1.setGeometry(QtCore.QRect(120, 400, 311, 22))
        self.lineEdit_experience1.setObjectName("lineEdit_experience1")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 210, 81, 16))
        self.label_13.setObjectName("label_13")
        self.comboBox_major = QtWidgets.QComboBox(Form)
        self.comboBox_major.setGeometry(QtCore.QRect(120, 370, 181, 22))
        self.comboBox_major.setObjectName("comboBox_major")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 370, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(290, 90, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(230, 150, 16, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(230, 180, 16, 16))
        self.label_28.setObjectName("label_28")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(310, 340, 16, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(310, 370, 16, 16))
        self.label_31.setObjectName("label_31")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Create Requiremnet", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Job name         :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Salary   :", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Position :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "_____________________________________________________________", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Short description (100 characters)", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Education   :", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "Experience :", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "confirm", None, -1))
        self.comboBox_Degree.setItemText(0, QtWidgets.QApplication.translate("Form", "no minimum requried", None, -1))
        self.comboBox_Degree.setItemText(1, QtWidgets.QApplication.translate("Form", "minimum bachelor degree", None, -1))
        self.comboBox_Degree.setItemText(2, QtWidgets.QApplication.translate("Form", "minimum master degree", None, -1))
        self.comboBox_Degree.setItemText(3, QtWidgets.QApplication.translate("Form", "PHD", None, -1))
        self.lineEdit_experience1.setText(QtWidgets.QApplication.translate("Form", "eg. pilot must have at least 1000 of flight hours", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "Required Skill", None, -1))
        self.comboBox_major.setItemText(0, QtWidgets.QApplication.translate("Form", "  --None--", None, -1))
        self.comboBox_major.setItemText(1, QtWidgets.QApplication.translate("Form", "Accounting", None, -1))
        self.comboBox_major.setItemText(2, QtWidgets.QApplication.translate("Form", "Computer Science", None, -1))
        self.comboBox_major.setItemText(3, QtWidgets.QApplication.translate("Form", "Engineering", None, -1))
        self.comboBox_major.setItemText(4, QtWidgets.QApplication.translate("Form", "Business Administration", None, -1))
        self.comboBox_major.setItemText(5, QtWidgets.QApplication.translate("Form", "Sociology/Social Work", None, -1))
        self.comboBox_major.setItemText(6, QtWidgets.QApplication.translate("Form", "Mathematics/Statistics", None, -1))
        self.comboBox_major.setItemText(7, QtWidgets.QApplication.translate("Form", "Psychology", None, -1))
        self.comboBox_major.setItemText(8, QtWidgets.QApplication.translate("Form", "History/Political Science", None, -1))
        self.comboBox_major.setItemText(9, QtWidgets.QApplication.translate("Form", "Healthcare", None, -1))
        self.comboBox_major.setItemText(10, QtWidgets.QApplication.translate("Form", "Education", None, -1))
        self.comboBox_major.setItemText(11, QtWidgets.QApplication.translate("Form", "Environmental Science", None, -1))
        self.comboBox_major.setItemText(12, QtWidgets.QApplication.translate("Form", "Visual & Performing Arts", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Major field :", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_30.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_31.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

