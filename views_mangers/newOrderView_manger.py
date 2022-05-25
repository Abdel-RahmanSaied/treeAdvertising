from PyQt5 import QtWidgets , QtCore
from views import newOrder_view
import json
import os

class NewOrderView_manger(QtWidgets.QWidget, newOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderView_manger, self).__init__()
        self.setupUi(self)

        self.clientDesign_btn.clicked.connect(self.getfiles)


    def getfiles(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')
        if len(self.fileName) != 0 :
            self.filaPath_lbl.setText(self.fileName)
            #self.checkAcceptedSignal.emit()
        else :
            self.filaPath_lbl.setText('مسار الملف ')

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderView_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()