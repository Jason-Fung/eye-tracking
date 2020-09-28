# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CameraButton = QtWidgets.QPushButton(self.centralwidget)
        self.CameraButton.setGeometry(QtCore.QRect(60, 110, 141, 31))
        self.CameraButton.setObjectName("CameraButton")
        self.SaveImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveImageButton.setGeometry(QtCore.QRect(60, 190, 141, 31))
        self.SaveImageButton.setObjectName("SaveImageButton")
        self.StopViewButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopViewButton.setGeometry(QtCore.QRect(60, 150, 141, 31))
        self.StopViewButton.setObjectName("StopViewButton")
        self.CameraLabel = QtWidgets.QGroupBox(self.centralwidget)
        self.CameraLabel.setGeometry(QtCore.QRect(240, 110, 481, 341))
        self.CameraLabel.setObjectName("CameraLabel")
        self.CameraWindow = QtWidgets.QLabel(self.CameraLabel)
        self.CameraWindow.setGeometry(QtCore.QRect(0, 20, 481, 321))
        self.CameraWindow.setText("")
        self.CameraWindow.setObjectName("CameraWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CameraButton.setText(_translate("MainWindow", "Show Camera"))
        self.SaveImageButton.setText(_translate("MainWindow", "Save Image"))
        self.StopViewButton.setText(_translate("MainWindow", "Stop Viewing"))
        self.CameraLabel.setTitle(_translate("MainWindow", "Not Active"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
