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
from processing_functions import *

class capture(Ui_MainWindow):
    def __init__(self):
        super(capture,self).__init__() # parent constructor
        # uic.loadUi('mainwindow.ui',self)

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self,MainWindow)
        self.CameraButton.clicked.connect(self.onClicked)
        self.StopViewButton.clicked.connect(self.offClicked)
        self.ThresholdSlider.valueChanged.connect(self.handleSliderValueChange)
        self.ThresholdValue.valueChanged.connect(self.handleBoxValueChange)

    def handleSliderValueChange(self, value):
        # function is to connect with box value 
        self.ThresholdValue.setValue(value)

    def handleBoxValueChange(self, value):
        # function is to connect with slider 
        self.ThresholdSlider.setValue(value)


    def onClicked(self):
        # function onClicked() starts video streaming

        detector, face_cascade, eye_cascade = init_settings()

        _translate = QtCore.QCoreApplication.translate
        self.CameraLabel.setTitle(_translate("MainWindow","Active"))
        print("Webcam has connected")
        # start capturing video
        cap = cv2.VideoCapture(0)
        self.cap = cap
        while(cap.isOpened()):
            # capture frame-by-frame
            ret, frame = cap.read()
            frame = cv2.flip(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB),1) # flip horizontally

                # eye_h, eye_w, eye_c = eye.shape # h = height, w = width, c = channel
                # left_eye, right_eye = eyes
                # bytesPerLine_eye = 3 * width

                # qleft_eye = QImage(left_eye, eye_w, eye_h, bytesPerLine_eye, QImage.Format_RGB888)
                # qright_eye = QImage(right_eye, eye_w, eye_h, bytesPerLine_eye, QImage.Format_RGB888)
                # self.LeftEyeWindow.setPixmap(QPixmap.fromImage(qleft_eye))
                # self.RightEyeWindow.setPixmap(QPixmap.fromImage(qright_eye))
                # cv2.waitKey()

            if ret == True:
                face = detect_faces(frame, face_cascade)
                if face is not None: # check for face

                    left_eye, right_eye = detect_eyes(face, eye_cascade)
                    threshold = self.ThresholdSlider.value()
                    self.threshold = threshold

                    if left_eye is not None: # check for a left eye
                        left_eye_h, left_eye_w = left_eye.shape 
                        keypoints = blob_process(left_eye, self.threshold, detector)
                        left_eye = draw_blobs(left_eye, keypoints)

                    if right_eye is not None: # check for a right eye
                        keypoints = blob_process(right_eye, self.threshold, detector)
                        right_eye = draw_blobs(right_eye, keypoints)

                            
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
