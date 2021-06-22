# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:57:14 2021

@author: hcji
"""

import numpy as np
import pandas as pd
from scipy import stats

from PyQt5.QtCore import Qt, QVariant
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from AnalTSA import Ui_MainWindow
from ColumnSelectUI import ColumnSelectUI
from ParamTSAUI import ParamTSAUI
from MakeFigure import MakeFigure

from Thread import TPPThread, DistThread
from MakeFigure import MakeFigure
from Utils import TableModel, fit_curve
from iTSA import estimate_df, p_value_adjust


r1p1Data = pd.read_csv('data/TPCA_TableS14_DMSO.csv')
r1p2Data = pd.read_csv('data/TPCA_TableS14_MTX.csv')
r2p1Data = pd.read_csv('data/TPCA_TableS14_DMSO.csv')
r2p2Data = pd.read_csv('data/TPCA_TableS14_MTX.csv')
columns = ['T37', 'T40', 'T43', 'T46', 'T49', 'T52', 'T55', 'T58', 'T61', 'T64']


class AnalTSAUI(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None): 
        super(AnalTSAUI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("TPP Analysis")
        self.setWindowIcon(QtGui.QIcon("img/TPCA.ico"))
        
        # main window
        self.resize(1500, 900)
        self.setMinimumWidth(1150)
        self.setMinimumHeight(650)
        self.move(75, 50)
        
        # figure box
        self.figureTSA1 = MakeFigure(10, 10, dpi = 250)
        self.figureTSA1_ntb = NavigationToolbar(self.figureTSA1, self)
        self.gridlayoutTSA = QGridLayout(self.groupBox1)
        self.gridlayoutTSA.addWidget(self.figureTSA1)
        self.gridlayoutTSA.addWidget(self.figureTSA1_ntb)
        
        self.figureTSA2 = MakeFigure(10, 10, dpi = 250)
        self.figureTSA2_ntb = NavigationToolbar(self.figureTSA2, self)
        self.gridlayoutTSA2 = QGridLayout(self.groupBox2)
        self.gridlayoutTSA2.addWidget(self.figureTSA2)
        self.gridlayoutTSA2.addWidget(self.figureTSA2_ntb)
        
        # threads
        self.TPPThread = None
        self.AnalDistThread = None
        
        # menu action
        self.actionProteomics.triggered.connect(self.LoadProteinFile)
        self.actionTPP.triggered.connect(self.ShowAnalTPP)
        
        # button action
        self.ButtonR1P1.clicked.connect(self.SetR1P1)
        self.ButtonR1P2.clicked.connect(self.SetR1P2)
        self.ButtonR2P1.clicked.connect(self.SetR2P1)
        self.ButtonR2P2.clicked.connect(self.SetR2P2)
        self.ButtonSave.clicked.connect(self.SaveData)
        
        self.ColumnSelectUI = ColumnSelectUI()
        self.ColumnSelectUI.ButtonColumnSelect.clicked.connect(self.SetProteinColumn)
        self.ColumnSelectUI.ButtonColumnCancel.clicked.connect(self.ColumnSelectUI.close)

        self.ParamTSAUI = ParamTSAUI()
        self.ParamTSAUI.ButtonConfirm.clicked.connect(self.SetParams)
        self.ParamTSAUI.ButtonCancel.clicked.connect(self.ParamTSAUI.close)
        
        # server data
        self.columns = None
        self.prots = None
        self.resultTable = pd.DataFrame()
        self.resultData = []
        
        # default params
        self.haxis_TPP = 0.5
        self.minR2_TPP = 0.8
        self.maxPlateau_TPP = 0.3
        self.repCheck_TPP = 'True'
        self.minR2_NP_Null = 0.8
        self.minR2_NP_Alt = 0.8
        self.maxPlateau_NP = 0.
        self.minR2_Infl = 0.8
        self.numSD_Infl = 2
        self.Metr_Dist = 'cityblock'
        self.minR2_Dist = 0.8
        self.maxPlateau_Dist = 0.3
        

    def WarnMsg(self, Text):
        msg = QtWidgets.QMessageBox()
        msg.resize(550, 200)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(Text)
        msg.setWindowTitle("Warning")
        msg.exec_()    
    
    
    def ErrorMsg(self, Text):
        msg = QtWidgets.QMessageBox()
        msg.resize(550, 200)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(Text)
        msg.setWindowTitle("Error")
        msg.exec_()
    
    
    def OpenParams(self):
        self.ParamTSAUI.show()
    
    
    def SetParams(self):
        pass
        self.ParamTSAUI.close()
    
    
    def LoadProteinFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileNames, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"Load", "","All Files (*);;CSV Files (*.csv)", options=options)
        
        if len(fileNames) == 0:
            pass
        
        else:
            for fileName in fileNames:
                if fileName:
                    if fileName.split('.')[1] in ['csv', 'xlsx']:
                        self.ListFile.addItem(fileName)
                    else:
                        pass


    def ClearProteinFile(self):
        self.ListFile.clear()

        
    def FillTable(self, resultTable):
        self.tableWidgetProteinList.setRowCount(resultTable.shape[0])
        self.tableWidgetProteinList.setColumnCount(resultTable.shape[1])
        self.tableWidgetProteinList.setHorizontalHeaderLabels(resultTable.columns)
        self.tableWidgetProteinList.setVerticalHeaderLabels(resultTable.index.astype(str))
        for i in range(resultTable.shape[0]):
            for j in range(resultTable.shape[1]):
                if type(resultTable.iloc[i,j]) == np.float64:
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole, QVariant(float(resultTable.iloc[i,j])))
                    # item = QtWidgets.QTableWidgetItem(str(resultTable.iloc[i,j]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(resultTable.iloc[i,j]))
                self.tableWidgetProteinList.setItem(i, j, item)
                
                
    def ReplaceNonNumeric(self, data):
        for col in data.columns[1:]:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        # data = data.astype(float)
        keep = np.logical_not(np.isnan(np.sum(np.array(data)[:,1:], axis = 1).astype(float)))
        data = data.iloc[keep,:]
        data = data.reset_index(drop = True)
        return data


    def SelectProteinTable(self):
        selectItem = self.ListFile.currentItem()
        if not selectItem:
            self.ErrorMsg('No item is selected')
            return None
        try:
            if selectItem.text().split('.')[1] == 'csv':
                selectData = pd.read_csv(selectItem.text())
            elif selectItem.text().split('.')[1] == 'xlsx':
                selectData = pd.read_excel(selectItem.text())
            else:
                return None
        except:
            self.ErrorMsg('Cannot be load the selected file')
        
        if 'Accession' in selectData.columns:
            return selectData
        else:
            self.ErrorMsg('Accession is not given in the data')
            return None


    def SetR1P1(self):
        data = self.SelectProteinTable()
        if data is None:
            return None
        self.ColumnSelectUI.listWidget.clear()
        all_cols = data.columns
        for c in all_cols:
            self.ColumnSelectUI.listWidget.addItem(c)
        self.ColumnSelectUI.show()


    def SetR1P2(self):
        if self.columns == None:
            self.ErrorMsg('Please set Group 1')
        else:
            data = self.SelectProteinTable()
            if data is None:
                return None
            columns = ['Accession'] + self.columns
            try:
                data = data.loc[:, columns]
                data = self.ReplaceNonNumeric(data)
                if np.nanmax(data.loc[:, self.columns]) > 10:
                    self.WarnMsg('The data seems not normalized')
                self.tableRep1Protein2.setModel(TableModel(data))
            except:
                self.ErrorMsg('No columns matched with Group 1')


    def SetR2P1(self):
        if self.columns == None:
            self.ErrorMsg('Please set Group 1')
        else:
            data = self.SelectProteinTable()
            if data is None:
                return None
            columns = ['Accession'] + self.columns
            try:
                data = data.loc[:, columns]
                data = self.ReplaceNonNumeric(data)
                if np.nanmax(data.loc[:, self.columns]) > 10:
                    self.WarnMsg('The data seems not normalized')
                self.tableRep2Protein1.setModel(TableModel(data))
            except:
                self.ErrorMsg('No columns matched with Replicate 1')


    def SetR2P2(self):
        if self.columns == None:
            self.ErrorMsg('Please set Group 1')
        else:
            data = self.SelectProteinTable()
            if data is None:
                return None
            columns = ['Accession'] + self.columns
            try:
                data = data.loc[:, columns]
                data = self.ReplaceNonNumeric(data)
                if np.nanmax(data.loc[:, self.columns]) > 10:
                    self.WarnMsg('The data seems not normalized')
                self.tableRep2Protein2.setModel(TableModel(data))
            except:
                self.ErrorMsg('No columns matched with Replicate 1')


    def SetProteinColumn(self):
        data = self.SelectProteinTable()
        self.columns = [i.text() for i in self.ColumnSelectUI.listWidget.selectedItems()]
        try:
            [float(t.replace('T', '')) for t in self.columns]
        except:
            self.columns = None
            self.ErrorMsg('Selected columns can only be Txx, where xx is a number representing temperature')
            return None
        columns = ['Accession'] + self.columns
        data = data.loc[:, columns]
        data = self.ReplaceNonNumeric(data)
        if np.nanmax(data.loc[:, self.columns] > 10):
            self.WarnMsg('The data seems not normalized')
        self.ColumnSelectUI.close()
        self.tableRep1Protein1.setModel(TableModel(data))


    def ProcessBar(self, msg):
        self.progressBar.setValue(int(msg))
        
    
    def ResultData(self, msg):
        self.resultData.append(msg)
        # print(msg)
    
    # TPP Analysis 
    def ShowAnalTPP(self):
        columns = self.columns
        self.ColumnSelectUI.close()
        self.tableWidgetProteinList.clear()
        self.progressBar.setValue(0)
        
        r1p1Data = self.tableRep1Protein1.model()._data
        r1p2Data = self.tableRep1Protein2.model()._data
        r2p1Data = self.tableRep2Protein1.model()._data
        r2p2Data = self.tableRep2Protein2.model()._data

        haxis = self.haxis_TPP
        minR2 = self.minR2_TPP
        maxPlateau = self.maxPlateau_TPP
        
        temps = np.array([float(t.replace('T', '')) for t in columns])
        cols = ['Accession'] + columns
        
        r1p1 = r1p1Data.loc[:, cols]
        r1p2 = r1p2Data.loc[:, cols]
        if (r2p1Data is not None) and (r2p2Data is not None):
            r2p1 = r2p1Data.loc[:, cols]
            r2p2 = r2p2Data.loc[:, cols]
            prot_1 = np.intersect1d(list(r1p1.iloc[:,0]), list(r1p2.iloc[:,0]))
            prot_2 = np.intersect1d(list(r2p1.iloc[:,0]), list(r2p2.iloc[:,0]))
            self.prots = np.intersect1d(prot_1, prot_2)
        else:
            r2p1 = None
            r2p2 = None
            self.prots = np.intersect1d(list(r1p1.iloc[:,0]), list(r1p2.iloc[:,0]))
        
        self.TPPThread = TPPThread(self.prots, temps, r1p1, r1p2, r2p1, r2p2, minR2, maxPlateau, haxis)
        self.TPPThread._ind.connect(self.ProcessBar)
        self.TPPThread._res.connect(self.ResultData)
        self.TPPThread.start()
        self.TPPThread.finished.connect(self.VisualizeTPP)
        
        '''
        res = []
        for i, p in enumerate(prots):
            x = temps
            y1 = np.array(data_1[data_1.iloc[:,0] == p].iloc[0,1:])
            y2 = np.array(data_2[data_2.iloc[:,0] == p].iloc[0,1:])
            res.append(fit_curve(x, y1, y2, minR2, maxPlateau, h_axis))
            self.AnalTSAUI.progressBar.setValue(int(i / len(prots)))
        '''
        # res = Parallel(n_jobs=n_core, backend = 'threading')(delayed(fit_curve)(p) for p in prots)
        # res = pd.DataFrame(res)
    
    
    def VisualizeTPP(self):   
        prots = self.prots
        r2p1Data = self.tableRep2Protein1.model()._data
        r2p2Data = self.tableRep2Protein2.model()._data
        
        res = pd.DataFrame(self.resultData)
        if (r2p1Data is None) or (r2p2Data is None):
            res.columns = ['Rep1Group1_R2', 'Rep1Group2_R2', 'Rep1Group1_Tm', 'Rep1Group2_Tm', 'Rep1delta_Tm', 'Rep1min_Slope']
        else:
            res.columns = ['Rep1Group1_R2', 'Rep1Group2_R2', 'Rep1Group1_Tm', 'Rep1Group2_Tm', 'Rep1delta_Tm', 'Rep1min_Slope',
                           'Rep2Group1_R2', 'Rep2Group2_R2', 'Rep2Group1_Tm', 'Rep2Group2_Tm', 'Rep2delta_Tm', 'Rep2min_Slope']
        res['Accession'] = prots
    
        delta_Tm = res['Rep1delta_Tm']
        p_Val = []
        for i in range(len(res)):
            s = delta_Tm[i]
            pv = stats.t.sf(abs(s - np.nanmean(delta_Tm)) / np.nanstd(delta_Tm), len(delta_Tm)-1)
            p_Val.append(pv)
        res['Rep1pVal (-log10)'] = -np.log10(p_Val)
        score = -np.log10(np.array(p_Val)) * (res['Rep1Group1_R2'] * res['Rep1Group2_R2']) ** 2
            
        if (r2p1Data is not None) and (r2p2Data is not None):
            delta_Tm = res['Rep2delta_Tm']
            p_Val = []
            for i in range(len(res)):
                s = delta_Tm[i]
                pv = stats.t.sf(abs(s - np.nanmean(delta_Tm)) / np.nanstd(delta_Tm), len(delta_Tm)-1)
                p_Val.append(pv)
            res['Rep2pVal (-log10)'] = -np.log10(p_Val)
            score_2 = -np.log10(np.array(p_Val)) * (res['Rep2Group1_R2'] * res['Rep2Group2_R2']) ** 2
            score += score_2

        res['Score'] = score
        res = np.round(res, 3)
        # res = res[['Accession', 'Score', 'p_Val (-log10)', 'delta_Tm', 'Group1_R2', 'Group2_R2', 'Group1_Tm', 'Group2_Tm', 'min_Slope']]
        resultTable = res.sort_values(by = 'Score', axis = 0, ascending = False)
        
        self.resultData = []
        self.resultTable = resultTable
        self.FillTable(resultTable)

    '''
    def ShowMeltCurve(self):
        columns = self.columns
        proteinData1 = self.tableProtein1.model()._data
        proteinData2 = self.tableProtein2.model()._data
        
        header = [self.AnalTSAUI.tableWidgetProteinList.horizontalHeaderItem(i).text() for i in range(self.AnalTSAUI.tableWidgetProteinList.columnCount())]
        i = self.AnalTSAUI.tableWidgetProteinList.selectedItems()[0].row()
        j = header.index('Accession')
        ProteinAccession = self.AnalTSAUI.tableWidgetProteinList.item(i, j).text()

        self.AnalTSAUI.figureTSA.SingleTSAFigure(proteinData1, proteinData2, columns, ProteinAccession)
    '''

    def SaveData(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save", ".csv","CSV Files (*.csv)", options=options)
        if fileName:
            data = self.resultTable
            data.to_csv(fileName)    
        

        

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    ui = AnalTSAUI()
    ui.show()
    sys.exit(app.exec_())