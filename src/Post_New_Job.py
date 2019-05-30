from PySide2.QtWidgets import *
import ui_py.Create_Job_Criteria_UI

class Post_New_Job(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.Create_Job_Criteria_UI.Ui_Form()
        self.ui.setupUi(self)
