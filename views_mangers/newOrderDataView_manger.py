from PyQt5 import QtWidgets , QtCore
from views import newOrderData_view
import json
import os

class NewOrderDataView_manger(QtWidgets.QWidget, newOrderData_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderDataView_manger, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderDataView_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()