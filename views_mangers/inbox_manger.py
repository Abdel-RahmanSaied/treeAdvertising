from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from views import inbox_view
import requests

class Inbox_manger(QtWidgets.QWidget, inbox_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    reload_signal = QtCore.pyqtSignal()
    alert_signal = QtCore.pyqtSignal()
    def __init__(self , name=None, *args, **kwargs ):
        super(Inbox_manger, self).__init__()
        self.setupUi(self)
        self.base_url = "https://saied.pythonanywhere.com/inbox_orders/"
        self.update_link = "https://saied.pythonanywhere.com/updateItem/"
        self.accept_order = "https://saied.pythonanywhere.com/updateAccept/"
        self.token = ''
        self.orderID = 0
        self.item_selected = False
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.details_btn.clicked.connect(self.orderDetails)
        self.end_btn.clicked.connect(self.end_order)
        self.reload_signal.connect(self.run)
        self.headers = {}

        self.user_name = ''

        self.accept_btn.clicked.connect(self.accept_state)

        self.inbox_count = 0
        self.index = 0

        # admin = True
        self.admin_check = False

    def selectionChanged(self):
        items = self.listWidget.selectedItems()
        #self.index = self.listWidget.currentIndex().row()
        for item in items:
            self.orderID = int(item.text())
            self.item_selected = True

    def run(self):
        msg = QtWidgets.QMessageBox()
        if self.admin_check == False :
            counter = 0
            self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                       'Authorization': f'Token {self.token}'}
            try :
                self.reply = requests.get(self.base_url , headers=self.headers).json()
            except Exception as s :
                print("ss",s)
            try :
                self.listWidget.clear()
                for element in self.reply:
                    self.listWidget.addItem(str(element['order_id']))
                    if element['accepted_by'] == "Not Accepted yet" :
                        item = self.listWidget.item(counter)
                        item.setForeground(QtGui.QColor("red"))
                        #item.setBackground(QtGui.QColor("red"))
                    counter +=1
                self.checkAcceptedSignal.emit()
            except Exception as e :
                print(e)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you don't have any inbox !")
            msg.exec_()


    def orderDetails(self):
        msg = QtWidgets.QMessageBox()
        if self.item_selected != False :
            self.checkAcceptedSignal.emit()
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()

    def accept_state(self):
        msg = QtWidgets.QMessageBox()
        data = {"accepted_by" : self.user_name}
        if self.item_selected != False:
            try :
                self.reply = requests.put(f"{self.accept_order}{self.orderID}//" , json=data , headers=self.headers).json()
                response = self.reply['Response']
                #print(response)
                if response == "You don't have permission to update this." :
                    msg.setWindowTitle("Warning")
                    msg.setText(f"{response}by {self.user_name}")
                    msg.exec_()
                else:
                    # item = self.listWidget.item(self.index)
                    # item.setBackground(QtGui.QColor("red"))
                    msg.setWindowTitle("Warning")
                    msg.setText(response)
                    msg.exec_()
                    self.reload_signal.emit()
            except Exception as s:
                print("ss",s)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("you must select the order !")
            msg.exec_()

    def end_order(self):
        msg = QtWidgets.QMessageBox()
        data = {"state" : "F"}
        if self.item_selected != False:
            try :
                self.reply = requests.put(f"{self.update_link}{self.orderID}//" , json=data , headers=self.headers).json()
                print(self.reply)
                response = self.reply['Response']
                if response == "You don't have permission to delete this." :
                    msg.setWindowTitle("Warning")
                    msg.setText(response)
                    msg.exec_()
                else:
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

    def check_inbox(self):
        self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try :
            reply_check = requests.get(self.base_url , headers=self.headers).json()
            #print(reply_check)
            try :
                if reply_check['Response'] == "You don't have any orders" :
                    self.admin_check = True
            except :
                self.admin_check = False

        except Exception as s :
            print("ss",s)
        try :
            reply_count = len(reply_check)
        except Exception as d :
            print(d)
        try :
            if self.inbox_count == 0 :
                self.inbox_count = reply_count
            elif self.inbox_count != reply_count :
                self.alert_signal.emit()
                self.inbox_count = reply_count
        except Exception as r :
            print(r)




if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Inbox_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()