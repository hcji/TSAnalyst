# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 1021)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelFileList = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelFileList.setFont(font)
        self.labelFileList.setObjectName("labelFileList")
        self.verticalLayout.addWidget(self.labelFileList)
        self.ListFile = QtWidgets.QListWidget(self.layoutWidget)
        self.ListFile.setObjectName("ListFile")
        self.verticalLayout.addWidget(self.ListFile)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonGroup1 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonGroup1.setObjectName("ButtonGroup1")
        self.horizontalLayout.addWidget(self.ButtonGroup1)
        self.ButtonGroup2 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonGroup2.setObjectName("ButtonGroup2")
        self.horizontalLayout.addWidget(self.ButtonGroup2)
        self.ButtonClearFileList = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonClearFileList.setObjectName("ButtonClearFileList")
        self.horizontalLayout.addWidget(self.ButtonClearFileList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelDatabase = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelDatabase.setFont(font)
        self.labelDatabase.setObjectName("labelDatabase")
        self.verticalLayout.addWidget(self.labelDatabase)
        self.ListDatabase = QtWidgets.QListWidget(self.layoutWidget)
        self.ListDatabase.setObjectName("ListDatabase")
        self.verticalLayout.addWidget(self.ListDatabase)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ButtonDatabaseConfirm = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonDatabaseConfirm.setObjectName("ButtonDatabaseConfirm")
        self.horizontalLayout_2.addWidget(self.ButtonDatabaseConfirm)
        self.ButtonDatabaseRemove = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonDatabaseRemove.setObjectName("ButtonDatabaseRemove")
        self.horizontalLayout_2.addWidget(self.ButtonDatabaseRemove)
        self.ButtonClearDatabase = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonClearDatabase.setObjectName("ButtonClearDatabase")
        self.horizontalLayout_2.addWidget(self.ButtonClearDatabase)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelProteinComplex = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelProteinComplex.setFont(font)
        self.labelProteinComplex.setObjectName("labelProteinComplex")
        self.verticalLayout.addWidget(self.labelProteinComplex)
        self.tableProteinComplex = QtWidgets.QTableView(self.layoutWidget)
        self.tableProteinComplex.setObjectName("tableProteinComplex")
        self.verticalLayout.addWidget(self.tableProteinComplex)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ButtonCalcComplex = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonCalcComplex.setObjectName("ButtonCalcComplex")
        self.horizontalLayout_3.addWidget(self.ButtonCalcComplex)
        self.ButtonShowCurve = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonShowCurve.setObjectName("ButtonShowCurve")
        self.horizontalLayout_3.addWidget(self.ButtonShowCurve)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelProteinTable1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelProteinTable1.setFont(font)
        self.labelProteinTable1.setObjectName("labelProteinTable1")
        self.verticalLayout_2.addWidget(self.labelProteinTable1)
        self.tableProtein1 = QtWidgets.QTableView(self.widget)
        self.tableProtein1.setMinimumSize(QtCore.QSize(0, 200))
        self.tableProtein1.setObjectName("tableProtein1")
        self.verticalLayout_2.addWidget(self.tableProtein1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelProteinTable2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelProteinTable2.setFont(font)
        self.labelProteinTable2.setObjectName("labelProteinTable2")
        self.verticalLayout_3.addWidget(self.labelProteinTable2)
        self.tableProtein2 = QtWidgets.QTableView(self.widget)
        self.tableProtein2.setMinimumSize(QtCore.QSize(0, 200))
        self.tableProtein2.setObjectName("tableProtein2")
        self.verticalLayout_3.addWidget(self.tableProtein2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionProteomics = QtWidgets.QAction(MainWindow)
        self.actionProteomics.setObjectName("actionProteomics")
        self.actionDatabase = QtWidgets.QAction(MainWindow)
        self.actionDatabase.setObjectName("actionDatabase")
        self.action_CETSA = QtWidgets.QAction(MainWindow)
        self.action_CETSA.setObjectName("action_CETSA")
        self.actionCalcPval = QtWidgets.QAction(MainWindow)
        self.actionCalcPval.setObjectName("actionCalcPval")
        self.actionCalcROC = QtWidgets.QAction(MainWindow)
        self.actionCalcROC.setObjectName("actionCalcROC")
        self.actionCheck_update = QtWidgets.QAction(MainWindow)
        self.actionCheck_update.setObjectName("actionCheck_update")
        self.actionCitation = QtWidgets.QAction(MainWindow)
        self.actionCitation.setObjectName("actionCitation")
        self.actionCheck_liences = QtWidgets.QAction(MainWindow)
        self.actionCheck_liences.setObjectName("actionCheck_liences")
        self.actionPreprocessing = QtWidgets.QAction(MainWindow)
        self.actionPreprocessing.setObjectName("actionPreprocessing")
        self.actionCalcComplex = QtWidgets.QAction(MainWindow)
        self.actionCalcComplex.setObjectName("actionCalcComplex")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuDatabase.addAction(self.actionPreprocessing)
        self.menuDatabase.addAction(self.actionProteomics)
        self.menuDatabase.addAction(self.actionDatabase)
        self.menuHelp.addAction(self.actionCheck_update)
        self.menuHelp.addAction(self.actionCitation)
        self.menuHelp.addAction(self.actionCheck_liences)
        self.menuAnalysis.addAction(self.action_CETSA)
        self.menuAnalysis.addAction(self.actionCalcROC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFileList.setText(_translate("MainWindow", "File List"))
        self.ButtonGroup1.setText(_translate("MainWindow", "Set as G1"))
        self.ButtonGroup2.setText(_translate("MainWindow", "Set as G2"))
        self.ButtonClearFileList.setText(_translate("MainWindow", "Clear"))
        self.labelDatabase.setText(_translate("MainWindow", "Database List"))
        self.ButtonDatabaseConfirm.setText(_translate("MainWindow", "Confirm"))
        self.ButtonDatabaseRemove.setText(_translate("MainWindow", "Remove"))
        self.ButtonClearDatabase.setText(_translate("MainWindow", "Clear"))
        self.labelProteinComplex.setText(_translate("MainWindow", "Protein Complex"))
        self.ButtonCalcComplex.setText(_translate("MainWindow", "Calc Change"))
        self.ButtonShowCurve.setText(_translate("MainWindow", "Show Curve"))
        self.labelProteinTable1.setText(_translate("MainWindow", "Group1 Protein Table"))
        self.labelProteinTable2.setText(_translate("MainWindow", "Group2 Protein Table"))
        self.groupBox.setTitle(_translate("MainWindow", "Group1 Thermal Shift Curve"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Group2 Thermal Shift Curve"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Data"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionProteomics.setText(_translate("MainWindow", "Load proteomics..."))
        self.actionDatabase.setText(_translate("MainWindow", "Load PPI database..."))
        self.action_CETSA.setText(_translate("MainWindow", "Single protein analysis ..."))
        self.actionCalcPval.setText(_translate("MainWindow", "Calculate p-values of protein complex ..."))
        self.actionCalcROC.setText(_translate("MainWindow", "Protein pair analysis..."))
        self.actionCheck_update.setText(_translate("MainWindow", "Check update ..."))
        self.actionCitation.setText(_translate("MainWindow", "Check citation ..."))
        self.actionCheck_liences.setText(_translate("MainWindow", "Check licence"))
        self.actionPreprocessing.setText(_translate("MainWindow", "Preprocessing..."))
        self.actionCalcComplex.setText(_translate("MainWindow", "Protein complex analysis..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
