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

    def calibrateAdaThresh(self, value):
        # work on adaptive thresholding
        return None

    # def showEyes()

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


            if ret == True:
                face = detect_faces(frame, face_cascade)
                if face is not None: # check for face

                    left_eye, right_eye, coords = detect_eyes(face, eye_cascade)

                    # Use threshold for both eyes. IN THE FUTURE IMPLEMENT INDIVIDUAL THRESHOLD
                    # FOR EACH EYE
                    threshold = self.ThresholdSlider.value()
                    self.threshold = threshold

                    # show rectangular window around eye  

                    # cv2.rectangle(face,(le_x, le_y),(le_x+le_w,le_y+le_h),(0,225,255),2) # left eye
                    # cv2.rectangle(face,(le_x, le_y),(le_x+le_w,le_y+le_h),(0,225,255),2) # right eye

                    if left_eye is not None: # check for a left eye
                        if self.leftCheckBox.isChecked():
                            _, keypoints = blob_process(left_eye, self.threshold, detector)
                            left_eye = draw_blobs(left_eye, keypoints)

                        # ensure that image is compatible to display left eye in right window
                        left_eye = np.require(left_eye, np.uint8, 'C')
                        # left_eye = draw_blobs(left_eye, keypoints)
                        self.display_eye_image(left_eye, 'left')

                    if right_eye is not None: # check for a right eye
                        if self.rightCheckBox.isChecked():
                            _, keypoints = blob_process(right_eye, self.threshold, detector)
                            right_eye = draw_blobs(right_eye, keypoints)

                        # ensure that image is compatible to display right eye in right window
                        right_eye = np.require(right_eye, np.uint8, 'C')
                        # right_eye = draw_blobs(right_eye, keypoints)
                        self.display_eye_image(right_eye, 'right')
                            
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

    def display_eye_image(self, img, window):
        # function eye_image() displays captured eyes onto QT Gui interface

        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4: # for RGBA
                qformat = QImage.Format_RGBA8888
            else: # for RGB
                qformat = QImage.Format_RGB888
        
        output_img = QImage(img, img.shape[0], img.shape[1], img.strides[0], qformat)
        if window == 'left':
            self.LeftEyeWindow.setPixmap(QPixmap.fromImage(output_img))
            self.LeftEyeWindow.setScaledContents(True)
        if window == 'right':
            self.RightEyeWindow.setPixmap(QPixmap.fromImage(output_img))
            self.RightEyeWindow.setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = capture()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
