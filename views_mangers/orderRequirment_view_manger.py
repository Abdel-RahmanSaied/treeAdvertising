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
        self.delete_url = "https://saied.pythonanywhere.com/deleteRequirement/"
        self.update_link = "https://saied.pythonanywhere.com/updateRequiredItem/"
        self.accept_url = "https://saied.pythonanywhere.com/acceptRequirement/"
        self.token = ''
        self.userName = ''
        self.tableWidget.verticalHeader().setVisible(False)
        self.id = -1
        self.tableWidget.selectionModel().selectionChanged.connect(self.selected_order)
        self.delete_btn.clicked.connect(self.delete_requirement)
        self.details_btn.clicked.connect(self.end_order)

    def selected_order(self, selected):
        row = 0
        for index in selected.indexes():
            row = index.row()
        index = self.tableWidget.model().index(row, 0)
        self.id = self.tableWidget.model().data(index)


    def delete_requirement(self):
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        msg = QtWidgets.QMessageBox()
        if self.id == -1:
            msg.setWindowTitle("Warning")
            msg.setText("No client was selected !")
            msg.exec_()
        else:
            try:
                self.delete_response = requests.delete(rf"{self.delete_url}{self.id}//", headers=headers).json()
                response = self.delete_response["Response"]
                self.run()
                msg.setWindowTitle("Response")
                msg.setText(response)
                msg.exec_()
                self.id = -1
            except Exception as e:
                print(e)


    def run(self):
        self.tableWidget.setRowCount(0)
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try:
            self.reply = requests.get(self.base_url , headers=headers).json()
        except Exception as s :
            print("ss",s)

        rowPosition = self.tableWidget.rowCount()
        for rows in  self.reply :
            try:
                self.tableWidget.insertRow(rowPosition)
                # [{'id': 1, 'product_name': 'testP', 'user_name': 'mok11', 'quantity': 5, 'acceptable_by': 'not accepted', 'user_id': 2}]
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(rows['id'])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(rows['product_name']))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(rows['quantity'])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(rows['user_name']))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(rows['acceptable_by']))
            except Exception as e:
                print(e)

    def end_order(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json','Authorization': f'Token {self.token}'}
        data = {"acceptable_by": self.userName}
        if self.id != -1:
            try:
                reply = requests.put(f"{self.accept_url}{self.id}//", json=data, headers=headers).json()
                response = reply["Response"]
                msg.setWindowTitle("Warning")
                msg.setText(response)
                msg.exec_()
                self.id = -1
                self.run()
            except Exception as s:
                print("ss", s)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = OrderRequirment()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)