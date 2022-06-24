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
from views_mangers.orderRequirment_view_manger import OrderRequirment
from views_mangers.add_requirement_manger import AddRequirement

from views_mangers.inbox_manger import Inbox_manger

class Tree_Advertising(QtWidgets.QStackedWidget):
    def __init__(self):
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

        # install signals
        self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)
        # self.login_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.login_manger.exit_btn.clicked.connect(self.exit_program)
        '''
        main view signals
        '''
        self.main_manger.workOrder_btn.clicked.connect(self.handle_workOrder)
        self.main_manger.followOrders_btn.clicked.connect(self.handle_followOrder)
        self.main_manger.finishedOrders_btn.clicked.connect(self.handle_finishedOrders)
        self.main_manger.ordersReq_btn.clicked.connect(self.handle_orderRequirment)
        self.main_manger.clients_btn.clicked.connect(self.handle_Clients)
        self.main_manger.logOut_btn.clicked.connect(lambda : self.setCurrentIndex(0))
        self.main_manger.inbox_btn.clicked.connect(self.handle_inboxManger)

        self.main_manger.logout_signal.connect(self.handle_logOut)

        # self.main_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.main_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        new order view signals
        '''

        self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.newOrder_manger.checkAcceptedSignal.connect(self.handle_clearOrder)
        self.newOrder_manger.end_btn.clicked.connect(self.handle_clearOrder)

        # self.newOrder_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.newOrder_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        follow Orders screen 
        '''
        #self.followOrder_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        self.followOrder_manger.checkAcceptedSignal.connect(self.handle_DetailsFollowOrder)
        self.followOrder_manger.new_btn.clicked.connect(self.handle_workOrder)
        self.followOrder_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        # self.followOrder_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.followOrder_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        followed order detail screen 
        '''
        self.orderDetails_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        # self.orderDetails_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.orderDetails_manger.exit_btn.clicked.connect(self.exit_program)
        '''
        finished orders screen
        '''
        self.finishedOrders_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        # self.finishedOrders_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.finishedOrders_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        order Requirement screen
        '''
        self.orderRequirment_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.orderRequirment_manger.new_btn.clicked.connect(self.handle_addRequirement)
        # self.orderRequirment_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        # self.orderRequirment_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        clients
        '''
        self.clients_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.clients_manger.new_btn.clicked.connect(self.handle_addClient)
        # self.clients_manger.minimize_btn.clicked.connect(lambda: self.showMinimized())
        # self.clients_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        Add client
        '''
        self.addClient_manger.end_btn.clicked.connect(lambda: self.setCurrentIndex(7))
        self.addClient_manger.checkDataSignal.connect(self.handle_Clients)
        # self.addClient_manger.add_btn.clicked.connect(lambda: self.setCurrentIndex(8))
        # self.addClient_manger.minimize_btn.clicked.connect(lambda: self.showMinimized())
        # self.addClient_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        inbox 
        '''
        # self.inbox_manger.exit_btn.clicked.connect(self.exit_program)
        # self.inbox_manger.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.inbox_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.inbox_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        '''
        Add Requirement
        '''
        self.addRequirement_manger.end_btn.clicked.connect(lambda: self.setCurrentIndex(6))
        self.addRequirement_manger.checkDataSignal.connect(self.handle_orderRequirment)
        # self.addClient_manger.add_btn.clicked.connect(lambda: self.setCurrentIndex(8))
        # self.addRequirement_manger.minimize_btn.clicked.connect(lambda: self.showMinimized())
        # self.addRequirement_manger.exit_btn.clicked.connect(self.exit_program)


        ''' designs  '''

    def handle_clearOrder(self):
        self.newOrder_manger.clear_data()
        self.setCurrentIndex(1)

    def handle_login_accepted(self):
        self.main_manger.username_lbl.setText(self.login_manger.username_lin.text())
        self.main_manger.start_stopwatch()
        self.setCurrentIndex(1)
    def handle_workOrder(self):
        self.newOrder_manger.token = self.login_manger.userToken
        self.setCurrentIndex(2)
    def handle_orderRequirment(self):
        self.orderRequirment_manger.token = self.login_manger.userToken
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
        self.setCurrentIndex(9)

    def exit_program(self):
        self.main_manger.thred.cancel()
        print("program closed")
        sys.exit()
    def handle_logOut(self):
        self.main_manger.thred.cancel()
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
