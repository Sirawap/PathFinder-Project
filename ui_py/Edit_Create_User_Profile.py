# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit_Create_User_Profile.ui',
# licensing of 'Edit_Create_User_Profile.ui' applies.
#
# Created: Fri May 31 14:18:53 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 631)
        Form.setStyleSheet("QWidget{\n"
"    background-image: url(:/bg/grey.png);\n"
"    color: white\n"
"}\n"
"\n"
"QComboBox{    \n"
"    background-color: rgb(65, 65, 65);\n"
"}url(:/bg/grey.png)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 579, 611))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_5.addWidget(self.lineEdit_name)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_name_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_name_2.setObjectName("lineEdit_name_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_name_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_userTel = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_userTel.setObjectName("lineEdit_userTel")
        self.horizontalLayout_6.addWidget(self.lineEdit_userTel)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_name_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_name_3.setObjectName("lineEdit_name_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_name_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_23.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_name_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_name_4.setObjectName("lineEdit_name_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_name_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_23.addLayout(self.verticalLayout_3)
        self.horizontalLayout_23.setStretch(0, 5)
        self.horizontalLayout_23.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_23)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.comboBox_degree = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_degree.setObjectName("comboBox_degree")
        self.comboBox_degree.addItem("")
        self.comboBox_degree.addItem("")
        self.comboBox_degree.addItem("")
        self.comboBox_degree.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_degree)
        self.horizontalLayout_19.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_6.addWidget(self.label_19)
        self.comboBox_subject = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_subject.setObjectName("comboBox_subject")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.comboBox_subject.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_subject)
        self.horizontalLayout_19.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.lineEdit_major = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_major.setText("")
        self.lineEdit_major.setObjectName("lineEdit_major")
        self.verticalLayout_7.addWidget(self.lineEdit_major)
        self.horizontalLayout_19.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_8.addWidget(self.label_24)
        self.lineEdit_university = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_university.setText("")
        self.lineEdit_university.setObjectName("lineEdit_university")
        self.verticalLayout_8.addWidget(self.lineEdit_university)
        self.horizontalLayout_19.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.register_language = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.register_language.setObjectName("register_language")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.register_language.addItem("")
        self.horizontalLayout_20.addWidget(self.register_language)
        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_21.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_21.addWidget(self.pushButton)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)
        self.verticalLayout_9.addLayout(self.horizontalLayout_22)
        self.scrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 557, 310))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        spacerItem1 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_2.addWidget(self.label_23)
        spacerItem4 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidget_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem7)
        self.pushButton_cancle_profile = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_cancle_profile.setObjectName("pushButton_cancle_profile")
        self.horizontalLayout_24.addWidget(self.pushButton_cancle_profile)
        self.pushButton_confirm_profile = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_confirm_profile.setObjectName("pushButton_confirm_profile")
        self.horizontalLayout_24.addWidget(self.pushButton_confirm_profile)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Edit Profile", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Name:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Surname:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Tel:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "E-mail:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Age:", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "Education Background", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "Education degree:", None, -1))
        self.comboBox_degree.setItemText(0, QtWidgets.QApplication.translate("Form", "Associate degree ", None, -1))
        self.comboBox_degree.setItemText(1, QtWidgets.QApplication.translate("Form", "Bachelor\'s degree ", None, -1))
        self.comboBox_degree.setItemText(2, QtWidgets.QApplication.translate("Form", "Master\'s degree", None, -1))
        self.comboBox_degree.setItemText(3, QtWidgets.QApplication.translate("Form", "Doctoral degree", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "Subject:", None, -1))
        self.comboBox_subject.setItemText(0, QtWidgets.QApplication.translate("Form", " -- None --", None, -1))
        self.comboBox_subject.setItemText(1, QtWidgets.QApplication.translate("Form", "Accounting", None, -1))
        self.comboBox_subject.setItemText(2, QtWidgets.QApplication.translate("Form", "Computer Science", None, -1))
        self.comboBox_subject.setItemText(3, QtWidgets.QApplication.translate("Form", "Engineering", None, -1))
        self.comboBox_subject.setItemText(4, QtWidgets.QApplication.translate("Form", "Business Administration", None, -1))
        self.comboBox_subject.setItemText(5, QtWidgets.QApplication.translate("Form", "Sociology/Social Work", None, -1))
        self.comboBox_subject.setItemText(6, QtWidgets.QApplication.translate("Form", "Mathematics/Statistics", None, -1))
        self.comboBox_subject.setItemText(7, QtWidgets.QApplication.translate("Form", "Psychology", None, -1))
        self.comboBox_subject.setItemText(8, QtWidgets.QApplication.translate("Form", "History/Political Science", None, -1))
        self.comboBox_subject.setItemText(9, QtWidgets.QApplication.translate("Form", "Healthcare", None, -1))
        self.comboBox_subject.setItemText(10, QtWidgets.QApplication.translate("Form", "Education", None, -1))
        self.comboBox_subject.setItemText(11, QtWidgets.QApplication.translate("Form", "Environmental Science", None, -1))
        self.comboBox_subject.setItemText(12, QtWidgets.QApplication.translate("Form", "Visual & Performing Arts", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "Major:", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Form", "University:", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Form", "Language :", None, -1))
        self.register_language.setItemText(0, QtWidgets.QApplication.translate("Form", " -- None -- ", None, -1))
        self.register_language.setItemText(1, QtWidgets.QApplication.translate("Form", "Arab", None, -1))
        self.register_language.setItemText(2, QtWidgets.QApplication.translate("Form", "Chinese", None, -1))
        self.register_language.setItemText(3, QtWidgets.QApplication.translate("Form", "English", None, -1))
        self.register_language.setItemText(4, QtWidgets.QApplication.translate("Form", "French", None, -1))
        self.register_language.setItemText(5, QtWidgets.QApplication.translate("Form", "Indian", None, -1))
        self.register_language.setItemText(6, QtWidgets.QApplication.translate("Form", "Japanese", None, -1))
        self.register_language.setItemText(7, QtWidgets.QApplication.translate("Form", "Korean", None, -1))
        self.register_language.setItemText(8, QtWidgets.QApplication.translate("Form", "Russian", None, -1))
        self.register_language.setItemText(9, QtWidgets.QApplication.translate("Form", "Spanish", None, -1))
        self.register_language.setItemText(10, QtWidgets.QApplication.translate("Form", "Thai", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Add Language", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Add Education Background", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("Form", "Language :", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Delete", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "Education:", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "Delete", None, -1))
        self.pushButton_cancle_profile.setText(QtWidgets.QApplication.translate("Form", "Cancle", None, -1))
        self.pushButton_confirm_profile.setText(QtWidgets.QApplication.translate("Form", "Confirm", None, -1))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

