# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from mainwindow import *
import dlib

class capture(Ui_MainWindow):
    def __init__(self):
        super(capture,self).__init__() # parent constructor
        # uic.loadUi('mainwindow.ui',self)

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self,MainWindow)
        self.CameraButton.clicked.connect(self.onClicked)
        self.StopViewButton.clicked.connect(self.offClicked)

    def onClicked(self):
        # function onClicked() starts video streaming

        _translate = QtCore.QCoreApplication.translate
        self.CameraLabel.setTitle(_translate("MainWindow","Active"))
        print("Webcam has connected")
        # start capturing video
        cap = cv2.VideoCapture(0)
        self.cap = cap
        while(cap.isOpened()):
            # capture frame-by-frame
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # frame.data[:,:,::-1]
            if ret == True:
                # Put capturing frame into QLabel in Qt 
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame, width, height, bytesPerLine, QImage.Format_RGB888)
                self.CameraWindow.setPixmap(QPixmap.fromImage(qImg))
                cv2.waitKey()

    def offClicked(self):
        # function offClicked() stops video streaming
        _translate = QtCore.QCoreApplication.translate
        self.CameraLabel.setTitle(_translate("MainWindow","Not Active"))
        self.cap.release()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = capture()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
