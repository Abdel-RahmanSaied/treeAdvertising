# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/finishedOrders_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1024)
        Form.setMinimumSize(QtCore.QSize(1340, 810))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(840, 20, 261, 33))
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 80, 1861, 811))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.next_btn = QtWidgets.QPushButton(self.frame)
        self.next_btn.setMinimumSize(QtCore.QSize(61, 41))
        self.next_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.next_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 0, 1, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 7, 1, 1)
        self.search_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(301, 0))
        self.search_lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;\n"
"font: 14pt \"Acumin Pro\";")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.gridLayout.addWidget(self.search_lineEdit, 0, 9, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.oreders_scrollArea = QtWidgets.QScrollArea(self.frame)
        self.oreders_scrollArea.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;\n"
"font: 11pt \"Acumin Pro\";")
        self.oreders_scrollArea.setWidgetResizable(True)
        self.oreders_scrollArea.setObjectName("oreders_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1823, 726))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.oreders_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.oreders_scrollArea, 1, 0, 1, 10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setGeometry(QtCore.QRect(870, 930, 183, 60))
        self.bck_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.bck_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bck_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.bck_btn.setObjectName("bck_btn")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_4.setMinimumSize(QtCore.QSize(1361, 821))
        self.label_4.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/login/images/backgroung/3433814.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1850, 20, 30, 30))
        self.exit_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.exit_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(178, 39, 39,100);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn.setObjectName("exit_btn")
        self.minimize_btn = QtWidgets.QPushButton(Form)
        self.minimize_btn.setGeometry(QtCore.QRect(1800, 20, 30, 30))
        self.minimize_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.minimize_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 229, 32,100);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.minimize_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-subtract-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QtCore.QSize(30, 30))
        self.minimize_btn.setObjectName("minimize_btn")
        self.label_4.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.bck_btn.raise_()
        self.exit_btn.raise_()
        self.minimize_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "اوامر الشغل المنتهيه"))
        self.next_btn.setText(_translate("Form", "بحث"))
        self.label_3.setText(_translate("Form", "الي"))
        self.label_2.setText(_translate("Form", "من"))
        self.search_lineEdit.setPlaceholderText(_translate("Form", "    بحث . . ."))
        self.bck_btn.setText(_translate("Form", "الرجوع"))
import app_resources_rc
