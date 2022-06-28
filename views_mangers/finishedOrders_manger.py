from PyQt5 import QtWidgets , QtCore
from views import finishedOrders_view
from PyQt5.QtWidgets import *
import json
import os
import requests

class FinishedOrders(QtWidgets.QWidget, finishedOrders_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(FinishedOrders, self).__init__()
        self.setupUi(self)
        self.base_url = "https://saied.pythonanywhere.com/orders/"
        self.searchByDate_url = "https://saied.pythonanywhere.com/searchByDate/"
        self.token = ''
        self.tableWidget.verticalHeader().setVisible(False)
        #self.orderID = 0
        self.orders = []
        self.next_btn.clicked.connect(self.search)

    def search(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                        'Authorization': f'Token {self.token}'}
        from_date = self.dateEdit.text()
        to_date = self.dateEdit_2.text()
        data = {
                "from_date": from_date,
                "to_date": to_date,
                "state": "finished"
                }
        try:
            search_reply = requests.post(self.searchByDate_url, json=data, headers=headers).json()
            print(search_reply)
            self.tableWidget.setRowCount(0)
            rowPosition = self.tableWidget.rowCount()
            for rows in search_reply:
                try:
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(str(rows['order_id'])))
                    self.tableWidget.setItem(0, 1, QTableWidgetItem(str(rows['user_name'])))
                    self.tableWidget.setItem(0, 2, QTableWidgetItem(str(rows['accepted_by'])))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem(str(rows['client_name'])))
                    self.tableWidget.setItem(0, 4, QTableWidgetItem(str(rows['img_path'])))
                    self.tableWidget.setItem(0, 5, QTableWidgetItem(str(rows['date'])))
                    self.tableWidget.setItem(0, 6, QTableWidgetItem(str(rows['recived_date'])))
                    self.tableWidget.setItem(0, 7, QTableWidgetItem(str(rows['delivery_date'])))
                    self.tableWidget.setItem(0, 8, QTableWidgetItem(str(rows['design_types'])))
                    self.tableWidget.setItem(0, 9, QTableWidgetItem(str(rows['design_path'])))
                    self.tableWidget.setItem(0, 10, QTableWidgetItem(str(rows['design_category'])))
                    self.tableWidget.setItem(0, 11, QTableWidgetItem(str(rows['printing_type'])))
                    self.tableWidget.setItem(0, 12, QTableWidgetItem(str(rows['size_width'])))
                    self.tableWidget.setItem(0, 13, QTableWidgetItem(str(rows['size_high'])))
                    self.tableWidget.setItem(0, 14, QTableWidgetItem(str(rows['materials'])))
                    self.tableWidget.setItem(0, 15, QTableWidgetItem(str(rows['color'])))
                    self.tableWidget.setItem(0, 16, QTableWidgetItem(str(rows['thickness'])))
                    self.tableWidget.setItem(0, 17, QTableWidgetItem(str(rows['Post_print_services'])))
                    self.tableWidget.setItem(0, 18, QTableWidgetItem(str(rows['target_dapertment'])))
                    self.tableWidget.setItem(0, 19, QTableWidgetItem(str(rows['notes'])))
                except Exception as e:
                    print(e)
        except Exception as d:
            print("dd",d)

    def run(self):
        self.tableWidget.setRowCount(0)
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try:
            self.reply = requests.get(self.base_url , headers=headers).json()
            # print(self.reply)
        except Exception as s :
            print("ss",s)

        rowPosition = self.tableWidget.rowCount()
        for rows in  self.reply :
            if rows["state"] == "F" :

                try:
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(str(rows['order_id'])))
                    self.tableWidget.setItem(0, 1, QTableWidgetItem(str(rows['user_name'])))
                    self.tableWidget.setItem(0, 2, QTableWidgetItem(str(rows['accepted_by'])))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem(str(rows['client_name'])))
                    self.tableWidget.setItem(0, 4, QTableWidgetItem(str(rows['img_path'])))
                    self.tableWidget.setItem(0, 5, QTableWidgetItem(str(rows['date'])))
                    self.tableWidget.setItem(0, 6, QTableWidgetItem(str(rows['recived_date'])))
                    self.tableWidget.setItem(0, 7, QTableWidgetItem(str(rows['delivery_date'])))
                    self.tableWidget.setItem(0, 8, QTableWidgetItem(str(rows['design_types'])))
                    self.tableWidget.setItem(0, 9, QTableWidgetItem(str(rows['design_path'])))
                    self.tableWidget.setItem(0, 10, QTableWidgetItem(str(rows['design_category'])))
                    self.tableWidget.setItem(0, 11, QTableWidgetItem(str(rows['printing_type'])))
                    self.tableWidget.setItem(0, 12, QTableWidgetItem(str(rows['size_width'])))
                    self.tableWidget.setItem(0, 13, QTableWidgetItem(str(rows['size_high'])))
                    self.tableWidget.setItem(0, 14, QTableWidgetItem(str(rows['materials'])))
                    self.tableWidget.setItem(0, 15, QTableWidgetItem(str(rows['color'])))
                    self.tableWidget.setItem(0, 16, QTableWidgetItem(str(rows['thickness'])))
                    self.tableWidget.setItem(0, 17, QTableWidgetItem(str(rows['Post_print_services'])))
                    self.tableWidget.setItem(0, 18, QTableWidgetItem(str(rows['target_dapertment'])))
                    self.tableWidget.setItem(0, 19, QTableWidgetItem(str(rows['notes'])))
                except Exception as e:
                    print(e)



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = FinishedOrders()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(15, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeToContents)
# header.setSectionResizeMode(19, QtWidgets.QHeaderView.Stretch)