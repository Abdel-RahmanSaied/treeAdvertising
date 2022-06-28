# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/orderRequirment_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1033)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(160, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(97, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.new_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_btn.sizePolicy().hasHeightForWidth())
        self.new_btn.setSizePolicy(sizePolicy)
        self.new_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.new_btn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.new_btn.setFont(font)
        self.new_btn.setStyleSheet("\n"
" transition-duration: 0.4s;\n"
" color: white;\n"
" background-color :rgb(50, 85, 127);\n"
" border: 2px solid #rgb(50, 85, 127)\n"
"\n"
" box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);")
        self.new_btn.setObjectName("new_btn")
        self.gridLayout.addWidget(self.new_btn, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(97, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.delete_btn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("\n"
" transition-duration: 0.4s;\n"
" color: white;\n"
" background-color :rgb(50, 85, 127);\n"
" border: 2px solid #rgb(50, 85, 127)\n"
"\n"
" box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);")
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.frame)
        self.search_btn.setMinimumSize(QtCore.QSize(91, 41))
        self.search_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127, 250);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_2.addWidget(self.search_btn, 0, 2, 1, 1)
        self.search_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(401, 35))
        self.search_lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;\n"
"font: 14pt \"Acumin Pro\";")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.gridLayout_2.addWidget(self.search_lineEdit, 0, 3, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
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
        self.tableWidget.setColumnCount(4)
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
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 1, 1, 1, 3)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 6)
        spacerItem4 = QtWidgets.QSpacerItem(753, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setFamily("Thunder Lord")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(643, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(759, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 4, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(669, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setMinimumSize(QtCore.QSize(200, 60))
        self.bck_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bck_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127, 250);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.bck_btn.setObjectName("bck_btn")
        self.horizontalLayout.addWidget(self.bck_btn)
        spacerItem8 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.details_btn = QtWidgets.QPushButton(Form)
        self.details_btn.setMinimumSize(QtCore.QSize(200, 60))
        self.details_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.details_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127, 250);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.details_btn.setObjectName("details_btn")
        self.horizontalLayout.addWidget(self.details_btn)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 1, 1, 3)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.new_btn.setText(_translate("Form", "جديد"))
        self.delete_btn.setText(_translate("Form", "مسح"))
        self.search_btn.setText(_translate("Form", "بحث"))
        self.search_lineEdit.setPlaceholderText(_translate("Form", "    بحث . . ."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "الرقم"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "اسم الطلب"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "الكمية"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "اسم الطالب"))
        self.label.setText(_translate("Form", "متطلبات اوامر الشغل"))
        self.bck_btn.setText(_translate("Form", "الرجوع"))
        self.details_btn.setText(_translate("Form", "انتهي"))
import app_resources_rc
