# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_Registeration.ui',
# licensing of 'Company_Registeration.ui' applies.
#
# Created: Tue May 28 21:10:35 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 532)
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
        self.label_17.setGeometry(QtCore.QRect(280, 300, 16, 16))
        self.label_17.setObjectName("label_17")
        self.register_tel = QtWidgets.QLineEdit(Form)
        self.register_tel.setGeometry(QtCore.QRect(360, 150, 111, 22))
        self.register_tel.setText("")
        self.register_tel.setObjectName("register_tel")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 71, 16))
        self.label_2.setObjectName("label_2")
        self.register_password = QtWidgets.QLineEdit(Form)
        self.register_password.setGeometry(QtCore.QRect(110, 330, 161, 22))
        self.register_password.setObjectName("register_password")
        self.register_company_name = QtWidgets.QLineEdit(Form)
        self.register_company_name.setGeometry(QtCore.QRect(140, 120, 241, 22))
        self.register_company_name.setObjectName("register_company_name")
        self.register_rePassword = QtWidgets.QLineEdit(Form)
        self.register_rePassword.setGeometry(QtCore.QRect(170, 360, 161, 22))
        self.register_rePassword.setObjectName("register_rePassword")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(30, 150, 61, 16))
        self.label_23.setObjectName("label_23")
        self.register_email = QtWidgets.QLineEdit(Form)
        self.register_email.setGeometry(QtCore.QRect(110, 150, 161, 22))
        self.register_email.setObjectName("register_email")
        self.confirm_b = QtWidgets.QPushButton(Form)
        self.confirm_b.setGeometry(QtCore.QRect(200, 480, 93, 28))
        self.confirm_b.setObjectName("confirm_b")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 101, 16))
        self.label.setObjectName("label")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(320, 150, 31, 16))
        self.label_24.setObjectName("label_24")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(340, 360, 16, 16))
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
        self.label_6.setGeometry(QtCore.QRect(30, 330, 71, 16))
        self.label_6.setObjectName("label_6")
        self.register_username = QtWidgets.QLineEdit(Form)
        self.register_username.setGeometry(QtCore.QRect(110, 300, 161, 22))
        self.register_username.setObjectName("register_username")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(280, 330, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(30, 360, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(480, 150, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(280, 150, 16, 16))
        self.label_26.setObjectName("label_26")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(70, 410, 351, 51))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(240, 260, 61, 24))
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(260, 230, 71, 24))
        self.label_13.setObjectName("label_13")
        self.lineEdit_zip = QtWidgets.QLineEdit(Form)
        self.lineEdit_zip.setGeometry(QtCore.QRect(310, 260, 63, 22))
        self.lineEdit_zip.setObjectName("lineEdit_zip")
        self.lineEdit_city = QtWidgets.QLineEdit(Form)
        self.lineEdit_city.setGeometry(QtCore.QRect(340, 230, 124, 22))
        self.lineEdit_city.setText("")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(30, 260, 91, 24))
        self.label_14.setObjectName("label_14")
        self.lineEdit_houseNo = QtWidgets.QLineEdit(Form)
        self.lineEdit_houseNo.setGeometry(QtCore.QRect(60, 200, 63, 22))
        self.lineEdit_houseNo.setObjectName("lineEdit_houseNo")
        self.lineEdit_street = QtWidgets.QLineEdit(Form)
        self.lineEdit_street.setGeometry(QtCore.QRect(360, 200, 126, 22))
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(140, 200, 23, 24))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 230, 101, 24))
        self.label_12.setObjectName("label_12")
        self.lineEdit_district = QtWidgets.QLineEdit(Form)
        self.lineEdit_district.setGeometry(QtCore.QRect(130, 230, 117, 22))
        self.lineEdit_district.setObjectName("lineEdit_district")
        self.lineEdit_state = QtWidgets.QLineEdit(Form)
        self.lineEdit_state.setGeometry(QtCore.QRect(130, 260, 94, 22))
        self.lineEdit_state.setText("")
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.lineEdit_soi = QtWidgets.QLineEdit(Form)
        self.lineEdit_soi.setGeometry(QtCore.QRect(170, 200, 121, 22))
        self.lineEdit_soi.setObjectName("lineEdit_soi")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 31, 24))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(310, 200, 51, 24))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Address :", None, -1))
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
        self.label_16.setText(QtWidgets.QApplication.translate("Form", " Zip Code:", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "City/Ampur:", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Province/State:", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Soi:", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "District/Tambon:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "No.", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Street:", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

