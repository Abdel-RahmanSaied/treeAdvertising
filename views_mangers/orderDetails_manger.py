from PyQt5 import QtWidgets , QtCore
from views import orderDetails_view
import json
import os

class OrderDetails(QtWidgets.QWidget, orderDetails_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OrderDetails, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = OrderDetails()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()