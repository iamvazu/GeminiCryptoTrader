# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 420)
        MainWindow.setMinimumSize(QtCore.QSize(747, 420))
        MainWindow.setMaximumSize(QtCore.QSize(747, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.dashboardTab = QtWidgets.QWidget()
        self.dashboardTab.setObjectName("dashboardTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dashboardTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currencyTabWidget = QtWidgets.QTabWidget(self.dashboardTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currencyTabWidget.sizePolicy().hasHeightForWidth())
        self.currencyTabWidget.setSizePolicy(sizePolicy)
        self.currencyTabWidget.setObjectName("currencyTabWidget")
        self.btcTab = QtWidgets.QWidget()
        self.btcTab.setObjectName("btcTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.btcTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btcLayout = QtWidgets.QVBoxLayout()
        self.btcLayout.setObjectName("btcLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.btcTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.btcLastPriceLabel = QtWidgets.QLabel(self.btcTab)
        self.btcLastPriceLabel.setText("")
        self.btcLastPriceLabel.setObjectName("btcLastPriceLabel")
        self.gridLayout_3.addWidget(self.btcLastPriceLabel, 0, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.btcTab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.btcDeltaLabel = QtWidgets.QLabel(self.btcTab)
        self.btcDeltaLabel.setText("")
        self.btcDeltaLabel.setObjectName("btcDeltaLabel")
        self.gridLayout_3.addWidget(self.btcDeltaLabel, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.btcTab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.btcRangeLabel = QtWidgets.QLabel(self.btcTab)
        self.btcRangeLabel.setText("")
        self.btcRangeLabel.setObjectName("btcRangeLabel")
        self.gridLayout_3.addWidget(self.btcRangeLabel, 2, 1, 1, 2)
        self.btcLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.btcLayout, 0, 0, 1, 1)
        self.currencyTabWidget.addTab(self.btcTab, "")
        self.ethTab = QtWidgets.QWidget()
        self.ethTab.setObjectName("ethTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ethTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ethLayout = QtWidgets.QVBoxLayout()
        self.ethLayout.setObjectName("ethLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ethLastPriceLabel = QtWidgets.QLabel(self.ethTab)
        self.ethLastPriceLabel.setText("")
        self.ethLastPriceLabel.setObjectName("ethLastPriceLabel")
        self.gridLayout_5.addWidget(self.ethLastPriceLabel, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.ethTab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.ethTab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.ethDeltaLabel = QtWidgets.QLabel(self.ethTab)
        self.ethDeltaLabel.setText("")
        self.ethDeltaLabel.setObjectName("ethDeltaLabel")
        self.gridLayout_5.addWidget(self.ethDeltaLabel, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.ethTab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)
        self.ethRangeLabel = QtWidgets.QLabel(self.ethTab)
        self.ethRangeLabel.setText("")
        self.ethRangeLabel.setObjectName("ethRangeLabel")
        self.gridLayout_5.addWidget(self.ethRangeLabel, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 2, 1, 1)
        self.ethLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.ethLayout, 0, 0, 1, 1)
        self.currencyTabWidget.addTab(self.ethTab, "")
        self.horizontalLayout_2.addWidget(self.currencyTabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.balanceGroupBox = QtWidgets.QGroupBox(self.dashboardTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.balanceGroupBox.sizePolicy().hasHeightForWidth())
        self.balanceGroupBox.setSizePolicy(sizePolicy)
        self.balanceGroupBox.setObjectName("balanceGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.balanceGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.balanceGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usdBalanceLabel = QtWidgets.QLabel(self.balanceGroupBox)
        self.usdBalanceLabel.setText("")
        self.usdBalanceLabel.setObjectName("usdBalanceLabel")
        self.gridLayout.addWidget(self.usdBalanceLabel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.balanceGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btcBalanceLabel = QtWidgets.QLabel(self.balanceGroupBox)
        self.btcBalanceLabel.setText("")
        self.btcBalanceLabel.setObjectName("btcBalanceLabel")
        self.gridLayout.addWidget(self.btcBalanceLabel, 1, 1, 1, 1)
        self.ethBalanceLabel = QtWidgets.QLabel(self.balanceGroupBox)
        self.ethBalanceLabel.setText("")
        self.ethBalanceLabel.setObjectName("ethBalanceLabel")
        self.gridLayout.addWidget(self.ethBalanceLabel, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.balanceGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.balanceGroupBox)
        self.availableGroupBox = QtWidgets.QGroupBox(self.dashboardTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableGroupBox.sizePolicy().hasHeightForWidth())
        self.availableGroupBox.setSizePolicy(sizePolicy)
        self.availableGroupBox.setObjectName("availableGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.availableGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.usdAvailableLabel = QtWidgets.QLabel(self.availableGroupBox)
        self.usdAvailableLabel.setText("")
        self.usdAvailableLabel.setObjectName("usdAvailableLabel")
        self.gridLayout_2.addWidget(self.usdAvailableLabel, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.availableGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.btcAvailableLabel = QtWidgets.QLabel(self.availableGroupBox)
        self.btcAvailableLabel.setText("")
        self.btcAvailableLabel.setObjectName("btcAvailableLabel")
        self.gridLayout_2.addWidget(self.btcAvailableLabel, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.availableGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.availableGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.ethAvailableLabel = QtWidgets.QLabel(self.availableGroupBox)
        self.ethAvailableLabel.setText("")
        self.ethAvailableLabel.setObjectName("ethAvailableLabel")
        self.gridLayout_2.addWidget(self.ethAvailableLabel, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.availableGroupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.disconnectButton = QtWidgets.QPushButton(self.dashboardTab)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout.addWidget(self.disconnectButton)
        self.connectButton = QtWidgets.QPushButton(self.dashboardTab)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.mainTabWidget.addTab(self.dashboardTab, "")
        self.transactionsTab = QtWidgets.QWidget()
        self.transactionsTab.setObjectName("transactionsTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.transactionsTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.transactionsTable = QtWidgets.QTableWidget(self.transactionsTab)
        self.transactionsTable.setObjectName("transactionsTable")
        self.transactionsTable.setColumnCount(0)
        self.transactionsTable.setRowCount(0)
        self.gridLayout_8.addWidget(self.transactionsTable, 0, 0, 1, 1)
        self.mainTabWidget.addTab(self.transactionsTab, "")
        self.openOrdersTab = QtWidgets.QWidget()
        self.openOrdersTab.setObjectName("openOrdersTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.openOrdersTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.openOrdersTable = QtWidgets.QTableWidget(self.openOrdersTab)
        self.openOrdersTable.setObjectName("openOrdersTable")
        self.openOrdersTable.setColumnCount(0)
        self.openOrdersTable.setRowCount(0)
        self.gridLayout_9.addWidget(self.openOrdersTable, 0, 0, 1, 1)
        self.mainTabWidget.addTab(self.openOrdersTab, "")
        self.conditionalTab = QtWidgets.QWidget()
        self.conditionalTab.setObjectName("conditionalTab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.conditionalTab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.conditionalTable = QtWidgets.QTableWidget(self.conditionalTab)
        self.conditionalTable.setObjectName("conditionalTable")
        self.conditionalTable.setColumnCount(0)
        self.conditionalTable.setRowCount(0)
        self.gridLayout_10.addWidget(self.conditionalTable, 0, 0, 1, 1)
        self.mainTabWidget.addTab(self.conditionalTab, "")
        self.gridLayout_7.addWidget(self.mainTabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 747, 22))
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.editMenu = QtWidgets.QMenu(self.menuBar)
        self.editMenu.setObjectName("editMenu")
        self.viewMenu = QtWidgets.QMenu(self.menuBar)
        self.viewMenu.setObjectName("viewMenu")
        self.helpMenu = QtWidgets.QMenu(self.menuBar)
        self.helpMenu.setObjectName("helpMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_Edit = QtWidgets.QAction(MainWindow)
        self.action_Edit.setObjectName("action_Edit")
        self.setupAction = QtWidgets.QAction(MainWindow)
        self.setupAction.setObjectName("setupAction")
        self.buyAction = QtWidgets.QAction(MainWindow)
        self.buyAction.setObjectName("buyAction")
        self.sellAction = QtWidgets.QAction(MainWindow)
        self.sellAction.setObjectName("sellAction")
        self.conditionalAction = QtWidgets.QAction(MainWindow)
        self.conditionalAction.setObjectName("conditionalAction")
        self.genDepositAction = QtWidgets.QAction(MainWindow)
        self.genDepositAction.setObjectName("genDepositAction")
        self.withdrawToAction = QtWidgets.QAction(MainWindow)
        self.withdrawToAction.setObjectName("withdrawToAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.optionsAction = QtWidgets.QAction(MainWindow)
        self.optionsAction.setObjectName("optionsAction")
        self.notificationsAction = QtWidgets.QAction(MainWindow)
        self.notificationsAction.setObjectName("notificationsAction")
        self.toggleStatusBarAction = QtWidgets.QAction(MainWindow)
        self.toggleStatusBarAction.setObjectName("toggleStatusBarAction")
        self.showOrderBookAction = QtWidgets.QAction(MainWindow)
        self.showOrderBookAction.setObjectName("showOrderBookAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.action_Visit_Gemini_API_Docs = QtWidgets.QAction(MainWindow)
        self.action_Visit_Gemini_API_Docs.setObjectName("action_Visit_Gemini_API_Docs")
        self.action_Gemini_Exchange = QtWidgets.QAction(MainWindow)
        self.action_Gemini_Exchange.setObjectName("action_Gemini_Exchange")
        self.fileMenu.addAction(self.setupAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.buyAction)
        self.fileMenu.addAction(self.sellAction)
        self.fileMenu.addAction(self.conditionalAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.genDepositAction)
        self.fileMenu.addAction(self.withdrawToAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.optionsAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.notificationsAction)
        self.viewMenu.addAction(self.toggleStatusBarAction)
        self.viewMenu.addAction(self.showOrderBookAction)
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.action_Visit_Gemini_API_Docs)
        self.helpMenu.addAction(self.action_Gemini_Exchange)
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.editMenu.menuAction())
        self.menuBar.addAction(self.viewMenu.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.mainTabWidget.setCurrentIndex(0)
        self.currencyTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gemini Crypto Trader"))
        self.label_7.setText(_translate("MainWindow", "Last Price:"))
        self.label_8.setText(_translate("MainWindow", "24-Hour Δ:"))
        self.label_9.setText(_translate("MainWindow", "24-Hour Range:"))
        self.currencyTabWidget.setTabText(self.currencyTabWidget.indexOf(self.btcTab), _translate("MainWindow", "BTC"))
        self.label_11.setText(_translate("MainWindow", "Last Price:"))
        self.label_10.setText(_translate("MainWindow", "24-Hour Δ:"))
        self.label_12.setText(_translate("MainWindow", "24-Hour Range:"))
        self.currencyTabWidget.setTabText(self.currencyTabWidget.indexOf(self.ethTab), _translate("MainWindow", "ETH"))
        self.balanceGroupBox.setTitle(_translate("MainWindow", "Balances:"))
        self.label.setText(_translate("MainWindow", "USD:"))
        self.label_3.setText(_translate("MainWindow", "ETH:"))
        self.label_2.setText(_translate("MainWindow", "BTC:"))
        self.availableGroupBox.setTitle(_translate("MainWindow", "Available for Trading:"))
        self.label_5.setText(_translate("MainWindow", "BTC:"))
        self.label_4.setText(_translate("MainWindow", "USD:"))
        self.label_6.setText(_translate("MainWindow", "ETH:"))
        self.disconnectButton.setText(_translate("MainWindow", "&Disconnect"))
        self.connectButton.setText(_translate("MainWindow", "&Connect"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.dashboardTab), _translate("MainWindow", "Dashboard"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.transactionsTab), _translate("MainWindow", "Transactions"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.openOrdersTab), _translate("MainWindow", "Open Orders"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.conditionalTab), _translate("MainWindow", "Conditional"))
        self.fileMenu.setTitle(_translate("MainWindow", "&File"))
        self.editMenu.setTitle(_translate("MainWindow", "&Edit"))
        self.viewMenu.setTitle(_translate("MainWindow", "&View"))
        self.helpMenu.setTitle(_translate("MainWindow", "&Help"))
        self.action_Edit.setText(_translate("MainWindow", "&Edit"))
        self.setupAction.setText(_translate("MainWindow", "Se&tup"))
        self.buyAction.setText(_translate("MainWindow", "&Buy"))
        self.sellAction.setText(_translate("MainWindow", "&Sell"))
        self.conditionalAction.setText(_translate("MainWindow", "&Conditional"))
        self.genDepositAction.setText(_translate("MainWindow", "&Generate Deposit Address"))
        self.withdrawToAction.setText(_translate("MainWindow", "&Withdraw To..."))
        self.exitAction.setText(_translate("MainWindow", "&Exit"))
        self.optionsAction.setText(_translate("MainWindow", "&Options"))
        self.notificationsAction.setText(_translate("MainWindow", "&Notifications"))
        self.toggleStatusBarAction.setText(_translate("MainWindow", "&Hide Statusbar"))
        self.showOrderBookAction.setText(_translate("MainWindow", "&Show Orderbook"))
        self.aboutAction.setText(_translate("MainWindow", "&About"))
        self.action_Visit_Gemini_API_Docs.setText(_translate("MainWindow", "&Visit Gemini API Docs"))
        self.action_Gemini_Exchange.setText(_translate("MainWindow", "Visit &Gemini Exchange"))

