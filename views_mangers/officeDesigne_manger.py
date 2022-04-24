from PyQt5 import QtWidgets , QtCore
from views import officeDesigne_view
import json
import os

class OfficeDesigne(QtWidgets.QWidget, officeDesigne_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OfficeDesigne, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = OfficeDesigne()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()