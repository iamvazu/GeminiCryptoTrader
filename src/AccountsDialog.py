################################################################################
#                                                                              #
#  AccountsDialog.py                                                           #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, base64
from ui_AccountsDialog import Ui_AccountsDialog
from ManageDialog import ManageDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget, QRadioButton

class AccountsDialog(QtWidgets.QDialog, Ui_AccountsDialog):
    # Class data
    accounts = []       # List of saved accounts
    account = {}        # Currently selected/last loaded account
    settings = {}       # Program settings

    # Initializer
    def __init__(self, parent, accounts, settings):
        super(AccountsDialog, self).__init__(parent)
        self.initUI()
        self.accounts = accounts
        self.settings = settings
        self.setLastUsedAccount()
        self.centerOnScreen()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.doneButton.clicked.connect(self.accept)
        self.addButton.clicked.connect(self.addAccount)
        self.updateButton.clicked.connect(self.updateAccount)
        self.manageButton.clicked.connect(self.openManageDialog)
        self.traderCB.toggled.connect(self.traderCBToggled)

        # Set trader role as default
        self.traderCB.setChecked(True)

    # Return account list
    ############################################################################
    @pyqtSlot()
    def getAccounts(self):
        return self.accounts

    # Adds a new account
    ############################################################################
    def addAccount(self):
        data = self.inputToJson()

        if self.isValidInput(data, False):
            self.accounts.append(data)

    # Update saved account information
    ############################################################################
    @pyqtSlot()
    def updateAccount(self):
        data = self.inputToJson()

        # Search through account data to edit if input is valid
        if self.isValidInput(data, True):
            for i in self.accounts:
                if i['accountId'] == data['accountId']:
                    i['isTrader'] == data['isTrader']
                    i['hasHeartbeat'] == data['hasHeartbeat']
                    i['isFundManager'] == data['isFundManager']
                    i['apiKey'] = data['apiKey']
                    i['secretKey'] = data['secretKey']
                    i['isSandbox'] = data['isSandbox']

    # Open the manage accounts dialog
    ############################################################################
    @pyqtSlot()
    def openManageDialog(self):
        md = ManageDialog(self, self.accounts)
        if md.exec_():
            self.accounts = md.getAccounts()
            self.setLastUsedAccount()

    # Translate input data into a JSON object
    ############################################################################
    def inputToJson(self):
        # Get data from input
        data = {
            'lastUsed':         True,
            'isTrader':         self.traderCB.isChecked(),
            'hasHeartbeat':     self.heartbeatCB.isChecked(),
            'isFundManager':    self.fundManagerCB.isChecked(),
            'accountId':        self.accountIdLE.text(),
            'apiKey':           self.apiKeyLE.text(),
            'secretKey':        self.secretKeyLE.text(),
            'isSandbox':        self.sandboxCB.isChecked()
        }

        return data

    # Validate input; forUpdate is a flag for updating already saved account
    ############################################################################
    def isValidInput(self, data, forUpdate):
        # Make sure at least one role is enabled
        if not self.traderCB.isChecked() and not self.fundManagerCB.isChecked():
            msg = QMessageBox()
            msg.setText('At least one role must be set.')
            msg.exec()
            return False

        # Check for duplicates
        if not forUpdate:
            for i in self.accounts:
                if i['accountId'] == data['accountId']:
                    msg = QMessageBox()
                    msg.setText('This Account ID already exists.')
                    msg.exec()
                    return False
                if i['apiKey'] == data['apiKey']:
                    msg = QMessageBox()
                    msg.setText('This API key already exists.')
                    msg.exec()
                    return False
                if i['secretKey'] == data['secretKey']:
                    msg = QMessageBox()
                    msg.setText('This secret key already exists.')
                    msg.exec()
                    return False

        # Ensure account ID and API key are provided
        #if (data['accountId'] == '' or data['apiKey'] == ''):
        #    msg = QMessageBox()
        #    msg.setText('Account ID and API Key are required.')
        #    msg.exec()
        #    return False

        # Ensure last used account is unique
        for i in self.accounts:
            if i['lastUsed'] == True and i['accountId'] != data['accountId']:
                i['lastUsed'] = False

        # Return input is valid
        return True

    # Loads account information from file
    ############################################################################
    def setLastUsedAccount(self):
        if not self.accounts:
            self.accountIdLE.setText('')
            self.apiKeyLE.setText('')
            self.secretKeyLE.setText('')
            self.sandboxCB.setChecked(False)
            self.account = self.inputToJson()
            self.accounts.append(self.account)
        else:
            for i in self.accounts:
                if i['lastUsed'] == True:
                    self.accountIdLE.setText(i['accountId'])
                    self.traderCB.setChecked(i['isTrader'])
                    self.heartbeatCB.setChecked(i['hasHeartbeat'])
                    self.fundManagerCB.setChecked(i['isFundManager'])
                    self.apiKeyLE.setText(i['apiKey'])
                    self.secretKeyLE.setText(i['secretKey'])
                    self.sandboxCB.setChecked(i['isSandbox'])
                    self.account = i
                    break

    # Trader check box toggled, enable heartbeat option
    ############################################################################
    @pyqtSlot()
    def traderCBToggled(self):
        if self.traderCB.isChecked():
            self.heartbeatCB.setEnabled(True)
        else:
            self.heartbeatCB.setChecked(False)
            self.heartbeatCB.setEnabled(False)

    # Centers dialog on the screen
    ############################################################################
    def centerOnScreen(self):
        desktopSize = QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (self.height() / 2)
        left = (desktopSize.width() / 2) - (self.width() / 2)
        self.move(left, top)

    # Close event
    ############################################################################
    def closeEvent(self, event):
        return