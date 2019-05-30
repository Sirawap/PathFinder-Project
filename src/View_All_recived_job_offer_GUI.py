from PySide2.QtWidgets import *
import ui_py.View_All_recived_job_offer

class View_All_Reply(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = ui_py.View_All_recived_job_offer.Ui_Form()
        self.ui.setupUi(self)
