# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_Job_Criteria_UI.ui',
# licensing of 'Create_Job_Criteria_UI.ui' applies.
#
# Created: Thu May 30 15:23:54 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 650)
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
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 160, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 431, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 330, 201, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_description = QtWidgets.QTextEdit(Form)
        self.textEdit_description.setGeometry(QtCore.QRect(40, 350, 351, 51))
        self.textEdit_description.setObjectName("textEdit_description")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 410, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 470, 81, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 590, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.warning_label = QtWidgets.QLabel(Form)
        self.warning_label.setGeometry(QtCore.QRect(50, 540, 371, 41))
        self.warning_label.setText("")
        self.warning_label.setObjectName("warning_label")
        self.lineEdit_job_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_job_name.setGeometry(QtCore.QRect(150, 100, 141, 22))
        self.lineEdit_job_name.setObjectName("lineEdit_job_name")
        self.lineEdit_address = QtWidgets.QLineEdit(Form)
        self.lineEdit_address.setGeometry(QtCore.QRect(150, 130, 291, 22))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.lineEdit_tel = QtWidgets.QLineEdit(Form)
        self.lineEdit_tel.setGeometry(QtCore.QRect(70, 160, 113, 22))
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.lineEdit_web = QtWidgets.QLineEdit(Form)
        self.lineEdit_web.setGeometry(QtCore.QRect(270, 160, 171, 22))
        self.lineEdit_web.setText("")
        self.lineEdit_web.setObjectName("lineEdit_web")
        self.lineEdit_salary = QtWidgets.QLineEdit(Form)
        self.lineEdit_salary.setGeometry(QtCore.QRect(110, 240, 113, 21))
        self.lineEdit_salary.setObjectName("lineEdit_salary")
        self.lineEdit_position = QtWidgets.QLineEdit(Form)
        self.lineEdit_position.setGeometry(QtCore.QRect(110, 210, 113, 22))
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.start_h = QtWidgets.QComboBox(Form)
        self.start_h.setGeometry(QtCore.QRect(140, 270, 41, 22))
        self.start_h.setObjectName("start_h")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.start_h.addItem("")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(250, 270, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.start_min = QtWidgets.QComboBox(Form)
        self.start_min.setGeometry(QtCore.QRect(200, 270, 41, 22))
        self.start_min.setObjectName("start_min")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.start_min.addItem("")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(190, 270, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.comboBox_Degree = QtWidgets.QComboBox(Form)
        self.comboBox_Degree.setGeometry(QtCore.QRect(120, 410, 181, 22))
        self.comboBox_Degree.setObjectName("comboBox_Degree")
        self.comboBox_Degree.addItem("")
        self.comboBox_Degree.addItem("")
        self.comboBox_Degree.addItem("")
        self.lineEdit_experience1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_experience1.setGeometry(QtCore.QRect(120, 470, 311, 22))
        self.lineEdit_experience1.setObjectName("lineEdit_experience1")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 300, 81, 16))
        self.label_13.setObjectName("label_13")
        self.finish_h = QtWidgets.QComboBox(Form)
        self.finish_h.setGeometry(QtCore.QRect(270, 270, 41, 22))
        self.finish_h.setObjectName("finish_h")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.finish_h.addItem("")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(320, 270, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.finish_min = QtWidgets.QComboBox(Form)
        self.finish_min.setGeometry(QtCore.QRect(330, 270, 41, 22))
        self.finish_min.setObjectName("finish_min")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.finish_min.addItem("")
        self.comboBox_major = QtWidgets.QComboBox(Form)
        self.comboBox_major.setGeometry(QtCore.QRect(120, 440, 181, 22))
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
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 440, 81, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_experience2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_experience2.setGeometry(QtCore.QRect(120, 500, 311, 22))
        self.lineEdit_experience2.setObjectName("lineEdit_experience2")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(300, 100, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(190, 160, 16, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(230, 210, 16, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(230, 240, 16, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(380, 270, 16, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(310, 410, 16, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(310, 440, 16, 16))
        self.label_31.setObjectName("label_31")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Create Requiremnet", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Job name         :", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Tel :", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Website :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Salary   :", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Position :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "_____________________________________________________________", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "Working hour :   :", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "Address            :", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Short description (150 characters)", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Education   :", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "Experience :", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "confirm", None, -1))
        self.start_h.setItemText(0, QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.start_h.setItemText(1, QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.start_h.setItemText(2, QtWidgets.QApplication.translate("Form", "2", None, -1))
        self.start_h.setItemText(3, QtWidgets.QApplication.translate("Form", "3", None, -1))
        self.start_h.setItemText(4, QtWidgets.QApplication.translate("Form", "4", None, -1))
        self.start_h.setItemText(5, QtWidgets.QApplication.translate("Form", "5", None, -1))
        self.start_h.setItemText(6, QtWidgets.QApplication.translate("Form", "6", None, -1))
        self.start_h.setItemText(7, QtWidgets.QApplication.translate("Form", "7", None, -1))
        self.start_h.setItemText(8, QtWidgets.QApplication.translate("Form", "8", None, -1))
        self.start_h.setItemText(9, QtWidgets.QApplication.translate("Form", "9", None, -1))
        self.start_h.setItemText(10, QtWidgets.QApplication.translate("Form", "10", None, -1))
        self.start_h.setItemText(11, QtWidgets.QApplication.translate("Form", "11", None, -1))
        self.start_h.setItemText(12, QtWidgets.QApplication.translate("Form", "12", None, -1))
        self.start_h.setItemText(13, QtWidgets.QApplication.translate("Form", "13", None, -1))
        self.start_h.setItemText(14, QtWidgets.QApplication.translate("Form", "14", None, -1))
        self.start_h.setItemText(15, QtWidgets.QApplication.translate("Form", "15", None, -1))
        self.start_h.setItemText(16, QtWidgets.QApplication.translate("Form", "16", None, -1))
        self.start_h.setItemText(17, QtWidgets.QApplication.translate("Form", "17", None, -1))
        self.start_h.setItemText(18, QtWidgets.QApplication.translate("Form", "18", None, -1))
        self.start_h.setItemText(19, QtWidgets.QApplication.translate("Form", "19", None, -1))
        self.start_h.setItemText(20, QtWidgets.QApplication.translate("Form", "20", None, -1))
        self.start_h.setItemText(21, QtWidgets.QApplication.translate("Form", "21", None, -1))
        self.start_h.setItemText(22, QtWidgets.QApplication.translate("Form", "22", None, -1))
        self.start_h.setItemText(23, QtWidgets.QApplication.translate("Form", "23", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.start_min.setItemText(0, QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.start_min.setItemText(1, QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.start_min.setItemText(2, QtWidgets.QApplication.translate("Form", "2", None, -1))
        self.start_min.setItemText(3, QtWidgets.QApplication.translate("Form", "3", None, -1))
        self.start_min.setItemText(4, QtWidgets.QApplication.translate("Form", "4", None, -1))
        self.start_min.setItemText(5, QtWidgets.QApplication.translate("Form", "5", None, -1))
        self.start_min.setItemText(6, QtWidgets.QApplication.translate("Form", "6", None, -1))
        self.start_min.setItemText(7, QtWidgets.QApplication.translate("Form", "7", None, -1))
        self.start_min.setItemText(8, QtWidgets.QApplication.translate("Form", "8", None, -1))
        self.start_min.setItemText(9, QtWidgets.QApplication.translate("Form", "9", None, -1))
        self.start_min.setItemText(10, QtWidgets.QApplication.translate("Form", "10", None, -1))
        self.start_min.setItemText(11, QtWidgets.QApplication.translate("Form", "11", None, -1))
        self.start_min.setItemText(12, QtWidgets.QApplication.translate("Form", "12", None, -1))
        self.start_min.setItemText(13, QtWidgets.QApplication.translate("Form", "13", None, -1))
        self.start_min.setItemText(14, QtWidgets.QApplication.translate("Form", "14", None, -1))
        self.start_min.setItemText(15, QtWidgets.QApplication.translate("Form", "15", None, -1))
        self.start_min.setItemText(16, QtWidgets.QApplication.translate("Form", "16", None, -1))
        self.start_min.setItemText(17, QtWidgets.QApplication.translate("Form", "17", None, -1))
        self.start_min.setItemText(18, QtWidgets.QApplication.translate("Form", "18", None, -1))
        self.start_min.setItemText(19, QtWidgets.QApplication.translate("Form", "19", None, -1))
        self.start_min.setItemText(20, QtWidgets.QApplication.translate("Form", "20", None, -1))
        self.start_min.setItemText(21, QtWidgets.QApplication.translate("Form", "21", None, -1))
        self.start_min.setItemText(22, QtWidgets.QApplication.translate("Form", "22", None, -1))
        self.start_min.setItemText(23, QtWidgets.QApplication.translate("Form", "23", None, -1))
        self.start_min.setItemText(24, QtWidgets.QApplication.translate("Form", "24", None, -1))
        self.start_min.setItemText(25, QtWidgets.QApplication.translate("Form", "25", None, -1))
        self.start_min.setItemText(26, QtWidgets.QApplication.translate("Form", "26", None, -1))
        self.start_min.setItemText(27, QtWidgets.QApplication.translate("Form", "27", None, -1))
        self.start_min.setItemText(28, QtWidgets.QApplication.translate("Form", "28", None, -1))
        self.start_min.setItemText(29, QtWidgets.QApplication.translate("Form", "29", None, -1))
        self.start_min.setItemText(30, QtWidgets.QApplication.translate("Form", "30", None, -1))
        self.start_min.setItemText(31, QtWidgets.QApplication.translate("Form", "31", None, -1))
        self.start_min.setItemText(32, QtWidgets.QApplication.translate("Form", "32", None, -1))
        self.start_min.setItemText(33, QtWidgets.QApplication.translate("Form", "33", None, -1))
        self.start_min.setItemText(34, QtWidgets.QApplication.translate("Form", "34", None, -1))
        self.start_min.setItemText(35, QtWidgets.QApplication.translate("Form", "35", None, -1))
        self.start_min.setItemText(36, QtWidgets.QApplication.translate("Form", "36", None, -1))
        self.start_min.setItemText(37, QtWidgets.QApplication.translate("Form", "37", None, -1))
        self.start_min.setItemText(38, QtWidgets.QApplication.translate("Form", "38", None, -1))
        self.start_min.setItemText(39, QtWidgets.QApplication.translate("Form", "39", None, -1))
        self.start_min.setItemText(40, QtWidgets.QApplication.translate("Form", "40", None, -1))
        self.start_min.setItemText(41, QtWidgets.QApplication.translate("Form", "41", None, -1))
        self.start_min.setItemText(42, QtWidgets.QApplication.translate("Form", "42", None, -1))
        self.start_min.setItemText(43, QtWidgets.QApplication.translate("Form", "43", None, -1))
        self.start_min.setItemText(44, QtWidgets.QApplication.translate("Form", "44", None, -1))
        self.start_min.setItemText(45, QtWidgets.QApplication.translate("Form", "45", None, -1))
        self.start_min.setItemText(46, QtWidgets.QApplication.translate("Form", "46", None, -1))
        self.start_min.setItemText(47, QtWidgets.QApplication.translate("Form", "47", None, -1))
        self.start_min.setItemText(48, QtWidgets.QApplication.translate("Form", "48", None, -1))
        self.start_min.setItemText(49, QtWidgets.QApplication.translate("Form", "49", None, -1))
        self.start_min.setItemText(50, QtWidgets.QApplication.translate("Form", "50", None, -1))
        self.start_min.setItemText(51, QtWidgets.QApplication.translate("Form", "51", None, -1))
        self.start_min.setItemText(52, QtWidgets.QApplication.translate("Form", "52", None, -1))
        self.start_min.setItemText(53, QtWidgets.QApplication.translate("Form", "53", None, -1))
        self.start_min.setItemText(54, QtWidgets.QApplication.translate("Form", "54", None, -1))
        self.start_min.setItemText(55, QtWidgets.QApplication.translate("Form", "55", None, -1))
        self.start_min.setItemText(56, QtWidgets.QApplication.translate("Form", "56", None, -1))
        self.start_min.setItemText(57, QtWidgets.QApplication.translate("Form", "57", None, -1))
        self.start_min.setItemText(58, QtWidgets.QApplication.translate("Form", "58", None, -1))
        self.start_min.setItemText(59, QtWidgets.QApplication.translate("Form", "59", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", ":", None, -1))
        self.comboBox_Degree.setItemText(0, QtWidgets.QApplication.translate("Form", "bachelor degree or higher", None, -1))
        self.comboBox_Degree.setItemText(1, QtWidgets.QApplication.translate("Form", "master degree or higher", None, -1))
        self.comboBox_Degree.setItemText(2, QtWidgets.QApplication.translate("Form", "PHD", None, -1))
        self.lineEdit_experience1.setText(QtWidgets.QApplication.translate("Form", "eg. pilot must have at least 1000 of flight hours", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "Required Skill", None, -1))
        self.finish_h.setItemText(0, QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.finish_h.setItemText(1, QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.finish_h.setItemText(2, QtWidgets.QApplication.translate("Form", "2", None, -1))
        self.finish_h.setItemText(3, QtWidgets.QApplication.translate("Form", "3", None, -1))
        self.finish_h.setItemText(4, QtWidgets.QApplication.translate("Form", "4", None, -1))
        self.finish_h.setItemText(5, QtWidgets.QApplication.translate("Form", "5", None, -1))
        self.finish_h.setItemText(6, QtWidgets.QApplication.translate("Form", "6", None, -1))
        self.finish_h.setItemText(7, QtWidgets.QApplication.translate("Form", "7", None, -1))
        self.finish_h.setItemText(8, QtWidgets.QApplication.translate("Form", "8", None, -1))
        self.finish_h.setItemText(9, QtWidgets.QApplication.translate("Form", "9", None, -1))
        self.finish_h.setItemText(10, QtWidgets.QApplication.translate("Form", "10", None, -1))
        self.finish_h.setItemText(11, QtWidgets.QApplication.translate("Form", "11", None, -1))
        self.finish_h.setItemText(12, QtWidgets.QApplication.translate("Form", "12", None, -1))
        self.finish_h.setItemText(13, QtWidgets.QApplication.translate("Form", "13", None, -1))
        self.finish_h.setItemText(14, QtWidgets.QApplication.translate("Form", "14", None, -1))
        self.finish_h.setItemText(15, QtWidgets.QApplication.translate("Form", "15", None, -1))
        self.finish_h.setItemText(16, QtWidgets.QApplication.translate("Form", "16", None, -1))
        self.finish_h.setItemText(17, QtWidgets.QApplication.translate("Form", "17", None, -1))
        self.finish_h.setItemText(18, QtWidgets.QApplication.translate("Form", "18", None, -1))
        self.finish_h.setItemText(19, QtWidgets.QApplication.translate("Form", "19", None, -1))
        self.finish_h.setItemText(20, QtWidgets.QApplication.translate("Form", "20", None, -1))
        self.finish_h.setItemText(21, QtWidgets.QApplication.translate("Form", "21", None, -1))
        self.finish_h.setItemText(22, QtWidgets.QApplication.translate("Form", "22", None, -1))
        self.finish_h.setItemText(23, QtWidgets.QApplication.translate("Form", "23", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", ":", None, -1))
        self.finish_min.setItemText(0, QtWidgets.QApplication.translate("Form", "0", None, -1))
        self.finish_min.setItemText(1, QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.finish_min.setItemText(2, QtWidgets.QApplication.translate("Form", "2", None, -1))
        self.finish_min.setItemText(3, QtWidgets.QApplication.translate("Form", "3", None, -1))
        self.finish_min.setItemText(4, QtWidgets.QApplication.translate("Form", "4", None, -1))
        self.finish_min.setItemText(5, QtWidgets.QApplication.translate("Form", "5", None, -1))
        self.finish_min.setItemText(6, QtWidgets.QApplication.translate("Form", "6", None, -1))
        self.finish_min.setItemText(7, QtWidgets.QApplication.translate("Form", "7", None, -1))
        self.finish_min.setItemText(8, QtWidgets.QApplication.translate("Form", "8", None, -1))
        self.finish_min.setItemText(9, QtWidgets.QApplication.translate("Form", "9", None, -1))
        self.finish_min.setItemText(10, QtWidgets.QApplication.translate("Form", "10", None, -1))
        self.finish_min.setItemText(11, QtWidgets.QApplication.translate("Form", "11", None, -1))
        self.finish_min.setItemText(12, QtWidgets.QApplication.translate("Form", "12", None, -1))
        self.finish_min.setItemText(13, QtWidgets.QApplication.translate("Form", "13", None, -1))
        self.finish_min.setItemText(14, QtWidgets.QApplication.translate("Form", "14", None, -1))
        self.finish_min.setItemText(15, QtWidgets.QApplication.translate("Form", "15", None, -1))
        self.finish_min.setItemText(16, QtWidgets.QApplication.translate("Form", "16", None, -1))
        self.finish_min.setItemText(17, QtWidgets.QApplication.translate("Form", "17", None, -1))
        self.finish_min.setItemText(18, QtWidgets.QApplication.translate("Form", "18", None, -1))
        self.finish_min.setItemText(19, QtWidgets.QApplication.translate("Form", "19", None, -1))
        self.finish_min.setItemText(20, QtWidgets.QApplication.translate("Form", "20", None, -1))
        self.finish_min.setItemText(21, QtWidgets.QApplication.translate("Form", "21", None, -1))
        self.finish_min.setItemText(22, QtWidgets.QApplication.translate("Form", "22", None, -1))
        self.finish_min.setItemText(23, QtWidgets.QApplication.translate("Form", "23", None, -1))
        self.finish_min.setItemText(24, QtWidgets.QApplication.translate("Form", "24", None, -1))
        self.finish_min.setItemText(25, QtWidgets.QApplication.translate("Form", "25", None, -1))
        self.finish_min.setItemText(26, QtWidgets.QApplication.translate("Form", "26", None, -1))
        self.finish_min.setItemText(27, QtWidgets.QApplication.translate("Form", "27", None, -1))
        self.finish_min.setItemText(28, QtWidgets.QApplication.translate("Form", "28", None, -1))
        self.finish_min.setItemText(29, QtWidgets.QApplication.translate("Form", "29", None, -1))
        self.finish_min.setItemText(30, QtWidgets.QApplication.translate("Form", "30", None, -1))
        self.finish_min.setItemText(31, QtWidgets.QApplication.translate("Form", "31", None, -1))
        self.finish_min.setItemText(32, QtWidgets.QApplication.translate("Form", "32", None, -1))
        self.finish_min.setItemText(33, QtWidgets.QApplication.translate("Form", "33", None, -1))
        self.finish_min.setItemText(34, QtWidgets.QApplication.translate("Form", "34", None, -1))
        self.finish_min.setItemText(35, QtWidgets.QApplication.translate("Form", "35", None, -1))
        self.finish_min.setItemText(36, QtWidgets.QApplication.translate("Form", "36", None, -1))
        self.finish_min.setItemText(37, QtWidgets.QApplication.translate("Form", "37", None, -1))
        self.finish_min.setItemText(38, QtWidgets.QApplication.translate("Form", "38", None, -1))
        self.finish_min.setItemText(39, QtWidgets.QApplication.translate("Form", "39", None, -1))
        self.finish_min.setItemText(40, QtWidgets.QApplication.translate("Form", "40", None, -1))
        self.finish_min.setItemText(41, QtWidgets.QApplication.translate("Form", "41", None, -1))
        self.finish_min.setItemText(42, QtWidgets.QApplication.translate("Form", "42", None, -1))
        self.finish_min.setItemText(43, QtWidgets.QApplication.translate("Form", "43", None, -1))
        self.finish_min.setItemText(44, QtWidgets.QApplication.translate("Form", "44", None, -1))
        self.finish_min.setItemText(45, QtWidgets.QApplication.translate("Form", "45", None, -1))
        self.finish_min.setItemText(46, QtWidgets.QApplication.translate("Form", "46", None, -1))
        self.finish_min.setItemText(47, QtWidgets.QApplication.translate("Form", "47", None, -1))
        self.finish_min.setItemText(48, QtWidgets.QApplication.translate("Form", "48", None, -1))
        self.finish_min.setItemText(49, QtWidgets.QApplication.translate("Form", "49", None, -1))
        self.finish_min.setItemText(50, QtWidgets.QApplication.translate("Form", "50", None, -1))
        self.finish_min.setItemText(51, QtWidgets.QApplication.translate("Form", "51", None, -1))
        self.finish_min.setItemText(52, QtWidgets.QApplication.translate("Form", "52", None, -1))
        self.finish_min.setItemText(53, QtWidgets.QApplication.translate("Form", "53", None, -1))
        self.finish_min.setItemText(54, QtWidgets.QApplication.translate("Form", "54", None, -1))
        self.finish_min.setItemText(55, QtWidgets.QApplication.translate("Form", "55", None, -1))
        self.finish_min.setItemText(56, QtWidgets.QApplication.translate("Form", "56", None, -1))
        self.finish_min.setItemText(57, QtWidgets.QApplication.translate("Form", "57", None, -1))
        self.finish_min.setItemText(58, QtWidgets.QApplication.translate("Form", "58", None, -1))
        self.finish_min.setItemText(59, QtWidgets.QApplication.translate("Form", "59", None, -1))
        self.comboBox_major.setItemText(0, QtWidgets.QApplication.translate("Form", "Accounting", None, -1))
        self.comboBox_major.setItemText(1, QtWidgets.QApplication.translate("Form", "Computer Science", None, -1))
        self.comboBox_major.setItemText(2, QtWidgets.QApplication.translate("Form", "Engineering", None, -1))
        self.comboBox_major.setItemText(3, QtWidgets.QApplication.translate("Form", "Business Administration", None, -1))
        self.comboBox_major.setItemText(4, QtWidgets.QApplication.translate("Form", "Sociology/Social Work", None, -1))
        self.comboBox_major.setItemText(5, QtWidgets.QApplication.translate("Form", "Mathematics/Statistics", None, -1))
        self.comboBox_major.setItemText(6, QtWidgets.QApplication.translate("Form", "Psychology", None, -1))
        self.comboBox_major.setItemText(7, QtWidgets.QApplication.translate("Form", "History/Political Science", None, -1))
        self.comboBox_major.setItemText(8, QtWidgets.QApplication.translate("Form", "Healthcare", None, -1))
        self.comboBox_major.setItemText(9, QtWidgets.QApplication.translate("Form", "Education", None, -1))
        self.comboBox_major.setItemText(10, QtWidgets.QApplication.translate("Form", "Environmental Science", None, -1))
        self.comboBox_major.setItemText(11, QtWidgets.QApplication.translate("Form", "Visual & Performing Arts", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Major field :", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
        self.label_29.setText(QtWidgets.QApplication.translate("Form", "*", None, -1))
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

