import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import ui_py.temp_table_widget
import src.temp2UI

class temp(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.temp_table_widget.Ui_Form()
        self.ui.setupUi(self)



        self.data = [["1.","Bill",'n','20','069696969'],["2.","Jia",'S','20','09696969696']]
        # model = QStandardItemModel()
        # model.setHorizontalHeaderLabels(['No','Name','Surname','age','tel'])

        style = "::section {""background-color: gray;" \
                "color: red; }"
        self.ui.tableWidget.horizontalHeader().setStyleSheet(style)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setColumnWidth(4,500)
        self.ui.tableWidget.setRowCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['No','Name','Surname','age','tel'])


        self.ui.combobox.setCurrentIndex(self.ui.combobox)


        # rowPosition = self.ui.tableWidget.rowCount()
        # self.ui.tableWidget.insertRow(0)
        # self.ui.tableWidget.insertRow(1)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(self.data[i][j]))


        self.ui.tableWidget.doubleClicked.connect(self.itemclick)

        self.ui.pushButton.clicked.connect(self.openNewWidget) ###look at here



    def itemclick(self):
        print("popo")
        # x = self.data[column]
        # self.ui.tableWidget.removeRow(row)
        # print('No :', x[0])
        # print('Name :', x[1])
        # print('Surname :', x[2])
        # print('Age :', x[3])
        # print('Tel :', x[4])
        #change print to  write in database

    def openNewWidget(self):###look at here
        self.temp2 = src.temp2UI.temp2()
        self.temp2.show()

        self.temp2.ui.pushButton.clicked.connect(self.refresh)###look at here

    def refresh(self):###look at here
        print("fuck")
        self.temp2.close()




if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # w = temp()
    # w.show()
    #
    # sys.exit(app.exec_())
    sr = "12.2"

    if sr.is:
        print("poop")
