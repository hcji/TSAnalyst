# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalTSA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1413, 929)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelFileList = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelFileList.setFont(font)
        self.labelFileList.setObjectName("labelFileList")
        self.verticalLayout.addWidget(self.labelFileList)
        self.ListFile = QtWidgets.QListWidget(self.layoutWidget)
        self.ListFile.setMinimumSize(QtCore.QSize(450, 0))
        self.ListFile.setObjectName("ListFile")
        self.verticalLayout.addWidget(self.ListFile)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ButtonR1P1 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonR1P1.setObjectName("ButtonR1P1")
        self.horizontalLayout_4.addWidget(self.ButtonR1P1)
        self.ButtonR1P2 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonR1P2.setObjectName("ButtonR1P2")
        self.horizontalLayout_4.addWidget(self.ButtonR1P2)
        self.ButtonRemove = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonRemove.setObjectName("ButtonRemove")
        self.horizontalLayout_4.addWidget(self.ButtonRemove)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonR2P1 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonR2P1.setObjectName("ButtonR2P1")
        self.horizontalLayout.addWidget(self.ButtonR2P1)
        self.ButtonR2P2 = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonR2P2.setObjectName("ButtonR2P2")
        self.horizontalLayout.addWidget(self.ButtonR2P2)
        self.ButtonClearFileList = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonClearFileList.setObjectName("ButtonClearFileList")
        self.horizontalLayout.addWidget(self.ButtonClearFileList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelDatabase = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelDatabase.setFont(font)
        self.labelDatabase.setObjectName("labelDatabase")
        self.verticalLayout_4.addWidget(self.labelDatabase)
        self.tableWidgetProteinList = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidgetProteinList.setMinimumSize(QtCore.QSize(0, 500))
        self.tableWidgetProteinList.setObjectName("tableWidgetProteinList")
        self.tableWidgetProteinList.setColumnCount(0)
        self.tableWidgetProteinList.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidgetProteinList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ButtonParam = QtWidgets.QPushButton(self.layoutWidget1)
        self.ButtonParam.setObjectName("ButtonParam")
        self.horizontalLayout_2.addWidget(self.ButtonParam)
        self.ButtonShow = QtWidgets.QPushButton(self.layoutWidget1)
        self.ButtonShow.setObjectName("ButtonShow")
        self.horizontalLayout_2.addWidget(self.ButtonShow)
        self.ButtonSave = QtWidgets.QPushButton(self.layoutWidget1)
        self.ButtonSave.setObjectName("ButtonSave")
        self.horizontalLayout_2.addWidget(self.ButtonSave)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelProteinTable1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelProteinTable1.setFont(font)
        self.labelProteinTable1.setObjectName("labelProteinTable1")
        self.verticalLayout_2.addWidget(self.labelProteinTable1)
        self.tabWidget_1 = QtWidgets.QTabWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_1.setFont(font)
        self.tabWidget_1.setObjectName("tabWidget_1")
        self.R1P1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.R1P1.setFont(font)
        self.R1P1.setObjectName("R1P1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.R1P1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableRep1Protein1 = QtWidgets.QTableView(self.R1P1)
        self.tableRep1Protein1.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.tableRep1Protein1.setFont(font)
        self.tableRep1Protein1.setObjectName("tableRep1Protein1")
        self.gridLayout_2.addWidget(self.tableRep1Protein1, 0, 0, 1, 1)
        self.tabWidget_1.addTab(self.R1P1, "")
        self.R1P2 = QtWidgets.QWidget()
        self.R1P2.setObjectName("R1P2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.R1P2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableRep1Protein2 = QtWidgets.QTableView(self.R1P2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableRep1Protein2.setFont(font)
        self.tableRep1Protein2.setObjectName("tableRep1Protein2")
        self.gridLayout_3.addWidget(self.tableRep1Protein2, 0, 0, 1, 1)
        self.tabWidget_1.addTab(self.R1P2, "")
        self.verticalLayout_2.addWidget(self.tabWidget_1)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelProteinTable1_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelProteinTable1_2.setFont(font)
        self.labelProteinTable1_2.setObjectName("labelProteinTable1_2")
        self.verticalLayout_3.addWidget(self.labelProteinTable1_2)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.R2P1 = QtWidgets.QWidget()
        self.R2P1.setObjectName("R2P1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.R2P1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableRep2Protein1 = QtWidgets.QTableView(self.R2P1)
        self.tableRep2Protein1.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.tableRep2Protein1.setFont(font)
        self.tableRep2Protein1.setObjectName("tableRep2Protein1")
        self.gridLayout_4.addWidget(self.tableRep2Protein1, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.R2P1, "")
        self.R2P2 = QtWidgets.QWidget()
        self.R2P2.setObjectName("R2P2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.R2P2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableRep2Protein2 = QtWidgets.QTableView(self.R2P2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableRep2Protein2.setFont(font)
        self.tableRep2Protein2.setObjectName("tableRep2Protein2")
        self.gridLayout_5.addWidget(self.tableRep2Protein2, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.R2P2, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.groupBox1 = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBox1.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox1.setFont(font)
        self.groupBox1.setObjectName("groupBox1")
        self.groupBox2 = QtWidgets.QGroupBox(self.splitter_3)
        self.groupBox2.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox2.setFont(font)
        self.groupBox2.setObjectName("groupBox2")
        self.verticalLayout_5.addWidget(self.splitter_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1413, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
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
        self.actionCETSA = QtWidgets.QAction(MainWindow)
        self.actionCETSA.setObjectName("actionCETSA")
        self.actionCalcPval = QtWidgets.QAction(MainWindow)
        self.actionCalcPval.setObjectName("actionCalcPval")
        self.actionTPP = QtWidgets.QAction(MainWindow)
        self.actionTPP.setObjectName("actionTPP")
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
        self.actioniTSA = QtWidgets.QAction(MainWindow)
        self.actioniTSA.setObjectName("actioniTSA")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.actionAnalDist = QtWidgets.QAction(MainWindow)
        self.actionAnalDist.setObjectName("actionAnalDist")
        self.actionExternal = QtWidgets.QAction(MainWindow)
        self.actionExternal.setObjectName("actionExternal")
        self.actionInflect = QtWidgets.QAction(MainWindow)
        self.actionInflect.setObjectName("actionInflect")
        self.actionNPARC = QtWidgets.QAction(MainWindow)
        self.actionNPARC.setObjectName("actionNPARC")
        self.actionINFLECT = QtWidgets.QAction(MainWindow)
        self.actionINFLECT.setObjectName("actionINFLECT")
        self.actionDistance = QtWidgets.QAction(MainWindow)
        self.actionDistance.setObjectName("actionDistance")
        self.menuDatabase.addAction(self.actionProteomics)
        self.menuAnalysis.addAction(self.actionTPP)
        self.menuAnalysis.addAction(self.actionNPARC)
        self.menuAnalysis.addAction(self.actionDistance)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_1.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFileList.setText(_translate("MainWindow", "File List"))
        self.ButtonR1P1.setText(_translate("MainWindow", "Rep 1 Ctrl"))
        self.ButtonR1P2.setText(_translate("MainWindow", "Rep 1 Case"))
        self.ButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.ButtonR2P1.setText(_translate("MainWindow", "Rep 2 Ctrl"))
        self.ButtonR2P2.setText(_translate("MainWindow", "Rep 2 Case"))
        self.ButtonClearFileList.setText(_translate("MainWindow", "Clear"))
        self.labelDatabase.setText(_translate("MainWindow", "Result Table"))
        self.ButtonParam.setText(_translate("MainWindow", "Params"))
        self.ButtonShow.setText(_translate("MainWindow", "Show Curve"))
        self.ButtonSave.setText(_translate("MainWindow", "Save Result"))
        self.labelProteinTable1.setText(_translate("MainWindow", "Replicate #1 Protein Table"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.R1P1), _translate("MainWindow", "Group1"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.R1P2), _translate("MainWindow", "Group2"))
        self.labelProteinTable1_2.setText(_translate("MainWindow", "Replicate #2 Protein Table"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.R2P1), _translate("MainWindow", "Group1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.R2P2), _translate("MainWindow", "Group2"))
        self.groupBox1.setTitle(_translate("MainWindow", "Thermal Shift Curve"))
        self.groupBox2.setTitle(_translate("MainWindow", "Rank of targets"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Data"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionProteomics.setText(_translate("MainWindow", "Load proteomics..."))
        self.actionDatabase.setText(_translate("MainWindow", "Load PPI database..."))
        self.actionCETSA.setText(_translate("MainWindow", "Thermal shift analysis ..."))
        self.actionCalcPval.setText(_translate("MainWindow", "Calculate p-values of protein complex ..."))
        self.actionTPP.setText(_translate("MainWindow", "Run TPP Method"))
        self.actionCheck_update.setText(_translate("MainWindow", "Check update ..."))
        self.actionCitation.setText(_translate("MainWindow", "Check citation ..."))
        self.actionCheck_liences.setText(_translate("MainWindow", "Check licence..."))
        self.actionPreprocessing.setText(_translate("MainWindow", "Preprocessing..."))
        self.actionCalcComplex.setText(_translate("MainWindow", "Protein complex analysis..."))
        self.actioniTSA.setText(_translate("MainWindow", "Isothermal shift analysis..."))
        self.actionContact.setText(_translate("MainWindow", "Contact author..."))
        self.actionAnalDist.setText(_translate("MainWindow", "Distance-based analysis..."))
        self.actionExternal.setText(_translate("MainWindow", "External tool analysis..."))
        self.actionInflect.setText(_translate("MainWindow", "Inflect analysis..."))
        self.actionNPARC.setText(_translate("MainWindow", "Run NPARC Method"))
        self.actionINFLECT.setText(_translate("MainWindow", "Run Inflect Method"))
        self.actionDistance.setText(_translate("MainWindow", "Run Distance Mehod"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

