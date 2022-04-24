from PyQt5 import QtWidgets , QtCore
from views import officeDesign_view
import json
import os

class OfficeDesign(QtWidgets.QWidget, officeDesign_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OfficeDesign, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = OfficeDesign()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()