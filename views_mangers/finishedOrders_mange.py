from PyQt5 import QtWidgets , QtCore
from views import finishedOrders_view
import json
import os

class FinishedOrders(QtWidgets.QWidget, finishedOrders_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(FinishedOrders, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = FinishedOrders()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()