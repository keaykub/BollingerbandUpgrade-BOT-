from iqoptionapi.stable_api import IQ_Option
from talib import *
import time
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 460)
        self.email_w = QtWidgets.QLineEdit(Dialog)
        self.email_w.setGeometry(QtCore.QRect(20, 21, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_w.setFont(font)
        self.email_w.setAutoFillBackground(False)
        self.email_w.setObjectName("email_w")
        self.pass_w = QtWidgets.QLineEdit(Dialog)
        self.pass_w.setGeometry(QtCore.QRect(250, 20, 171, 31))
        self.pass_w.setAutoFillBackground(False)
        self.pass_w.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_w.setObjectName("pass_w")
        self.login_w = QtWidgets.QPushButton(Dialog)
        self.login_w.setGeometry(QtCore.QRect(430, 20, 91, 31))
        self.login_w.clicked.connect(self.login_iq)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.login_w.setFont(font)
        self.login_w.setStyleSheet("background-color: rgb(170, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.login_w.setObjectName("login_w")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 69, 501, 51))
        self.groupBox.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.status_w = QtWidgets.QLabel(self.groupBox)
        self.status_w.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.status_w.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.status_w.setObjectName("status_w")
        self.balance_w = QtWidgets.QLabel(self.groupBox)
        self.balance_w.setGeometry(QtCore.QRect(260, 10, 81, 31))
        self.balance_w.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.balance_w.setObjectName("balance_w")
        self.status_online_w = QtWidgets.QLabel(self.groupBox)
        self.status_online_w.setGeometry(QtCore.QRect(90, 10, 141, 31))
        self.status_online_w.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);")
        self.status_online_w.setObjectName("status_online_w")
        self.status_balance = QtWidgets.QLabel(self.groupBox)
        self.status_balance.setGeometry(QtCore.QRect(350, 10, 131, 31))
        self.status_balance.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);")
        self.status_balance.setObjectName("status_balance")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 501, 171))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.currency_w = QtWidgets.QLineEdit(self.groupBox_2)
        self.currency_w.setGeometry(QtCore.QRect(110, 10, 111, 31))
        self.currency_w.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.currency_w.setObjectName("currency_w")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(230, 10, 81, 31))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.amount_w = QtWidgets.QLineEdit(self.groupBox_2)
        self.amount_w.setGeometry(QtCore.QRect(310, 10, 61, 31))
        self.amount_w.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amount_w.setObjectName("amount_w")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(380, 10, 51, 31))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.time_w = QtWidgets.QLineEdit(self.groupBox_2)
        self.time_w.setGeometry(QtCore.QRect(430, 10, 61, 31))
        self.time_w.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_w.setObjectName("time_w")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(190, 70, 151, 16))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.start_w = QtWidgets.QPushButton(self.groupBox_2)
        self.start_w.setGeometry(QtCore.QRect(20, 120, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.start_w.setFont(font)
        self.start_w.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.start_w.setObjectName("start_w")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(210, 440, 121, 16))
        self.label_13.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 310, 241, 121))
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.profit_w = QtWidgets.QLabel(self.groupBox_4)
        self.profit_w.setGeometry(QtCore.QRect(90, 50, 71, 31))
        self.profit_w.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.profit_w.setObjectName("profit_w")
        self.winrate_w_2 = QtWidgets.QLabel(self.groupBox_4)
        self.winrate_w_2.setGeometry(QtCore.QRect(90, 0, 71, 31))
        self.winrate_w_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.winrate_w_2.setObjectName("winrate_w_2")
        self.login_w_2 = QtWidgets.QPushButton(Dialog)
        self.login_w_2.setGeometry(QtCore.QRect(350, 350, 91, 31))
        self.login_w_2.clicked.connect(self.out)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.login_w_2.setFont(font)
        self.login_w_2.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.login_w_2.setObjectName("login_w_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bollingerband V1"))
        self.email_w.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">asdasd</span></p></body></html>"))
        self.login_w.setText(_translate("Dialog", "LOGIN"))
        self.status_w.setText(_translate("Dialog", "STATUS"))
        self.balance_w.setText(_translate("Dialog", "BALANCE"))
        self.status_online_w.setText(_translate("Dialog", "OFFLINE"))
        self.status_balance.setText(_translate("Dialog", "OFFLINE"))
        self.label_4.setText(_translate("Dialog", "CURRENCY:"))
        self.label_5.setText(_translate("Dialog", "AMOUNT:"))
        self.label_6.setText(_translate("Dialog", "TIME:"))
        self.label_7.setText(_translate("Dialog", "Bollinger Band V1"))
        self.start_w.setText(_translate("Dialog", "START"))
        self.label_13.setText(_translate("Dialog", "CREDIT: TRADEFORLIFE"))
        self.profit_w.setText(_translate("Dialog", "WAIT!"))
        self.winrate_w_2.setText(_translate("Dialog", "PROFIT"))
        self.login_w_2.setText(_translate("Dialog", "EXIT"))

    def login_iq(self):
        def bollingerband_iq():
            CUR = self.currency_w.text()
            AM = self.amount_w.text()
            TM = self.time_w.text()
            profits = 0.00
            while True:
                QtCore.QCoreApplication.processEvents()
                open1, close1, max1, min1, volume1, times1 = API.edsg_get_over_candles_return_all(1,100,CUR,60)
                upperband, middleband, lowerband = BBANDS(close1, timeperiod=14, nbdevup=2, nbdevdn=2, matype=0)
                upb = upperband[-1]
                lwb = lowerband[-1]
                real = RSI(close1, timeperiod=14)
                rsi_data = real[-1]
                if rsi_data >= 70 and close1[-1] > upb:
                    while True:
                        QtCore.QCoreApplication.processEvents()

                        open1, close1, max1, min1, volume1, times1 = API.edsg_get_over_candles_return_all(1,100,CUR,60)
                        upperband, middleband, lowerband = BBANDS(close1, timeperiod=14, nbdevup=2, nbdevdn=2, matype=0)
                        upb = upperband[-1]
                        if close1[-1] < upb:

                            order_sell, id_sell = API.buy(int(AM),CUR,"put",int(TM))
                            if order_sell == True:
                                while True:
                                    QtCore.QCoreApplication.processEvents()

                                    win_sell = API.check_win_v3(id_sell)
                                    if win_sell > 0:
                                        percent = win_sell
                                        profits = profits + percent
                                        self.profit_w.setNum(profits)
                                        BA = API.get_balance()
                                        self.status_balance.setNum(BA)
                                        break
                                    else:
                                        percent = win_sell
                                        profits = profits + percent
                                        self.profit_w.setNum(profits)
                                        BA = API.get_balance()
                                        self.status_balance.setNum(BA)
                                        break
                            time.sleep(300)
                        break


                elif rsi_data <= 30 and close1[-1] < lwb:
                    while True:
                        QtCore.QCoreApplication.processEvents()

                        open1, close1, max1, min1, volume1, times1 = API.edsg_get_over_candles_return_all(1,100,CUR,60)
                        upperband, middleband, lowerband = BBANDS(close1, timeperiod=14, nbdevup=2, nbdevdn=2, matype=0)
                        lwb = lowerband[-1]
                        if close1[-1] > lwb:

                            order_buy, id_buy = API.buy(int(AM),CUR,"call",int(TM))
                            if order_buy == True:
                                while True:
                                    QtCore.QCoreApplication.processEvents()
                                    win_buy = API.check_win_v3(id_buy)
                                    if win_buy > 0 :
                                        percent = win_buy
                                        profits = profits + percent
                                        self.profit_w.setNum(profits)
                                        BA = API.get_balance()
                                        self.status_balance.setNum(BA)
                                        break
                                    else:
                                        percent = win_buy
                                        profits = profits + percent
                                        self.profit_w.setNum(profits)
                                        BA = API.get_balance()
                                        self.status_balance.setNum(BA)
                                        break
                            time.sleep(300)
                        break


        user = self.email_w.text()
        password = self.pass_w.text()
        API = IQ_Option(user,password)
        iqch1,iqch2 = API.connect()
        if iqch1 == True:
                self.status_online_w.setText("Online")
                BA = API.get_balance()
                self.status_balance.setNum(BA)
        else:
                self.status_online_w.setText("Offline")

        self.start_w.clicked.connect(bollingerband_iq)

    def out(self):
        exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

