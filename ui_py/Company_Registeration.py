# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_Registeration.ui',
# licensing of 'Company_Registeration.ui' applies.
#
# Created: Sun Jun  2 09:56:48 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 414)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    color: white\n"
"}\n"
"\n"
"QComboBox{    \n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLabel#error_label{    \n"
"    color: red;\n"
"}")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(280, 190, 16, 16))
        self.label_17.setObjectName("label_17")
        self.register_tel = QtWidgets.QLineEdit(Form)
        self.register_tel.setGeometry(QtCore.QRect(360, 150, 111, 22))
        self.register_tel.setText("")
        self.register_tel.setObjectName("register_tel")
        self.register_password = QtWidgets.QLineEdit(Form)
        self.register_password.setGeometry(QtCore.QRect(110, 220, 161, 22))
        self.register_password.setObjectName("register_password")
        self.register_company_name = QtWidgets.QLineEdit(Form)
        self.register_company_name.setGeometry(QtCore.QRect(140, 120, 241, 22))
        self.register_company_name.setObjectName("register_company_name")
        self.register_rePassword = QtWidgets.QLineEdit(Form)
        self.register_rePassword.setGeometry(QtCore.QRect(170, 250, 161, 22))
        self.register_rePassword.setObjectName("register_rePassword")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_23.setObjectName("label_23")
        self.register_email = QtWidgets.QLineEdit(Form)
        self.register_email.setGeometry(QtCore.QRect(110, 150, 161, 22))
        self.register_email.setObjectName("register_email")
        self.confirm_b = QtWidgets.QPushButton(Form)
        self.confirm_b.setGeometry(QtCore.QRect(200, 370, 93, 28))
        self.confirm_b.setObjectName("confirm_b")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 101, 16))
        self.label.setObjectName("label")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(320, 150, 31, 16))
        self.label_24.setObjectName("label_24")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(340, 250, 16, 16))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(390, 120, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 71, 16))
        self.label_6.setObjectName("label_6")
        self.register_username = QtWidgets.QLineEdit(Form)
        self.register_username.setGeometry(QtCore.QRect(110, 190, 161, 22))
        self.register_username.setObjectName("register_username")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(280, 220, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(30, 250, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(480, 150, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(280, 150, 16, 16))
        self.label_26.setObjectName("label_26")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(70, 300, 351, 51))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "email :", None, -1))
        self.confirm_b.setText(QtWidgets.QApplication.translate("Form", "Confirm", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Company name :", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Form", "Tel :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "User name :", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Register", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Password   :", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Re-confirm Password  :", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

