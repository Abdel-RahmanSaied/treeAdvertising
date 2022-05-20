from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_manger import Login_Manager
from views_mangers.main_manger import Main_manger
from views_mangers.newOrderView_manger import NewOrderView_manger
# from views_mangers.chooseDesign_manger import ChooseDesign_manger
# from views_mangers.newOrderDataView_manger import NewOrderDataView_manger
from views_mangers.notes_manger import NotesManger

from views_mangers.followOrder_manger import FollowOrder
# from views_mangers.officeDesign_manger import OfficeDesign
from views_mangers.finishedOrders_manger import FinishedOrders
from views_mangers.orderDetails_manger import OrderDetails

class Tree_Advertising(QtWidgets.QStackedWidget):
    def __init__(self):
        super(Tree_Advertising, self).__init__()
        self.login_manger = Login_Manager()
        self.main_manger = Main_manger()
        self.newOrder_manger=NewOrderView_manger()
#         self.chooseDesign_manger = ChooseDesign_manger()
#         self.newOrderData_manger=NewOrderDataView_manger()
        self.notes_manger = NotesManger()

        self.followOrder_manger = FollowOrder()
#         self.officeDesign_manger = OfficeDesign()
        self.finishedOrders_manger = FinishedOrders()

        self.orderDetails_manger = OrderDetails()

        # add widgets to the stack
        self.addWidget(self.login_manger) #0
        self.addWidget(self.main_manger) #1
        self.addWidget(self.newOrder_manger) #2
#         self.addWidget(self.chooseDesign_manger) #3

        self.addWidget(self.followOrder_manger)  #4  !!!
#         self.addWidget(self.officeDesign_manger)  #5 delete
        self.addWidget(self.finishedOrders_manger) #6  !!!
        self.addWidget(self.orderDetails_manger) #7  !!!
        self.addWidget(self.notes_manger) #8


        # install signals
        self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)
        '''
        main view signals
        '''
        self.main_manger.workOrder_btn.clicked.connect(self.handle_workOrder)
        self.main_manger.followOrders_btn.clicked.connect(self.handle_followOrder)
        self.main_manger.finishedOrders_btn.clicked.connect(self.handle_finishedOrders)
        self.main_manger.logOut_btn.clicked.connect(lambda : self.setCurrentIndex(0))

        '''
        new order view signals
        '''
        self.newOrder_manger.next_btn.clicked.connect(self.handle_notes)
        self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))

        '''
        new order data screen signals 
        '''
#         self.newOrderData_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(3))
#         self.newOrderData_manger.next_btn.clicked.connect(self.handle_notes)

        '''
        choose design signals
        '''
#         self.chooseDesign_manger.checkAcceptedSignal.connect(self.handle_chooseDesignClient)
#         self.chooseDesign_manger.officeDesign_btn.clicked.connect(self.handle_officeDesign)
#         self.chooseDesign_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(2))

        '''
        office design screen
        '''
#         self.officeDesign_manger.next_btn.clicked.connect(self.handle_chooseDesignClient)
#         self.officeDesign_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        '''
        follow Orders screen 
        '''
        self.followOrder_manger.details_btn.clicked.connect(self.handle_DetailsOrder)
        self.followOrder_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))

        '''
        followed order detail screen 
        '''
        self.orderDetails_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(5))
        '''
        finished orders screen
        '''
        self.finishedOrders_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        '''
        notes screen
        '''
        self.notes_manger.end_btn.clicked.connect(self.handle_login_accepted)
        self.notes_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(2))


    def handle_login_accepted(self):
        self.setCurrentIndex(1)
    def handle_workOrder(self):
        self.setCurrentIndex(2)
    def handle_newOrder(self):
        self.setCurrentIndex(3)
    def handle_chooseDesignClient(self):
        self.setCurrentIndex(4)
    def handle_followOrder(self):
        self.setCurrentIndex(5)
    def handle_officeDesign(self):
        self.setCurrentIndex(6)
    def handle_finishedOrders(self):
        self.setCurrentIndex(7)
    def handle_DetailsOrder(self):
        self.setCurrentIndex(8)
    def handle_notes(self):
        self.setCurrentIndex(9)

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Tree_Advertising()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
