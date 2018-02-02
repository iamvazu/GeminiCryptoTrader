################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
import icons
import urllib
from urllib.request import urlopen
from urllib.error import URLError
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from SetupDialog import SetupDialog
from BuyDialog import BuyDialog
from SellDialog import SellDialog
from ConditionalDialog import ConditionalDialog
from GenDepositAddrDialog import GenDepositAddrDialog
from WithdrawToDialog import WithdrawToDialog
from AboutDialog import AboutDialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...', msecs=3000)

        # Check internet connection
        if self.internetAvailable(self):
            self.connectIconPM = QPixmap(':/orange-circle.png')
        else:
            self.connectIconPM = QPixmap(':/red-circle.png')
        self.connectIconLabel = QLabel(self)
        self.connectIconLabel.setPixmap(self.connectIconPM)
        self.statusBar.setToolTip('Green when connected to exchange')
        self.statusBar.addPermanentWidget(self.connectIconLabel)

        # Connect actions
        self.setupAction.triggered.connect(self.openSetupDialog)
        self.buyAction.triggered.connect(self.openBuyDialog)
        self.sellAction.triggered.connect(self.openSellDialog)
        self.conditionalAction.triggered.connect(self.openConditionalDialog)
        self.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        self.withdrawToAction.triggered.connect(self.openWithdrawToDialog)
        self.exitAction.triggered.connect(self.close)
        self.toggleStatusBarAction.triggered.connect(self.toggleStatusBar)
        self.aboutAction.triggered.connect(self.openAboutDialog)

    # Opens setup dialog
    ############################################################################
    @pyqtSlot()
    def openSetupDialog(self):
        sd = SetupDialog(self)
        sd.show()

    # Opens buy dialog
    ############################################################################
    @pyqtSlot()
    def openBuyDialog(self):
        bd = BuyDialog(self)
        bd.show()

    # Opens sell dialog
    ############################################################################
    @pyqtSlot()
    def openSellDialog(self):
        sd = SellDialog(self)
        sd.show()

    # Opens conditional dialog
    ############################################################################
    @pyqtSlot()
    def openConditionalDialog(self):
        cd = ConditionalDialog(self)
        cd.show()

    # Opens dialog to generate new deposit address
    ############################################################################
    @pyqtSlot()
    def openGenDepositAddrDialog(self):
        gd = GenDepositAddrDialog(self)
        gd.show()

    # Opens withdraw dialog
    ############################################################################
    @pyqtSlot()
    def openWithdrawToDialog(self):
        wd = WithdrawToDialog(self)
        wd.show()

    # Opens about dialog
    ############################################################################
    @pyqtSlot()
    def openAboutDialog(self):
        ad = AboutDialog(self)
        ad.show()

    # Toggles status bar on or off
    ############################################################################
    @pyqtSlot()
    def toggleStatusBar(self):
        if self.statusBar.isVisible():
            self.statusBar.hide()
            self.toggleStatusBarAction.setText('Show Statusbar')
        else:
            self.statusBar.show()
            self.toggleStatusBarAction.setText('Hide Statusbar')

    # Checks internet connection
    ############################################################################
    @staticmethod
    def internetAvailable(arg):
        try:
            urlopen('http://74.125.21.99', timeout=1)
            return True
        except URLError as err:
            return False
