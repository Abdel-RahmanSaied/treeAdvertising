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
        Form.resize(1095, 780)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(826, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(825, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.frame)
        self.next_btn.setMinimumSize(QtCore.QSize(61, 41))
        self.next_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.next_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127, 250);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.next_btn.setObjectName("next_btn")
        self.gridLayout.addWidget(self.next_btn, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 5, 1, 1)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 8, 1, 1)
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
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255,100);\n"
"font: 14pt \"Acumin Pro\";")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(20)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(19, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 10)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 3)
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.bck_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bck_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127, 250);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.bck_btn.setObjectName("bck_btn")
        self.gridLayout_2.addWidget(self.bck_btn, 2, 1, 1, 1)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(12, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(13, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(14, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(15, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(16, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(17, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(18, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(19, QtWidgets.QHeaderView.Stretch)

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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "رقم امر الشغل"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "اسم المشرف "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "اسم القائم علي العمل"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "اسم العميل"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "مسار الصوره"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "التاريخ"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "تاريخ الاستلام"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "تاريخ التسليم"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "نوع التصميم"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "مسار الملف"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "التصميم"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "نوع الطباعه"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "العرض"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "الطول"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "الخامات"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "اللون"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "السُمك"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "خدمات ما بعد الطباعه"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Form", "القسم المختص"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Form", "ملاحظات"))
        self.bck_btn.setText(_translate("Form", "الرجوع"))
import app_resources_rc
