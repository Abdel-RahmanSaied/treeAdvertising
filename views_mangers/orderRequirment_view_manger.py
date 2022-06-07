from PyQt5 import QtWidgets , QtCore
from views import orderRequirment_view
import json
import requests
import os
from PyQt5.QtWidgets import *


class OrderRequirment(QtWidgets.QWidget, orderRequirment_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OrderRequirment, self).__init__()
        self.setupUi(self)
        self.base_url = "https://saied.pythonanywhere.com/requirements/"
        self.token = ''


    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}

        self.reply = requests.get(self.base_url , headers=headers).json()
        print(self.reply)

        rowPosition = self.tableWidget.rowCount()
        counter = 0
        for rows in  self.reply :
            self.tableWidget.insertRow(rowPosition)
            # [{'id': 1, 'product_name': 'testP', 'user_name': 'mok11', 'quantity': 5, 'acceptable_by': 'not accepted', 'user_id': 2}]
            self.tableWidget.setItem(counter, 0, QTableWidgetItem(rows['product_name']))
            self.tableWidget.setItem(counter, 1, QTableWidgetItem(str(rows['quantity'])))
            self.tableWidget.setItem(counter, 2, QTableWidgetItem(rows['user_name']))
            counter+=1


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = OrderRequirment()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)