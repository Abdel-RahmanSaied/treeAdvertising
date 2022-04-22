from PyQt5 import QtWidgets , QtCore
from views import newOrderData_view
import json
import os

class NewOrderDataView_manger(QtWidgets.QWidget, newOrderData_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderDataView_manger, self).__init__()
        self.setupUi(self)
        self.clientDesign_btn.clicked.connect(self.getfiles)

    def clear_File_path(self):
        self.fileName = ""
    def clear_warning(self):
        self.warning_lbl.setText("")

    def getfiles(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')

        if len(self.fileName) != 0 :
            self.filaPath_lbl.setText(self.fileName)
        else :
            self.filaPath_lbl.setText('مسار الملف ')

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderDataView_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()