# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desing.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 158)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.btnGeneratNum = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.btnGeneratNum.setFont(font)
        self.btnGeneratNum.setObjectName("btnGeneratNum")
        self.gridLayout.addWidget(self.btnGeneratNum, 1, 2, 1, 1)
        self.inputValidNum = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.inputValidNum.setFont(font)
        self.inputValidNum.setObjectName("inputValidNum")
        self.gridLayout.addWidget(self.inputValidNum, 0, 1, 1, 1)
        self.btnValidNum = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnValidNum.sizePolicy().hasHeightForWidth())
        self.btnValidNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.btnValidNum.setFont(font)
        self.btnValidNum.setObjectName("btnValidNum")
        self.gridLayout.addWidget(self.btnValidNum, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.labelReturn = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.labelReturn.setFont(font)
        self.labelReturn.setStyleSheet("color: green;")
        self.labelReturn.setText("")
        self.labelReturn.setReadOnly(True)
        self.labelReturn.setObjectName("labelReturn")
        self.gridLayout.addWidget(self.labelReturn, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Valid or Generate number"))
        self.label.setText(_translate("MainWindow", "Generate Number:"))
        self.btnGeneratNum.setText(_translate("MainWindow", "Generate"))
        self.btnValidNum.setText(_translate("MainWindow", "Valid"))
        self.label_2.setText(_translate("MainWindow", "Valid Number:"))