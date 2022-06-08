from PyQt5 import QtWidgets , QtCore
from views import orderDetails_view
import json
import requests
import os

class OrderDetails(QtWidgets.QWidget, orderDetails_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OrderDetails, self).__init__()
        self.setupUi(self)
        self.base_url = "https://saied.pythonanywhere.com/orders/"
        self.token = ''

        self.order_id = 1
    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        # [{'order_id': 1, 'user_name': 'mok11', 'date': '2022-06-05', 'recived_date': '2022-05-28', 'delivery_date': '2022-09-28', 'design_types': 'A', 'design_path': 'teeeeeeeeest', 'design_category': ['x'], 'printing_type': ['x'], 'size_width': 56.0, 'size_high': 645.0, 'materials': 'eeee', 'color': 'eeee', 'thickness': 12.2, 'Post_print_services': ['x'], 'state': 'I', 'notes': 'asd', 'user_id': 2, 'client_id': 2}]
        try :
            self.reply = requests.get(self.base_url , headers=headers).json()
        except Exception as s :
            print("ss",s)
        try :
            for item in self.reply :
                if item['order_id'] == self.order_id :
                    self.clientName_lbl.setText("xxxx")
                    self.orderID_lbl.setText(str(item["order_id"]))
                    self.date_lbl.setText(str(item['date']))
                    self.recived_date_lbl.setText(item['recived_date'])
                    self.print_type_lbl.setText(str(item['design_types']))
                    self.sevices_afterPrinting_lbl.setText(str(item['Post_print_services']))
                    self.notes_lbl.setText((item['notes']))

        except Exception as e:
            print(e)

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = OrderDetails()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()