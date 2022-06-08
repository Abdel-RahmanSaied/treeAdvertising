from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_manger import Login_Manager
from views_mangers.main_manger import Main_manger
from views_mangers.newOrderView_manger import NewOrderView_manger
import sys
from views_mangers.notes_manger import NotesManger

from views_mangers.followOrder_manger import FollowOrder
from views_mangers.finishedOrders_manger import FinishedOrders
from views_mangers.orderDetails_manger import OrderDetails
from views_mangers.orderRequirment_view_manger import OrderRequirment

class Tree_Advertising(QtWidgets.QStackedWidget):
    def __init__(self):
        super(Tree_Advertising, self).__init__()
        self.login_manger = Login_Manager()
        self.main_manger = Main_manger()
        self.newOrder_manger=NewOrderView_manger()
        self.notes_manger = NotesManger()
        self.followOrder_manger = FollowOrder()
        self.finishedOrders_manger = FinishedOrders()
        self.orderDetails_manger = OrderDetails()
        self.orderRequirment_manger = OrderRequirment()

        self.showFullScreen()

        # add widgets to the stack
        self.addWidget(self.login_manger) #0
        self.addWidget(self.main_manger) #1
        self.addWidget(self.newOrder_manger) #2

        self.addWidget(self.followOrder_manger)  #3  !!!

        self.addWidget(self.finishedOrders_manger) #4  !!!
        self.addWidget(self.orderDetails_manger) #5  !!!
        self.addWidget(self.notes_manger) #6
        self.addWidget(self.orderRequirment_manger) #7


        # install signals
        self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)
        self.login_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.login_manger.exit_btn.clicked.connect(self.exit_program)
        '''
        main view signals
        '''
        self.main_manger.workOrder_btn.clicked.connect(self.handle_workOrder)
        self.main_manger.followOrders_btn.clicked.connect(self.handle_followOrder)
        self.main_manger.finishedOrders_btn.clicked.connect(self.handle_finishedOrders)
        self.main_manger.ordersReq_btn.clicked.connect(self.handle_orderRequirment)
        self.main_manger.logOut_btn.clicked.connect(lambda : self.setCurrentIndex(0))

        self.main_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())

        self.main_manger.logout_signal.connect(self.handle_logOut)
        self.main_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        new order view signals
        '''
        self.newOrder_manger.next_btn.clicked.connect(self.handle_notes)
        self.newOrder_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.newOrder_manger.exit_btn.clicked.connect(self.exit_program)
        self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))


        '''
        follow Orders screen 
        '''
        self.followOrder_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        self.followOrder_manger.checkAcceptedSignal.connect(self.handle_DetailsOrder)
        self.followOrder_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.followOrder_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.followOrder_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        followed order detail screen 
        '''
        self.orderDetails_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(5))
        self.orderDetails_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.orderDetails_manger.exit_btn.clicked.connect(self.exit_program)
        '''
        finished orders screen
        '''
        self.finishedOrders_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.finishedOrders_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.finishedOrders_manger.exit_btn.clicked.connect(self.exit_program)

        '''
        order Requirement screen
        '''
        self.orderRequirment_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.orderRequirment_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.orderRequirment_manger.exit_btn.clicked.connect(self.exit_program)
        '''
        notes screen
        '''
        self.notes_manger.end_btn.clicked.connect(self.handle_login_accepted)
        self.notes_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(2))
        self.notes_manger.minimize_btn.clicked.connect(lambda : self.showMinimized())
        self.notes_manger.exit_btn.clicked.connect(self.exit_program)

        ''' designs  '''


    def handle_login_accepted(self):
        self.main_manger.username_lbl.setText(self.login_manger.username_lin.text())
        self.main_manger.start_stopwatch()
        self.setCurrentIndex(1)
    def handle_workOrder(self):
        self.setCurrentIndex(2)

    def handle_orderRequirment(self):
        self.orderRequirment_manger.token = self.login_manger.userToken
        self.orderRequirment_manger.run()
        self.setCurrentIndex(7)
    def handle_followOrder(self):
        self.followOrder_manger.token = self.login_manger.userToken
        self.followOrder_manger.run()
        self.setCurrentIndex(3)
#     def handle_officeDesign(self):
#         self.setCurrentIndex(6)
    def handle_finishedOrders(self):
        self.setCurrentIndex(4)
    def handle_DetailsOrder(self):
        self.orderDetails_manger.order_id = self.followOrder_manger.orderID
        self.orderDetails_manger.token = self.login_manger.userToken
        self.orderDetails_manger.run()
        self.setCurrentIndex(5)
    def handle_notes(self):
        self.setCurrentIndex(7)

    def exit_program(self):
        self.main_manger.thred.cancel()
        sys.exit()
    def handle_logOut(self):
        self.main_manger.thred.cancel()
        self.login_manger.password_lin.setText("")
        self.setCurrentIndex(0)

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Tree_Advertising()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
