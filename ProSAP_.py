# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProSAP_.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(948, 638)
        Form.setMinimumSize(QtCore.QSize(948, 638))
        Form.setMaximumSize(QtCore.QSize(948, 638))
        self.pushButtonPreprocess = QtWidgets.QPushButton(Form)
        self.pushButtonPreprocess.setGeometry(QtCore.QRect(130, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButtonPreprocess.setFont(font)
        self.pushButtonPreprocess.setObjectName("pushButtonPreprocess")
        self.pushButtonTPP = QtWidgets.QPushButton(Form)
        self.pushButtonTPP.setGeometry(QtCore.QRect(130, 360, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButtonTPP.setFont(font)
        self.pushButtonTPP.setObjectName("pushButtonTPP")
        self.pushButtonITSA = QtWidgets.QPushButton(Form)
        self.pushButtonITSA.setGeometry(QtCore.QRect(460, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButtonITSA.setFont(font)
        self.pushButtonITSA.setObjectName("pushButtonITSA")
        self.pushButtonTPCA = QtWidgets.QPushButton(Form)
        self.pushButtonTPCA.setGeometry(QtCore.QRect(460, 360, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.pushButtonTPCA.setFont(font)
        self.pushButtonTPCA.setObjectName("pushButtonTPCA")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(600, 540, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(600, 570, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 50, 525, 58))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonPreprocess.setText(_translate("Form", "Preprocess"))
        self.pushButtonTPP.setText(_translate("Form", "TPP Analysis"))
        self.pushButtonITSA.setText(_translate("Form", "PISA/iTSA Analysis"))
        self.pushButtonTPCA.setText(_translate("Form", "TPCA Analysis"))
        self.label_2.setText(_translate("Form", "Author: Ji Hongchao, Lu Xue, Chris Tan"))
        self.label_3.setText(_translate("Form", "E-mail: ji.hongchao@foxmail.com"))
        self.label.setText(_translate("Form", "ProSAP"))
        self.label_4.setText(_translate("Form", "-- Protein Stability Analysis Pod"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
