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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib as mpl
from typing import *
import pandas as pd


class capture(Ui_MainWindow):
    def __init__(self):
        super(capture,self).__init__() # parent constructor
        # uic.loadUi('mainwindow.ui',self)

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self,MainWindow)
        self.CameraButton.clicked.connect(self.onClicked)
        self.StopViewButton.clicked.connect(self.offClicked)
        self.Save_Data_Button.clicked.connect(self.save_data_click)


        self.ThresholdSlider.valueChanged.connect(self.handleSliderValueChange)
        self.ThresholdValue.valueChanged.connect(self.handleBoxValueChange)
        
        self.leftThreshSlider.valueChanged.connect(self.lefthandleSliderValueChange)
        self.leftThresholdValue.valueChanged.connect(self.lefthandleBoxValueChange)

        self.rightThreshSlider.valueChanged.connect(self.righthandleSliderValueChange)
        self.rightThresholdValue.valueChanged.connect(self.righthandleBoxValueChange)

        # set up left eye data streaming window
        self.LE_X_series_Box = QtWidgets.QVBoxLayout()
        self.LeftEye_X_Series.setLayout(self.LE_X_series_Box)
        self.LE_Y_series_Box = QtWidgets.QVBoxLayout()
        self.LeftEye_Y_Series.setLayout(self.LE_Y_series_Box)

        # set up right eye data streaming window
        self.RE_X_series_Box = QtWidgets.QVBoxLayout()
        self.RightEye_X_Series.setLayout(self.RE_X_series_Box)
        self.RE_Y_series_Box = QtWidgets.QVBoxLayout()
        self.RightEye_Y_Series.setLayout(self.RE_Y_series_Box)


        # Instantiate figure canvas and place into widget
        # x coordinate time series
        self.myFig_LE_X = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.LE_X_series_Box.addWidget(self.myFig_LE_X)
        # y coordinate time series
        # myFig_LE_Y = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.myFig_LE_Y = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.LE_Y_series_Box.addWidget(self.myFig_LE_Y)

        # Instantiate figure canvas and place into widget
        # x coordinate time series
        self.myFig_RE_X = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.RE_X_series_Box.addWidget(self.myFig_RE_X)
        # y coordinate time series
        # myFig_LE_Y = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.myFig_RE_Y = MyFigureCanvas(x_len = 200, y_range = [0,40], interval = 1)
        self.RE_Y_series_Box.addWidget(self.myFig_RE_Y)


    def handleSliderValueChange(self, value):
        # function is to connect with box value 
        self.ThresholdValue.setValue(value)

    def handleBoxValueChange(self, value):
        # function is to connect with slider 
        self.ThresholdSlider.setValue(value)

    def lefthandleSliderValueChange(self, value):
        # function is to connect with box value 
        self.leftThresholdValue.setValue(value)

    def lefthandleBoxValueChange(self, value):
        # function is to connect with slider 
        self.leftThreshSlider.setValue(value)

    def righthandleSliderValueChange(self, value):
        # function is to connect with box value 
        self.rightThresholdValue.setValue(value)

    def righthandleBoxValueChange(self, value):
        # function is to connect with slider 
        self.rightThreshSlider.setValue(value)

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

        # Original Kalman Filter Pre-process matrices
        # assume that the eye follows a linear model x(t) = x_o + vdt

        trans_matrix = np.array([[1, 1/60, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 1/60],
                                [0, 0, 0, 1]])

        init_state_mean = np.array([20,
                                    0,
                                    20,
                                    0])

        observ_matrix = [[1, 0, 0, 0],
                         [0, 0, 1, 0]]
        
        # Covariance Matrices
        observ_cov = np.diag([0.3**2,0.3**2]) # observation covariance
        state_cov = np.diag([0, 1, 0, 1]) # initial state covariance
        trans_cov = np.diag([0.01, 0.05, 0.01, 0.05])

        kf = KalmanFilter(transition_matrices= trans_matrix,
						observation_matrices = observ_matrix,
						initial_state_mean = init_state_mean,
						observation_covariance = observ_cov,
						initial_state_covariance = state_cov,
						transition_covariance = trans_cov,
                        em_vars = ['transition_covariance', 'observation_covariance'])

        # data 
        left_eye_data = []
        right_eye_data = []

        # set data limit for efficient data storage
        data_lim = 500

        # start capturing video
        cap = cv2.VideoCapture(0)
        self.cap = cap
        while(cap.isOpened()):
            # capture frame-by-frame
            ret, frame = cap.read()
            frame = cv2.flip(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB),1) # flip horizontally

            if ret == True:
                face = detect_faces(frame, face_cascade)
                # print(np.shape(face))
                if face is not None: # check for face

                    left_eye, right_eye, coords = detect_eyes(face, eye_cascade)
                
                    # Use threshold for both eyes. IN THE FUTURE IMPLEMENT INDIVIDUAL THRESHOLD
                    # FOR EACH EYE
                    threshold = self.ThresholdSlider.value()
                    self.threshold = threshold

                    left_threshold = self.leftThreshSlider.value()
                    self.left_threshold = left_threshold

                    right_threshold = self.rightThreshSlider.value()
                    self.right_threshold = right_threshold

                    if left_eye is not None: # check for a left eye
                        if self.leftCheckBox.isChecked():
                            _, l_keypoints = blob_process(left_eye, self.left_threshold, detector)
                            if l_keypoints is not ():
                                left_eye_data.append([l_keypoints[0].pt[0],l_keypoints[0].pt[1]])

                                if len(left_eye_data) == data_lim+1:
                                    # update the list of positions if the length of the array reaches
                                    # the data limit for efficient storage.
                                    # Pop the first value of the list after appending the new coordinates.
                                    left_eye_data.pop(0)
                                
                                self.left_eye_data = left_eye_data
                                if self.Track_X_LE.isChecked():
                                    self.myFig_LE_X._update_canvas_(data = l_keypoints[0].pt[0])
                                    self.myFig_LE_Y._update_canvas_(data = l_keypoints[0].pt[1])
                            
                            else:
                                left_eye_data.append(np.array([0,0]))
                                if len(left_eye_data) == data_lim+1:
                                    # update the list of positions if the length of the array reaches
                                    # the data limit for efficient storage.
                                    # Pop the first value of the list after appending the new coordinates.
                                    left_eye_data.pop(0)
                            
                            # apply the kalman filter 
                            if self.KF_CheckBox.isChecked():
                                # create new keypoints
                                # kf.em(left_eye_data, n_iter = 2)
                                l_next_mean, _ = kf.smooth(left_eye_data)
                                # print(next_mean)
                                self.left_filtered_data = l_next_mean
                                l_tmp = l_next_mean[-1]
                                l_new_keypoints = []
                                l_new_keypoints.append(cv2.KeyPoint(l_tmp[0],l_tmp[2],15))
                                left_eye = draw_blobs(left_eye, l_new_keypoints, color = [0,255,0])
                                # print(l_new_keypoints[0].pt[0] - l_keypoints[0].pt[0])

                            left_eye = draw_blobs(left_eye, l_keypoints)
                    
                        # ensure that image is compatible to display left eye in right window
                        left_eye = np.require(left_eye, np.uint8, 'C')
                        # left_eye = draw_blobs(left_eye, keypoints)
                        self.display_eye_image(left_eye, 'left')
                        
                    else: # does not find eye
                        self.myFig_LE_X._update_canvas_(data = 0)
                        self.myFig_LE_Y._update_canvas_(data = 0)

                    if right_eye is not None: # check for a left eye
                        if self.leftCheckBox.isChecked():
                            _, r_keypoints = blob_process(right_eye, self.right_threshold, detector)
                            if r_keypoints is not ():
                                right_eye_data.append([r_keypoints[0].pt[0],r_keypoints[0].pt[1]])

                                if len(right_eye_data) == data_lim+1:
                                    # update the list of positions if the length of the array reaches
                                    # the data limit for efficient storage.
                                    # Pop the first value of the list after appending the new coordinates.
                                    right_eye_data.pop(0)
                                
                                self.right_eye_data = right_eye_data
                                if self.Track_X_RE.isChecked():
                                    self.myFig_RE_X._update_canvas_(data = r_keypoints[0].pt[0])
                                    self.myFig_RE_Y._update_canvas_(data = r_keypoints[0].pt[1])
                            
                            else:
                                right_eye_data.append(np.array([0,0]))
                                if len(right_eye_data) == data_lim+1:
                                    # update the list of positions if the length of the array reaches
                                    # the data limit for efficient storage.
                                    # Pop the first value of the list after appending the new coordinates.
                                    right_eye_data.pop(0)
                            
                            # apply the kalman filter 
                            if self.KF_CheckBox.isChecked():
                                # create new keypoints
                                # kf.em(left_eye_data, n_iter = 2)
                                r_next_mean, _ = kf.smooth(right_eye_data)
                                # print(next_mean)
                                self.right_filtered_data = r_next_mean
                                r_tmp = r_next_mean[-1]
                                r_new_keypoints = []
                                r_new_keypoints.append(cv2.KeyPoint(r_tmp[0],r_tmp[2],15))
                                right_eye = draw_blobs(right_eye, r_new_keypoints, color = [0,255,0])
                                # print(l_new_keypoints[0].pt[0] - l_keypoints[0].pt[0])

                            right_eye = draw_blobs(right_eye, r_keypoints)
                    
                        # ensure that image is compatible to display left eye in right window
                        right_eye = np.require(right_eye, np.uint8, 'C')
                        # left_eye = draw_blobs(left_eye, keypoints)
                        self.display_eye_image(right_eye, 'right')
                        
                    else: # does not find eye
                        self.myFig_RE_X._update_canvas_(data = 0)
                        self.myFig_RE_Y._update_canvas_(data = 0)
                
                else: # does not find face
                    self.myFig_LE_X._update_canvas_(data = 0)
                    self.myFig_LE_Y._update_canvas_(data = 0)
                    self.myFig_RE_X._update_canvas_(data = 0)
                    self.myFig_RE_Y._update_canvas_(data = 0)

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
    
    def save_data_click(self):
        new_list = [self.left_eye_data,self.right_eye_data, 
                    self.left_filtered_data,self.right_filtered_data]
        df = pd.DataFrame(new_list)
        df.to_csv('test_data.csv')
        # function save_data_click() saves a segment of time series data 


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


class MyFigureCanvas(FigureCanvas):
    # FigureCanvas used to draw live plot 
    def __init__(self, x_len:int, y_range:list, interval:int) -> None:
        super().__init__(mpl.figure.Figure())
        # Range Settings
        self._x_len = x_len
        self._y_range_ = y_range

        # store two lists _x_ and y
        self._x_ = list(range(0,x_len))
        self._y_ = [0]*x_len

        # store a figure ax
        self._ax_ = self.figure.subplots()
        self._ax_.set_ylim(ymin = self._y_range_[0], ymax = self._y_range_[1])
        self._line_, = self._ax_.plot(self._x_,self._y_)
        self.draw()

        # # set timer
        # self._timer_ = self.new_timer(interval, [(self._update_canvas_, (), {})])
        # self._timer_.start()
        return
    
    def _update_canvas_(self, data):
        # function gets called regularly by timer

        self._y_.append(data)
        self._y_ = self._y_[-self._x_len:] # truncate list y
        self._line_.set_ydata(self._y_)
        self._ax_.draw_artist(self._ax_.patch)
        self._ax_.draw_artist(self._line_)
        self.update()
        self.flush_events()
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = capture()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
