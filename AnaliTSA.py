# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaliTSA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1045, 772)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Form.setFont(font)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBoxMethod = QtWidgets.QComboBox(Form)
        self.comboBoxMethod.setObjectName("comboBoxMethod")
        self.horizontalLayout.addWidget(self.comboBoxMethod)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBoxLog2 = QtWidgets.QComboBox(Form)
        self.comboBoxLog2.setObjectName("comboBoxLog2")
        self.horizontalLayout_2.addWidget(self.comboBoxLog2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.doubleSpinBoxFCthres = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBoxFCthres.setProperty("value", 1.1)
        self.doubleSpinBoxFCthres.setObjectName("doubleSpinBoxFCthres")
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxFCthres)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.doubleSpinBoxPthres = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBoxPthres.setSingleStep(0.01)
        self.doubleSpinBoxPthres.setProperty("value", 0.05)
        self.doubleSpinBoxPthres.setObjectName("doubleSpinBoxPthres")
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxPthres)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonData = QtWidgets.QPushButton(Form)
        self.pushButtonData.setObjectName("pushButtonData")
        self.horizontalLayout_5.addWidget(self.pushButtonData)
        self.pushButtonOK = QtWidgets.QPushButton(Form)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout_5.addWidget(self.pushButtonOK)
        self.pushButtonClose = QtWidgets.QPushButton(Form)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout_5.addWidget(self.pushButtonClose)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.tableWidgetLabel = QtWidgets.QTableWidget(Form)
        self.tableWidgetLabel.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidgetLabel.setObjectName("tableWidgetLabel")
        self.tableWidgetLabel.setColumnCount(0)
        self.tableWidgetLabel.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidgetLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButtonSave = QtWidgets.QPushButton(Form)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_6.addWidget(self.pushButtonSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.tableViewData = QtWidgets.QTableView(Form)
        self.tableViewData.setMinimumSize(QtCore.QSize(0, 250))
        self.tableViewData.setObjectName("tableViewData")
        self.verticalLayout.addWidget(self.tableViewData)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.vocano = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vocano.setFont(font)
        self.vocano.setObjectName("vocano")
        self.gridLayout = QtWidgets.QGridLayout(self.vocano)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxVolcano = QtWidgets.QGroupBox(self.vocano)
        self.groupBoxVolcano.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.groupBoxVolcano.setFont(font)
        self.groupBoxVolcano.setTitle("")
        self.groupBoxVolcano.setObjectName("groupBoxVolcano")
        self.gridLayout.addWidget(self.groupBoxVolcano, 0, 0, 1, 1)
        self.tabWidget.addTab(self.vocano, "")
        self.heatmap = QtWidgets.QWidget()
        self.heatmap.setObjectName("heatmap")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.heatmap)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxHeatmap = QtWidgets.QGroupBox(self.heatmap)
        self.groupBoxHeatmap.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.groupBoxHeatmap.setFont(font)
        self.groupBoxHeatmap.setTitle("")
        self.groupBoxHeatmap.setObjectName("groupBoxHeatmap")
        self.gridLayout_2.addWidget(self.groupBoxHeatmap, 0, 0, 1, 1)
        self.tabWidget.addTab(self.heatmap, "")
        self.barchart = QtWidgets.QWidget()
        self.barchart.setObjectName("barchart")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.barchart)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBoxBarchart = QtWidgets.QGroupBox(self.barchart)
        self.groupBoxBarchart.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.groupBoxBarchart.setFont(font)
        self.groupBoxBarchart.setTitle("")
        self.groupBoxBarchart.setObjectName("groupBoxBarchart")
        self.gridLayout_3.addWidget(self.groupBoxBarchart, 0, 0, 1, 1)
        self.tabWidget.addTab(self.barchart, "")
        self.pcaplot = QtWidgets.QWidget()
        self.pcaplot.setObjectName("pcaplot")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pcaplot)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBoxPCA = QtWidgets.QGroupBox(self.pcaplot)
        self.groupBoxPCA.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.groupBoxPCA.setFont(font)
        self.groupBoxPCA.setTitle("")
        self.groupBoxPCA.setObjectName("groupBoxPCA")
        self.gridLayout_4.addWidget(self.groupBoxPCA, 0, 0, 1, 1)
        self.tabWidget.addTab(self.pcaplot, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.tabWidget.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "Parameters for iTSA analysis:"))
        self.label_2.setText(_translate("Form", "Select methods"))
        self.label_3.setText(_translate("Form", "Log2 Transformed"))
        self.label_9.setText(_translate("Form", "Fold change threshold"))
        self.label_10.setText(_translate("Form", "P-value threshold"))
        self.pushButtonData.setText(_translate("Form", "Data"))
        self.pushButtonOK.setText(_translate("Form", "Confirm"))
        self.pushButtonClose.setText(_translate("Form", "Cancel"))
        self.label_8.setText(_translate("Form", "Label setting"))
        self.pushButtonSave.setText(_translate("Form", "Save"))
        self.label_11.setText(_translate("Form", "Data viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vocano), _translate("Form", "Volcano"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.heatmap), _translate("Form", "Heatmap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.barchart), _translate("Form", "Barchart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pcaplot), _translate("Form", "PCA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

