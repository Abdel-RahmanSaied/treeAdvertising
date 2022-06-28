from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextTableFormat, QTextLength, QFont

from views import followOrder_view
import json
import requests
import os
import pandas as pd
from jinja2 import Template

class FollowOrder(QtWidgets.QWidget, followOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    reload_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(FollowOrder, self).__init__()
        self.setupUi(self)

        self.base_url = "https://saied.pythonanywhere.com/getUnfinishedOrders/"
        self.update_link = "https://saied.pythonanywhere.com/updateItem/"
        self.delete_link = "https://saied.pythonanywhere.com/deleteitem/"
        self.searchByDate_url = "https://saied.pythonanywhere.com/searchByDate/"
        self.token = ''
        self.orderID = 0
        self.orders = []
        self.item_selected = False
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)

        self.details_btn.clicked.connect(self.orderDetails)
        self.end_btn.clicked.connect(self.end_order)
        self.delete_btn.clicked.connect(self.delete_order)
        self.next_btn.clicked.connect(self.search)
        self.reload_signal.connect(self.run)
        self.print_btn.clicked.connect(self.print_order)

        self.headers = {}

    def search(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                        'Authorization': f'Token {self.token}'}
        from_date = self.dateEdit.text()
        to_date= self.dateEdit_2.text()
        data = {
                "from_date": from_date,
                "to_date": to_date,
                "state": "all"
                }
        try:
            self.search_reply = requests.post(self.searchByDate_url, json=data, headers=headers).json()
            self.listWidget.clear()
            for element in self.search_reply:
                self.listWidget.addItem(str(element['order_id']))
        except Exception as d:
            print("dd",d)

    def print_order(self):
        msg = QtWidgets.QMessageBox()
        if self.item_selected != False:
            try:
                for item in self.orders:
                    if item['order_id'] == self.orderID:
                        pd_object = pd.DataFrame.from_dict(item, orient='index')
                        df = pd.DataFrame(pd_object)
                        df.drop(['user_id', 'client_id'], inplace=True)

                        # print(df)
                        dialog = QtPrintSupport.QPrintDialog()
                        if dialog.exec_() == QtWidgets.QDialog.Accepted:
                            tableFormat = QTextTableFormat()
                            tableFormat.setAlignment(QtCore.Qt.AlignVCenter) # Justify Table
                            tableFormat.setBackground(QtGui.QColor('#e0e0e0'))
                            tableFormat.setCellPadding(10)
                            tableFormat.setCellSpacing(0)
                            tableFormat.setBorder(1)
                            tableFormat.setWidth(QTextLength(QTextLength.PercentageLength, 100))
                            document = QtGui.QTextDocument()
                            cursor = QtGui.QTextCursor(document)
                            table = cursor.insertTable( df.count(), 2, tableFormat)
                            # format = table.format()
                            format = table.format()
                            format.setHeaderRowCount(0)
                            table.setFormat(format)
                            format = cursor.blockCharFormat()
                            format.setFontWeight(QFont.Bold)
                            for row, col in df.iterrows():
                                for value in [row, col[0]]:
                                    cursor.setCharFormat(format)
                                    cursor.insertText(str(value))
                                    cursor.movePosition(QtGui.QTextCursor.NextCell)

                            cell = table.cellAt(1, 0)

                        document.print_(dialog.printer())

            except Exception as e:
                print(e)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()


    def run(self):
        self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try :
            self.reply = requests.get(self.base_url , headers=self.headers).json()
            self.orders = self.reply
        except Exception as s :
            print("ss",s)
        try :
            self.listWidget.clear()
            for element in  self.reply:
                self.listWidget.addItem(str(element['order_id']))
        except Exception as e :
            print(e)
    def selectionChanged(self):
        items = self.listWidget.selectedItems()
        for item in items:
            self.orderID = int(item.text())
            self.item_selected = True
    def orderDetails(self):
        msg = QtWidgets.QMessageBox()
        if self.item_selected != False :
            self.checkAcceptedSignal.emit()
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()
    def end_order(self):
        msg = QtWidgets.QMessageBox()
        data = {"state" : "F"}
        if self.item_selected != False:
            try :
                self.reply = requests.put(f"{self.update_link}{self.orderID}//" , json=data , headers=self.headers)
                self.reload_signal.emit()
                msg.setWindowTitle("Warning")
                msg.setText("order state updated to finished !")
                msg.exec_()
            except Exception as s :
                print("ss",s)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()
    def delete_order(self):
        msg = QtWidgets.QMessageBox()
        if self.item_selected != False:
            try :
                self.reply = requests.delete(f"{self.delete_link}{self.orderID}//" , headers=self.headers).json()
                response = self.reply["Response"]
                msg.setWindowTitle("Warning")
                msg.setText(response)
                msg.exec_()
                self.reload_signal.emit()
            except Exception as s :
                print("ss",s)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = FollowOrder()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()