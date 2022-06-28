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

        try :
            self.reply = requests.get(self.base_url , headers=headers).json()
        except Exception as s :
            print("ss",s)
        try :
            for item in self.reply :
                if item['order_id'] == self.order_id :
                    print(item)
                    self.clientName_lbl.setText(item["client_name"])
                    self.orderID_lbl.setText(str(item["order_id"]))
                    self.date_lbl.setText(str(item['date']))
                    self.recived_date_lbl.setText(item['recived_date'])
                    self.deliver_date_lbl.setText(item["delivery_date"])
                    self.userName_lbl.setText(item["accepted_by"])
                    if str(item['target_dapertment']) == "['D']" :
                        self.department_lbl.setText("قسم الديزاين")
                    elif str(item['target_dapertment']) == "['P']" :
                        self.department_lbl.setText("قسم الطباعه")
                    else:
                        self.department_lbl.setText("قسم التصميم و الطباعه")

                    if item['state'] == 'D' :
                        self.state_lbl.setText("Ideal")
                    elif item['state'] == "I" :
                        self.state_lbl.setText("In progress")
                    else :
                        self.state_lbl.setText("Finished")

                    if item["design_types"] == "A" :
                        self.desigTybe_lbl.setText("تصميم مرفق")
                    if item["design_types"] == "O" :
                        self.desigTybe_lbl.setText("تصميم مكتب")
                    self.filePath_lbl.setText(item["design_path"])

                    design_category = '\n'.join(item["design_category"])
                    self.design_types_lbl.setText(design_category)

                    printing_type = '\n'.join(item['printing_type'])
                    self.print_type_lbl.setText(printing_type)

                    self.material_lbl.setText(item["materials"])

                    Post_print_services = '\n'.join(item['Post_print_services'])
                    self.sevices_afterPrinting_lbl.setText(Post_print_services)
                    self.width_lbl.setText(str(item['size_width']))
                    self.high_lbl.setText(str(item['size_high']))
                    self.color_lbl.setText(item['color'])
                    self.thinkness_lbl.setText(str(item['thickness']))

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