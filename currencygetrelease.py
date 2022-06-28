import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from parsingcurrencyforuah import parsing_currency
from interfacecurrencyget import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_currency)

    def show_currency(self):
        parsing_currency()
        with open('resultparsingcurrency.json', 'r', encoding='utf8') as file:
            list_currency = json.load(file)
        self.ui.label_1.setText(f"USD {list_currency['USD']['average_currency_buy']} / {list_currency['USD']['average_currency_sell']}")
        self.ui.label_2.setText(f"EUR {list_currency['EUR']['average_currency_buy']} / {list_currency['EUR']['average_currency_sell']}")
        self.ui.label_3.setText(f"PLN {list_currency['PLN']['average_currency_buy']} / {list_currency['PLN']['average_currency_sell']}")
        self.ui.label_4.setText(f"GBP {list_currency['GBP']['average_currency_buy']} / {list_currency['GBP']['average_currency_sell']}")
        self.ui.label_5.setText(f"CHF {list_currency['CHF']['average_currency_buy']} / {list_currency['CHF']['average_currency_sell']}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('logo.png'))
    myapp = MyWin()
    myapp.setWindowIcon(QtGui.QIcon('logo.png'))
    myapp.show()
    sys.exit(app.exec_())

