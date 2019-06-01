# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_main_screen.ui',
# licensing of 'User_main_screen.ui' applies.
#
# Created: Sat Jun  1 23:26:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 743)
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 648, 682))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_comapnyName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_comapnyName.setObjectName("lineEdit_comapnyName")
        self.horizontalLayout.addWidget(self.lineEdit_comapnyName)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_position = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.horizontalLayout_2.addWidget(self.lineEdit_position)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_salary = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_salary.setObjectName("lineEdit_salary")
        self.horizontalLayout_3.addWidget(self.lineEdit_salary)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.pushButton_commit_sen_method = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_commit_sen_method.setObjectName("pushButton_commit_sen_method")
        self.verticalLayout_3.addWidget(self.pushButton_commit_sen_method)
        self.radioButton_search_user_profile = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_search_user_profile.setObjectName("radioButton_search_user_profile")
        self.verticalLayout_3.addWidget(self.radioButton_search_user_profile)
        self.radioButton_search__keyword = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_search__keyword.setObjectName("radioButton_search__keyword")
        self.verticalLayout_3.addWidget(self.radioButton_search__keyword)
        self.radioButton_Show_all = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_Show_all.setObjectName("radioButton_Show_all")
        self.verticalLayout_3.addWidget(self.radioButton_Show_all)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 628, 184))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setStyleSheet("background-color: rgb(65,65,65);\n"
"color: rgb(0,0,0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pushButton_sendRequest = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_sendRequest.setObjectName("pushButton_sendRequest")
        self.horizontalLayout_8.addWidget(self.pushButton_sendRequest)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 628, 184))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_requested_job = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget_requested_job.setObjectName("tableWidget_requested_job")
        self.tableWidget_requested_job.setColumnCount(0)
        self.tableWidget_requested_job.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_requested_job)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
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
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Pathfinder", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Company Name:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Position:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Minimum Wedge(THB):", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "** Dont need to fill all details **", None, -1))
        self.pushButton_commit_sen_method.setText(QtWidgets.QApplication.translate("MainWindow", "Commit", None, -1))
        self.radioButton_search_user_profile.setText(QtWidgets.QApplication.translate("MainWindow", "Search by User Qualification", None, -1))
        self.radioButton_search__keyword.setText(QtWidgets.QApplication.translate("MainWindow", "Search By Key Word", None, -1))
        self.radioButton_Show_all.setText(QtWidgets.QApplication.translate("MainWindow", "Display All Job", None, -1))
        self.pushButton_sendRequest.setText(QtWidgets.QApplication.translate("MainWindow", "Send Request", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "All Requested Job", None, -1))
        self.menuMain.setTitle(QtWidgets.QApplication.translate("MainWindow", "Main", None, -1))
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

