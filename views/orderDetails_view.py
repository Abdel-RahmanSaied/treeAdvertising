# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/orderDetails_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1049)
        Form.setMinimumSize(QtCore.QSize(1340, 810))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(920, 30, 218, 33))
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(9, 84, 1891, 841))
        self.frame.setMinimumSize(QtCore.QSize(391, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.orderID_lbl = QtWidgets.QLabel(self.frame)
        self.orderID_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.orderID_lbl.setFont(font)
        self.orderID_lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
" border-radius: 12px;\n"
"padding-bottom:7px;")
        self.orderID_lbl.setText("")
        self.orderID_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.orderID_lbl.setObjectName("orderID_lbl")
        self.horizontalLayout.addWidget(self.orderID_lbl)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(63, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clientName_lbl = QtWidgets.QLabel(self.frame)
        self.clientName_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clientName_lbl.setFont(font)
        self.clientName_lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
" border-radius: 12px;\n"
"padding-bottom:7px;")
        self.clientName_lbl.setText("")
        self.clientName_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.clientName_lbl.setObjectName("clientName_lbl")
        self.horizontalLayout_2.addWidget(self.clientName_lbl)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(63, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_lbl = QtWidgets.QLabel(self.frame)
        self.date_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.date_lbl.setFont(font)
        self.date_lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
" border-radius: 12px;\n"
"padding-bottom:7px;")
        self.date_lbl.setText("")
        self.date_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_lbl.setObjectName("date_lbl")
        self.horizontalLayout_3.addWidget(self.date_lbl)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(63, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateCreated_lbl = QtWidgets.QLabel(self.frame)
        self.dateCreated_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dateCreated_lbl.setFont(font)
        self.dateCreated_lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
" border-radius: 12px;\n"
"padding-bottom:7px;")
        self.dateCreated_lbl.setText("")
        self.dateCreated_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dateCreated_lbl.setObjectName("dateCreated_lbl")
        self.horizontalLayout_4.addWidget(self.dateCreated_lbl)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(63, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sevices_afterPrinting_lbl = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sevices_afterPrinting_lbl.setFont(font)
        self.sevices_afterPrinting_lbl.setStyleSheet("\n"
" border-radius: 12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.sevices_afterPrinting_lbl.setText("")
        self.sevices_afterPrinting_lbl.setWordWrap(False)
        self.sevices_afterPrinting_lbl.setObjectName("sevices_afterPrinting_lbl")
        self.gridLayout_3.addWidget(self.sevices_afterPrinting_lbl, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.print_type_lbl = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.print_type_lbl.setFont(font)
        self.print_type_lbl.setStyleSheet("\n"
" border-radius: 12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.print_type_lbl.setText("")
        self.print_type_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.print_type_lbl.setWordWrap(True)
        self.print_type_lbl.setObjectName("print_type_lbl")
        self.gridLayout_4.addWidget(self.print_type_lbl, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 3, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.notes_lbl = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.notes_lbl.setFont(font)
        self.notes_lbl.setStyleSheet("\n"
" border-radius: 12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.notes_lbl.setText("")
        self.notes_lbl.setWordWrap(True)
        self.notes_lbl.setObjectName("notes_lbl")
        self.gridLayout_5.addWidget(self.notes_lbl, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 3, 0, 1, 4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.recived_date_lbl = QtWidgets.QLabel(self.frame)
        self.recived_date_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.recived_date_lbl.setFont(font)
        self.recived_date_lbl.setStyleSheet("\n"
" border-radius: 12px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.recived_date_lbl.setText("")
        self.recived_date_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.recived_date_lbl.setObjectName("recived_date_lbl")
        self.horizontalLayout_5.addWidget(self.recived_date_lbl)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setMinimumSize(QtCore.QSize(63, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_12.setMinimumSize(QtCore.QSize(1361, 821))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/login/images/backgroung/3433814.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setGeometry(QtCore.QRect(920, 950, 183, 60))
        self.bck_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.bck_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bck_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.bck_btn.setObjectName("bck_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1860, 40, 30, 30))
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
        self.minimize_btn.setGeometry(QtCore.QRect(1810, 40, 30, 30))
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
        self.label_12.raise_()
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
        self.label.setText(_translate("Form", "متابعة امر الشغل"))
        self.label_4.setText(_translate("Form", "رقم امر الشغل"))
        self.label_5.setText(_translate("Form", "اسم العميل "))
        self.label_6.setText(_translate("Form", "التاريخ"))
        self.label_7.setText(_translate("Form", "نوع العمليه"))
        self.groupBox_2.setTitle(_translate("Form", "خدمات ما بعد الطباعة"))
        self.groupBox.setTitle(_translate("Form", "نوع الطباعه"))
        self.groupBox_3.setTitle(_translate("Form", "ملاحظات"))
        self.label_9.setText(_translate("Form", "تاريخ التسليم "))
        self.bck_btn.setText(_translate("Form", "الرجوع"))
import app_resources_rc
