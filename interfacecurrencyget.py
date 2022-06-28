# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currencyget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 319)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(310, 319))
        self.centralwidget.setMaximumSize(QtCore.QSize(310, 319))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(35, 275, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 261, 241))
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yanone Kaffeesatz")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid #ffffff;\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exchange rate issuer"))
        self.pushButton.setText(_translate("MainWindow", "Get the exchange rate"))
        self.label_1.setText(_translate("MainWindow", "USD"))
        self.label_2.setText(_translate("MainWindow", "EUR"))
        self.label_3.setText(_translate("MainWindow", "PLN"))
        self.label_4.setText(_translate("MainWindow", "GBP"))
        self.label_5.setText(_translate("MainWindow", "CHF"))