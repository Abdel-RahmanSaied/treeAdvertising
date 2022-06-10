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
        self.delete_url = "https://saied.pythonanywhere.com/deleteClient/"
        self.token = ''
        self.tableWidget.verticalHeader().setVisible(False)
        self.id = -1
        self.tableWidget.selectionModel().selectionChanged.connect(self.selected_client)
        self.delete_btn.clicked.connect(self.delete_client)

    def selected_client(self, selected):
        row = 0
        for index in selected.indexes():
            row = index.row()
        index = self.tableWidget.model().index(row, 0)
        self.id = self.tableWidget.model().data(index)
        # print(f"id : {id} ")

    def delete_client(self):
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json','Authorization': f'Token {self.token}'}
        msg = QtWidgets.QMessageBox()
        if self.id == -1:
            msg.setWindowTitle("Warning")
            msg.setText("No client was selected !")
            msg.exec_()
        else:
            try:
                self.delete_response = requests.delete(rf"{self.delete_url}{self.id}//", headers=headers).json()
                self.response = self.delete_response["Response"]
                self.run()
                msg.setWindowTitle("Response")
                msg.setText(self.response)
                msg.exec_()

            except Exception as e:
                print(e)

    def run(self):
        self.tableWidget.setRowCount(0)
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try :
            self.delete_response = requests.get(self.base_url, headers=headers).json()
        except Exception as s :
            print("ss",s)
        rowPosition = self.tableWidget.rowCount()
        try :
            for rows in self.delete_response:
                self.tableWidget.insertRow(rowPosition)
                # [{"id": 2,"name": "test","phone_number": "01011","notes": "nothing","clientlevel": "B"}]
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(rows['id'])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(rows['name']))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(rows['phone_number'])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(rows['clientlevel']))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(rows['notes']))
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
# header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)