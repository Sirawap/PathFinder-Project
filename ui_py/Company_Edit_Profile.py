# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_Edit_Profile.ui',
# licensing of 'Company_Edit_Profile.ui' applies.
#
# Created: Sat Jun  1 15:37:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 418)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    color: white\n"
"}\n"
"QLabel#error_label_add{\n"
"    color: red;\n"
"}\n"
"QLabel#error_label_prof{\n"
"    color: red;\n"
"}\n"
"\n"
"QComboBox{\n"
"    \n"
"    background-color: rgb(65, 65, 65);\n"
"}")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"QComboBox{\n"
"    background-color: rgb(65, 65, 65);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 568, 398))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(132, 9, 281, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_updateCompany = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_updateCompany.setGeometry(QtCore.QRect(130, 150, 156, 23))
        self.pushButton_updateCompany.setObjectName("pushButton_updateCompany")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.error_label_add = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.error_label_add.setGeometry(QtCore.QRect(80, 360, 371, 16))
        self.error_label_add.setText("")
        self.error_label_add.setObjectName("error_label_add")
        self.error_label_prof = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.error_label_prof.setGeometry(QtCore.QRect(200, 80, 371, 16))
        self.error_label_prof.setText("")
        self.error_label_prof.setObjectName("error_label_prof")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 311, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_comp_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_comp_name.setText("")
        self.lineEdit_comp_name.setObjectName("lineEdit_comp_name")
        self.horizontalLayout.addWidget(self.lineEdit_comp_name)
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 197, 158, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_houseNo = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_houseNo.setObjectName("lineEdit_houseNo")
        self.horizontalLayout_5.addWidget(self.lineEdit_houseNo)
        self.layoutWidget2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2.setGeometry(QtCore.QRect(201, 197, 159, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lineEdit_soi = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_soi.setObjectName("lineEdit_soi")
        self.horizontalLayout_6.addWidget(self.lineEdit_soi)
        self.layoutWidget3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget3.setGeometry(QtCore.QRect(371, 197, 175, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.lineEdit_street = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.horizontalLayout_7.addWidget(self.lineEdit_street)
        self.layoutWidget4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget4.setGeometry(QtCore.QRect(21, 227, 186, 36))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lineEdit_district = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_district.setObjectName("lineEdit_district")
        self.horizontalLayout_8.addWidget(self.lineEdit_district)
        self.layoutWidget5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget5.setGeometry(QtCore.QRect(221, 227, 165, 36))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.lineEdit_city = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_city.setText("")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.horizontalLayout_9.addWidget(self.lineEdit_city)
        self.layoutWidget6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 270, 187, 37))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.lineEdit_state = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_state.setText("")
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.horizontalLayout_10.addWidget(self.lineEdit_state)
        self.layoutWidget7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget7.setGeometry(QtCore.QRect(220, 270, 186, 37))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.lineEdit_zip = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_zip.setObjectName("lineEdit_zip")
        self.horizontalLayout_11.addWidget(self.lineEdit_zip)
        self.layoutWidget8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget8.setGeometry(QtCore.QRect(10, 120, 331, 20))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.comboBox_Business = QtWidgets.QComboBox(self.layoutWidget8)
        self.comboBox_Business.setObjectName("comboBox_Business")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.comboBox_Business.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_Business)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)
        self.layoutWidget9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget9.setGeometry(QtCore.QRect(350, 40, 139, 35))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget9)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.layoutWidget9)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.horizontalLayout_3.addWidget(self.lineEdit_tel)
        self.layoutWidget10 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget10.setGeometry(QtCore.QRect(10, 80, 176, 22))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget10)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_web = QtWidgets.QLineEdit(self.layoutWidget10)
        self.lineEdit_web.setText("")
        self.lineEdit_web.setObjectName("lineEdit_web")
        self.horizontalLayout_2.addWidget(self.lineEdit_web)
        self.pushButton_CancelCompAdd = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_CancelCompAdd.setGeometry(QtCore.QRect(430, 300, 75, 23))
        self.pushButton_CancelCompAdd.setObjectName("pushButton_CancelCompAdd")
        self.pushButton_UpdateCompAdd = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_UpdateCompAdd.setGeometry(QtCore.QRect(130, 320, 161, 23))
        self.pushButton_UpdateCompAdd.setObjectName("pushButton_UpdateCompAdd")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(325, 53, 10, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(493, 50, 10, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(190, 80, 10, 16))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(210, 280, 10, 16))
        self.label_12.setObjectName("label_12")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Edit Profile", None, -1))
        self.pushButton_updateCompany.setText(QtWidgets.QApplication.translate("Form", "Update", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Address", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Company name:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "No.", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Soi:", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Street:", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "District/Tambon:", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "City/Ampur:", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Province/State:", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Form", " Zip Code:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Company business type:", None, -1))
        self.comboBox_Business.setItemText(0, QtWidgets.QApplication.translate("Form", "  -- None --", None, -1))
        self.comboBox_Business.setItemText(1, QtWidgets.QApplication.translate("Form", "New Item", None, -1))
        self.comboBox_Business.setItemText(2, QtWidgets.QApplication.translate("Form", "Alocohol", None, -1))
        self.comboBox_Business.setItemText(3, QtWidgets.QApplication.translate("Form", "Construction", None, -1))
        self.comboBox_Business.setItemText(4, QtWidgets.QApplication.translate("Form", "Domestic", None, -1))
        self.comboBox_Business.setItemText(5, QtWidgets.QApplication.translate("Form", "Financial instructor", None, -1))
        self.comboBox_Business.setItemText(6, QtWidgets.QApplication.translate("Form", "Health Service", None, -1))
        self.comboBox_Business.setItemText(7, QtWidgets.QApplication.translate("Form", "Manufacturer", None, -1))
        self.comboBox_Business.setItemText(8, QtWidgets.QApplication.translate("Form", "Mining", None, -1))
        self.comboBox_Business.setItemText(9, QtWidgets.QApplication.translate("Form", "Retail sales", None, -1))
        self.comboBox_Business.setItemText(10, QtWidgets.QApplication.translate("Form", "Service", None, -1))
        self.comboBox_Business.setItemText(11, QtWidgets.QApplication.translate("Form", "Transportation", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Tel :", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "E-mail :", None, -1))
        self.pushButton_CancelCompAdd.setText(QtWidgets.QApplication.translate("Form", "Back", None, -1))
        self.pushButton_UpdateCompAdd.setText(QtWidgets.QApplication.translate("Form", "Update", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

