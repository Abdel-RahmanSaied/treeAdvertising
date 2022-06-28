from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from views_mangers.loginView_manger import Login_Manager
from views_mangers.main_manger import Main_manger
from views_mangers.newOrderView_manger import NewOrderView_manger
from views_mangers.clients_manger import Clients
from views_mangers.add_client_manger import AddClients
from views_mangers.followOrder_manger import FollowOrder
from views_mangers.finishedOrders_manger import FinishedOrders
from views_mangers.orderDetails_manger import OrderDetails
from views_mangers.editOrder_manger import EditOrderView_manger
from views_mangers.orderRequirment_view_manger import OrderRequirment
from views_mangers.add_requirement_manger import AddRequirement
from views_mangers.inbox_manger import Inbox_manger
from views_mangers.user_registration_manger import Registration_manger

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot

import os
import time
import datetime
from threading import Timer

from playsound import playsound


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
            # Inbox_manger().check_inbox()


class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget ):
        super().__init__(widget)
        self._widget = widget

        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)
    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)

class Tree_Advertising(QtWidgets.QStackedWidget):
    def __init__(self , name=None, *args, **kwargs ):
        super(Tree_Advertising, self).__init__()

        self.login_manger = Login_Manager()
        self.main_manger = Main_manger()
        self.newOrder_manger=NewOrderView_manger()
        self.followOrder_manger = FollowOrder()
        self.finishedOrders_manger = FinishedOrders()
        self.orderDetails_manger = OrderDetails()
        self.orderRequirment_manger = OrderRequirment()
        self.clients_manger = Clients()
        self.addClient_manger = AddClients()
        self.inbox_manger = Inbox_manger()
        self.addRequirement_manger = AddRequirement()
        self.userRegister_manger = Registration_manger()
        self.editOrder_manger = EditOrderView_manger()

        #self.showFullScreen()


        # add widgets to the stack
        self.addWidget(self.login_manger) #0 done
        self.addWidget(self.main_manger) #1 done
        self.addWidget(self.newOrder_manger) #2 ***
        self.addWidget(self.followOrder_manger)  #3  !!!
        self.addWidget(self.finishedOrders_manger) #4  !!!
        self.addWidget(self.orderDetails_manger) #5  !!!
        self.addWidget(self.orderRequirment_manger) #6
        self.addWidget(self.clients_manger) #7
        self.addWidget(self.addClient_manger) #8 done
        self.addWidget(self.inbox_manger) #9
        self.addWidget(self.addRequirement_manger) # 10
        self.addWidget(self.userRegister_manger) #11
        self.addWidget(self.editOrder_manger) #12

        # install signals
        self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)

        '''
        main view signals
        '''
        self.main_manger.workOrder_btn.clicked.connect(self.handle_workOrder)
        self.main_manger.followOrders_btn.clicked.connect(self.handle_followOrder)
        self.main_manger.finishedOrders_btn.clicked.connect(self.handle_finishedOrders)
        self.main_manger.ordersReq_btn.clicked.connect(self.handle_orderRequirment)
        self.main_manger.clients_btn.clicked.connect(self.handle_Clients)
        self.main_manger.addUser_btn.clicked.connect(self.handle_user_registration)
        self.main_manger.logOut_btn.clicked.connect(self.handle_logOut)
        self.main_manger.inbox_btn.clicked.connect(self.handle_inboxManger)

        '''
        new order view signals
        '''

        self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.newOrder_manger.checkAcceptedSignal.connect(self.handle_clearOrder)
        self.newOrder_manger.end_btn.clicked.connect(self.handle_clearOrder)

        '''
        follow Orders screen 
        '''
        #self.followOrder_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        self.followOrder_manger.checkAcceptedSignal.connect(self.handle_DetailsFollowOrder)
        self.followOrder_manger.new_btn.clicked.connect(self.handle_workOrder)
        self.followOrder_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        '''
        followed order detail screen 
        '''
        self.orderDetails_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        '''
        finished orders screen
        '''
        self.finishedOrders_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        '''
        order Requirement screen
        '''
        self.orderRequirment_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.orderRequirment_manger.new_btn.clicked.connect(self.handle_addRequirement)

        '''
        clients
        '''
        self.clients_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.clients_manger.new_btn.clicked.connect(self.handle_addClient)

        '''
        Add client
        '''
        self.addClient_manger.end_btn.clicked.connect(lambda: self.setCurrentIndex(7))
        self.addClient_manger.checkDataSignal.connect(self.handle_Clients)

        '''
        inbox 
        '''

        self.inbox_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.inbox_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        self.inbox_manger.alert_signal.connect(self.play_sound)
        self.inbox_manger.checkAcceptedSignal.connect(lambda : self.setCurrentIndex(9))


        '''
        Add Requirement
        '''
        self.addRequirement_manger.end_btn.clicked.connect(lambda: self.setCurrentIndex(6))
        self.addRequirement_manger.checkDataSignal.connect(self.handle_orderRequirment)

        ''' add user '''
        self.userRegister_manger.end_btn.clicked.connect(lambda : self.setCurrentIndex(1))

        # try :
        #     dir_path = os.getcwd()
        #     path_image = os.path.join(dir_path+ r"/views_mangers/3433814.jpg").replace("\\", "/")
        #     #border-image: url(:/login/images/backgroung/3433814.jpg) 0 0 0 0 stretch stretch;
        #     print(path_image)
        #     #qss = f"border-image: url({path_image}) 0 0 0 0 stretch stretch;"
        #     qss = f"background: url({path_image}) 0 0 0 0 stretch stretch;"
        #     self.setStyleSheet(qss)
        #
        #     #self.setStyleSheet(" border-image: url(E:/@projects/tree Advertising/treeAdvertising/views_mangers/3433814.jpg) 0 0 0 0 stretch stretch; ")
        # except Exception as f :
        #     print(f)


        try :
            self.thred = RepeatTimer(1, self.start_time)
            self.thred.start()
        except Exception as w :
            print(w)
        try :
            tracker = MouseTracker(self)
            tracker.positionChanged.connect(self.on_positionChanged)
        except Exception as e :
            print(e)

        self.begin_timer = 0
        self.session_counter = 0
        self.sound_path = os.path.join(os.getcwd()+'/media/audio.wav')


    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        self.session_counter = time.time()
        #print("(%d, %d)" % (pos.x(), pos.y()))
    def start_time(self):
        if self.inbox_manger.admin_check == False :
            self.inbox_manger.check_inbox()

        end_time = time.time()
        lapced_time = end_time - self.begin_timer
        mins = lapced_time // 60
        sec = round(lapced_time % 60)
        hours = mins // 60
        mins = mins % 60
        session_time = str("{0}:{1}:{2}".format(int(hours), int(mins), sec))
        self.main_manger.sessionTime_lbl.setText(session_time)
        end_time_session = time.time()
        actuall_session_time = end_time_session - self.session_counter
        session_mins = actuall_session_time // 60
        session_mins = session_mins % 60
        if session_mins == 10 and self.currentIndex() != 0:
            self.handle_logOut()

    def play_sound(self):
        self.main_manger.notification_mark_lbl.setVisible(True)

        try :
            playsound(self.sound_path)
        except Exception as r :
            print(r)

    def handle_clearOrder(self):
        self.newOrder_manger.clear_data()
        self.setCurrentIndex(1)

    def handle_login_accepted(self):
        self.main_manger.username_lbl.setText(self.login_manger.username_lin.text())
        self.inbox_manger.token = self.login_manger.userToken
        self.begin_timer = time.time()
        self.session_counter = time.time()
        self.setCurrentIndex(1)
    def handle_workOrder(self):
        self.newOrder_manger.token = self.login_manger.userToken
        self.setCurrentIndex(2)
    def handle_orderRequirment(self):
        self.orderRequirment_manger.token = self.login_manger.userToken
        self.orderRequirment_manger.userName = self.login_manger.username_lin.text()
        self.orderRequirment_manger.run()
        self.setCurrentIndex(6)
    def handle_followOrder(self):
        self.followOrder_manger.token = self.login_manger.userToken
        self.followOrder_manger.run()
        self.setCurrentIndex(3)
    def handle_Clients(self):
        self.clients_manger.token = self.login_manger.userToken
        self.clients_manger.run()
        self.setCurrentIndex(7)
    def handle_addClient(self):
        self.addClient_manger.token = self.login_manger.userToken
        self.setCurrentIndex(8)
    def handle_addRequirement(self):
        self.addRequirement_manger.token = self.login_manger.userToken
        self.setCurrentIndex(10)
    def handle_finishedOrders(self):
        self.finishedOrders_manger.token = self.login_manger.userToken
        self.finishedOrders_manger.run()
        self.setCurrentIndex(4)
    def handle_DetailsFollowOrder(self):
        self.orderDetails_manger.order_id = self.followOrder_manger.orderID
        self.orderDetails_manger.token = self.login_manger.userToken
        self.orderDetails_manger.run()
        self.setCurrentIndex(5)

    def handle_DetailsOrder(self):
        self.orderDetails_manger.order_id = self.inbox_manger.orderID
        self.orderDetails_manger.token = self.login_manger.userToken
        self.orderDetails_manger.run()
        self.setCurrentIndex(5)

    def handle_inboxManger(self):
        self.inbox_manger.token = self.login_manger.userToken
        self.inbox_manger.user_name = self.login_manger.username_lin.text()
        self.inbox_manger.run()
        #self.setCurrentIndex(9)
        self.main_manger.notification_mark_lbl.setVisible(False)

    def handle_user_registration(self):
        self.userRegister_manger.token = self.login_manger.userToken
        self.userRegister_manger.clear()
        self.setCurrentIndex(11)

    def exit_program(self):
        self.thred.cancel()
        #print("program closed")
        sys.exit()
    def handle_logOut(self):
        #self.thred.cancel()
        self.login_manger.password_lin.setText("")
        self.setCurrentIndex(0)

    def closeEvent(self, event):
        try:
            self.exit_program()
            event.accept()
        except Exception as e:
            print(e)
            event.ignore()

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Tree_Advertising()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()