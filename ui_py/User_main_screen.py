# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_main_screen.ui',
# licensing of 'User_main_screen.ui' applies.
#
# Created: Sat Jun  1 12:34:05 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 634)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"QScrollArea{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 681, 561))
        self.scrollArea.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"QTableWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: black;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(240, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setGeometry(QtCore.QRect(100, 170, 91, 17))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(560, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setGeometry(QtCore.QRect(380, 170, 161, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 170, 121, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 111, 641, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(250, 140, 211, 16))
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 21))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 200, 581, 331))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 579, 329))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 581, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(65,65,65);\n"
"color: rgb(0,0,0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuJob_Negotiate = QtWidgets.QMenu(self.menubar)
        self.menuJob_Negotiate.setObjectName("menuJob_Negotiate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_Out = QtWidgets.QAction(MainWindow)
        self.actionLog_Out.setCheckable(False)
        self.actionLog_Out.setChecked(False)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.actionEdit_Profile = QtWidgets.QAction(MainWindow)
        self.actionEdit_Profile.setObjectName("actionEdit_Profile")
        self.actionView_Profile = QtWidgets.QAction(MainWindow)
        self.actionView_Profile.setObjectName("actionView_Profile")
        self.actionView_Sended_Job_Request = QtWidgets.QAction(MainWindow)
        self.actionView_Sended_Job_Request.setObjectName("actionView_Sended_Job_Request")
        self.actionView_Reply_Tray = QtWidgets.QAction(MainWindow)
        self.actionView_Reply_Tray.setObjectName("actionView_Reply_Tray")
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionLog_Out)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionEdit_Profile)
        self.menuMain.addAction(self.actionView_Profile)
        self.menuMain.addSeparator()
        self.menuJob_Negotiate.addAction(self.actionView_Sended_Job_Request)
        self.menuJob_Negotiate.addAction(self.actionView_Reply_Tray)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuJob_Negotiate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Pathfinder", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Display All Job", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Commit", None, -1))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Search by User Qualification", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Search By Key Word", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Company Name:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Position:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Minimum Wedge(THB):", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "** Dont need to fill all details **", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Company", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Job name", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Position", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Salary", None, -1))
        self.menuMain.setTitle(QtWidgets.QApplication.translate("MainWindow", "Main", None, -1))
        self.menuJob_Negotiate.setTitle(QtWidgets.QApplication.translate("MainWindow", "Job Negotiate", None, -1))
        self.actionLog_Out.setText(QtWidgets.QApplication.translate("MainWindow", "Log Out", None, -1))
        self.actionEdit_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "Edit Profile", None, -1))
        self.actionView_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "View Profile", None, -1))
        self.actionView_Sended_Job_Request.setText(QtWidgets.QApplication.translate("MainWindow", "View Sended Job Request", None, -1))
        self.actionView_Reply_Tray.setText(QtWidgets.QApplication.translate("MainWindow", "View Reply Tray", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

