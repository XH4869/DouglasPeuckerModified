# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DouglasPeucker.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt, Slot
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (QGridLayout, QLabel, QMenu, QMenuBar, QSizePolicy, 
     QSlider, QSpacerItem, QStatusBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget, 
     QFileDialog, QMessageBox)
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import functions
import numpy as np
import os

class Ui_MainWindow(QWidget):

    # self generated code from compiling .ui file with some modifications
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 704)
        MainWindow.setMinimumSize(QSize(70, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setFont(font)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setFont(font)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setFont(font)

        self.centralwidget = QWidget(MainWindow)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QRect(4, 2, 1105, 641))

        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.tabWidget = QTabWidget(self.layoutWidget)
        self.tabWidget.setMinimumSize(QSize(500, 600))
        self.tabWidget.setTabPosition(QTabWidget.South)

        self.tab_xyz = QWidget()
        self.tab_xyz_vLayout = QVBoxLayout(self.tab_xyz)
        self.plot_xyz = FigureCanvas(Figure())
        self.xyz_ax = self.plot_xyz.figure.subplots(subplot_kw={"projection": "3d"})
        self.tab_xyz_vLayout.addWidget(NavigationToolbar(self.plot_xyz, self))
        self.tab_xyz_vLayout.addWidget(self.plot_xyz)
        self.tabWidget.addTab(self.tab_xyz, "")

        self.tab_dh = QWidget()
        self.tab_dh_vLayout = QVBoxLayout(self.tab_dh)
        self.plot_dh = FigureCanvas(Figure())
        self.dh_ax = self.plot_dh.figure.subplots()
        self.tab_dh_vLayout.addWidget(NavigationToolbar(self.plot_dh, self))
        self.tab_dh_vLayout.addWidget(self.plot_dh)
        self.tabWidget.addTab(self.tab_dh, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.gridLayout = QGridLayout()
        self.mHSpacer1 = QSpacerItem(328, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.mHSpacer1, 0, 0, 1, 1)

        self.mSlider = QSlider(self.layoutWidget)
        self.mSlider.setMinimumSize(QSize(200, 30))
        self.mSlider.setMaximumSize(QSize(16777215, 30))
        self.mSlider.setFont(font)
        self.mSlider.setMaximum(50)
        self.mSlider.setSingleStep(1)
        self.mSlider.setValue(15)
        self.mSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.mSlider, 0, 1, 1, 1)

        self.mTextEdit = QTextEdit(self.layoutWidget)
        self.mTextEdit.setMinimumSize(QSize(50, 30))
        self.mTextEdit.setMaximumSize(QSize(60, 30))
        self.mTextEdit.setPlainText('1.5')

        self.gridLayout.addWidget(self.mTextEdit, 0, 2, 1, 1)

        self.mLabel = QLabel(self.layoutWidget)
        self.mLabel.setMinimumSize(QSize(0, 30))
        self.mLabel.setMaximumSize(QSize(16777215, 30))
        self.mLabel.setFont(font)

        self.gridLayout.addWidget(self.mLabel, 0, 3, 1, 1)

        self.mHSpacer2 = QSpacerItem(398, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.mHSpacer2, 0, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1129, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        self.openFilePath = None
        self.isClear = False

        # connect signals to slots
        self.mSlider.valueChanged.connect(self.updateTextEdit)
        self.mSlider.valueChanged.connect(self.redoSimplify)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionClose.triggered.connect(self.closeFile)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    # self generated code from compiling .ui file
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Douglas Peucker Algorithm", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_xyz), QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dh), QCoreApplication.translate("MainWindow", u"Distance-Height", None))
        self.mLabel.setText(QCoreApplication.translate("MainWindow", u"epsilon value", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


    # helping functions
    def simplify(self):
        '''main function to do height simplification using Douglas-Peucker algorithm'''
        features = functions.getPointsList(self.openFilePath)
        self.newFeatures = []
        for feature in features:
            # clear the canvas before drawing
            self.xyz_ax.clear()
            self.dh_ax.clear()

            # set axis labels for distance-height plot
            self.dh_ax.set_xlabel('Accumulated distance to starting point')
            self.dh_ax.set_ylabel('Relative height to starting point')

            # here only shows the relative coordinates
            x = np.array(feature)[:, 0]
            x = (x - np.amin(x)) / 100
            y = np.array(feature)[:, 1]
            y = (y - np.amin(y)) / 100
            
            # ensure the same minimal z value before and after the simplification, z value is also relative value
            z = np.array(feature)[:, 2]
            zmin = np.amin(z)
            z = (z - zmin) / 10

            self.xyz_ax.plot(x, y, z, color='b', label='before')

            ptList = functions.transformCoord(feature)
            x = np.array(ptList)[:, 0]
            y = np.array(ptList)[:, 1]
            self.dh_ax.plot(x, y, color='b', label='before')

            # simplify height and draw the results
            epsilon = float(self.mTextEdit.toPlainText())
            resList = functions.douglasPeucker(ptList, epsilon)
            newFeature = functions.restorePtList(resList, feature)
            self.newFeatures.append(newFeature)

            x = np.array(newFeature)[:, 0]
            x = (x - np.amin(x)) / 100
            y = np.array(newFeature)[:, 1]
            y = (y - np.amin(y)) / 100
            z = np.array(newFeature)[:, 2]
            z = (z - zmin) / 10
            self.xyz_ax.plot(x, y, z, color='r', label='after')
            self.xyz_ax.legend()

            x = np.array(resList)[:, 0]
            y = np.array(resList)[:, 1]
            self.dh_ax.plot(x, y, color='r', label='after')
            self.dh_ax.legend()

            # force the canvas to redraw, otherwise it will not refresh until interacting with the plot
            self.plot_xyz.draw()
            self.plot_dh.draw()
        return


    @Slot()
    def openFile(self):
        self.openFilePath = QFileDialog.getOpenFileName(parent=self, caption='Select a file', dir=os.getcwd(), filter='Shapefile (*.shp)')
        # only keep the file path
        self.openFilePath = self.openFilePath[0]
        if self.openFilePath:
            self.isClear = False
            self.simplify()
        return


    def saveFile(self):
        if self.openFilePath:
            self.saveFilePath = QFileDialog.getSaveFileName(parent=self, caption='Save file', dir=os.getcwd(), filter='Shapefile (*.shp)')
            functions.writeShp(self.newFeatures, self.saveFilePath[0])
        return


    def closeFile(self):
        # clear the plots
        self.xyz_ax.clear()
        self.dh_ax.clear()
        self.plot_xyz.draw()
        self.plot_dh.draw()

        # set slider value to default
        self.isClear = True
        self.mSlider.setValue(15)

        # set file path to none
        self.openFilePath = None
        return
    

    def updateTextEdit(self, value):
        # show the real epsilon value by dividing by 10, QSlider does not support non-int type 
        self.mTextEdit.setPlainText(str(value / 10))
        return


    def redoSimplify(self):
        if self.isClear:
            return
        elif self.openFilePath:
            self.simplify()
            return
        else: 
            return
