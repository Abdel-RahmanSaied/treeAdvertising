from PyQt5 import QtWidgets , QtCore
from views import clients_view
from PyQt5.QtWidgets import *
import json
import requests
import os

class Clients(QtWidgets.QWidget, clients_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Clients, self).__init__()
        self.setupUi(self)
        self.base_url = "https://saied.pythonanywhere.com/clients/"
        self.token = ''

    def run(self):
        self.tableWidget.setRowCount(0)
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try :
            self.reply = requests.get(self.base_url , headers=headers).json()
        except Exception as s :
            print("ss",s)
        rowPosition = self.tableWidget.rowCount()
        try :
            for rows in self.reply:
                self.tableWidget.insertRow(rowPosition)
                # [{"id": 2,"name": "test","phone_number": "01011","notes": "nothing","clientlevel": "B"}]
                self.tableWidget.setItem(0, 0, QTableWidgetItem(rows['name']))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(rows['phone_number'])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(rows['clientlevel']))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(rows['notes']))

        except Exception as e :
            print(e)

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Clients()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)