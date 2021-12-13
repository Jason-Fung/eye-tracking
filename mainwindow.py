# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 909)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CameraButton = QtWidgets.QPushButton(self.centralwidget)
        self.CameraButton.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.CameraButton.setObjectName("CameraButton")
        self.SaveImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveImageButton.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.SaveImageButton.setObjectName("SaveImageButton")
        self.StopViewButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopViewButton.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.StopViewButton.setObjectName("StopViewButton")
        self.CameraLabel = QtWidgets.QGroupBox(self.centralwidget)
        self.CameraLabel.setGeometry(QtCore.QRect(190, 20, 481, 341))
        self.CameraLabel.setObjectName("CameraLabel")
        self.CameraWindow = QtWidgets.QLabel(self.CameraLabel)
        self.CameraWindow.setGeometry(QtCore.QRect(0, 20, 481, 321))
        self.CameraWindow.setText("")
        self.CameraWindow.setObjectName("CameraWindow")
        self.LeftEyeWindow = QtWidgets.QLabel(self.centralwidget)
        self.LeftEyeWindow.setGeometry(QtCore.QRect(760, 30, 111, 111))
        self.LeftEyeWindow.setFrameShape(QtWidgets.QFrame.Box)
        self.LeftEyeWindow.setText("")
        self.LeftEyeWindow.setObjectName("LeftEyeWindow")
        self.RightEyeWindow = QtWidgets.QLabel(self.centralwidget)
        self.RightEyeWindow.setGeometry(QtCore.QRect(950, 30, 111, 111))
        self.RightEyeWindow.setFrameShape(QtWidgets.QFrame.Box)
        self.RightEyeWindow.setText("")
        self.RightEyeWindow.setObjectName("RightEyeWindow")
        self.LeftEyeLabel = QtWidgets.QLabel(self.centralwidget)
        self.LeftEyeLabel.setGeometry(QtCore.QRect(790, 10, 51, 16))
        self.LeftEyeLabel.setObjectName("LeftEyeLabel")
        self.RightEyeLabel = QtWidgets.QLabel(self.centralwidget)
        self.RightEyeLabel.setGeometry(QtCore.QRect(980, 10, 61, 16))
        self.RightEyeLabel.setObjectName("RightEyeLabel")
        self.ThresholdSlider = QtWidgets.QSlider(self.centralwidget)
        self.ThresholdSlider.setGeometry(QtCore.QRect(190, 370, 481, 22))
        self.ThresholdSlider.setMaximum(255)
        self.ThresholdSlider.setProperty("value", 0)
        self.ThresholdSlider.setSliderPosition(0)
        self.ThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ThresholdSlider.setObjectName("ThresholdSlider")
        self.ThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.ThresholdLabel.setGeometry(QtCore.QRect(130, 370, 51, 21))
        self.ThresholdLabel.setObjectName("ThresholdLabel")
        self.ThresholdValue = QtWidgets.QSpinBox(self.centralwidget)
        self.ThresholdValue.setGeometry(QtCore.QRect(680, 370, 61, 22))
        self.ThresholdValue.setMaximum(255)
        self.ThresholdValue.setObjectName("ThresholdValue")
        self.leftCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.leftCheckBox.setGeometry(QtCore.QRect(790, 150, 61, 17))
        self.leftCheckBox.setObjectName("leftCheckBox")
        self.rightCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rightCheckBox.setGeometry(QtCore.QRect(980, 150, 61, 17))
        self.rightCheckBox.setObjectName("rightCheckBox")
        self.leftThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.leftThresholdLabel.setGeometry(QtCore.QRect(680, 180, 71, 21))
        self.leftThresholdLabel.setObjectName("leftThresholdLabel")
        self.leftThresholdValue = QtWidgets.QSpinBox(self.centralwidget)
        self.leftThresholdValue.setGeometry(QtCore.QRect(1100, 180, 61, 22))
        self.leftThresholdValue.setMaximum(255)
        self.leftThresholdValue.setObjectName("leftThresholdValue")
        self.leftThreshSlider = QtWidgets.QSlider(self.centralwidget)
        self.leftThreshSlider.setGeometry(QtCore.QRect(760, 180, 331, 22))
        self.leftThreshSlider.setMaximum(255)
        self.leftThreshSlider.setProperty("value", 0)
        self.leftThreshSlider.setSliderPosition(0)
        self.leftThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftThreshSlider.setObjectName("leftThreshSlider")
        self.rightThresholdValue = QtWidgets.QSpinBox(self.centralwidget)
        self.rightThresholdValue.setGeometry(QtCore.QRect(1100, 220, 61, 22))
        self.rightThresholdValue.setMaximum(255)
        self.rightThresholdValue.setObjectName("rightThresholdValue")
        self.rightThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.rightThresholdLabel.setGeometry(QtCore.QRect(680, 220, 71, 21))
        self.rightThresholdLabel.setObjectName("rightThresholdLabel")
        self.rightThreshSlider = QtWidgets.QSlider(self.centralwidget)
        self.rightThreshSlider.setGeometry(QtCore.QRect(760, 220, 331, 22))
        self.rightThreshSlider.setMaximum(255)
        self.rightThreshSlider.setProperty("value", 0)
        self.rightThreshSlider.setSliderPosition(0)
        self.rightThreshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightThreshSlider.setObjectName("rightThreshSlider")
        self.X_LeftEyeSeriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.X_LeftEyeSeriesLabel.setGeometry(QtCore.QRect(180, 420, 141, 16))
        self.X_LeftEyeSeriesLabel.setObjectName("X_LeftEyeSeriesLabel")
        self.Y_LeftEyeSeriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.Y_LeftEyeSeriesLabel.setGeometry(QtCore.QRect(180, 540, 141, 16))
        self.Y_LeftEyeSeriesLabel.setObjectName("Y_LeftEyeSeriesLabel")
        self.Track_X_LE = QtWidgets.QCheckBox(self.centralwidget)
        self.Track_X_LE.setGeometry(QtCore.QRect(110, 420, 61, 17))
        self.Track_X_LE.setObjectName("Track_X_LE")
        self.LeftEye_X_Series = QtWidgets.QFrame(self.centralwidget)
        self.LeftEye_X_Series.setGeometry(QtCore.QRect(180, 440, 891, 80))
        self.LeftEye_X_Series.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftEye_X_Series.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftEye_X_Series.setObjectName("LeftEye_X_Series")
        self.LeftEye_Y_Series = QtWidgets.QFrame(self.centralwidget)
        self.LeftEye_Y_Series.setGeometry(QtCore.QRect(180, 560, 891, 80))
        self.LeftEye_Y_Series.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftEye_Y_Series.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftEye_Y_Series.setObjectName("LeftEye_Y_Series")
        self.KF_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.KF_CheckBox.setGeometry(QtCore.QRect(880, 30, 61, 17))
        self.KF_CheckBox.setObjectName("KF_CheckBox")
        self.Save_Data_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Data_Button.setGeometry(QtCore.QRect(10, 140, 141, 31))
        self.Save_Data_Button.setObjectName("Save_Data_Button")
        self.RightEye_Y_Series = QtWidgets.QFrame(self.centralwidget)
        self.RightEye_Y_Series.setGeometry(QtCore.QRect(180, 790, 891, 80))
        self.RightEye_Y_Series.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightEye_Y_Series.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightEye_Y_Series.setObjectName("RightEye_Y_Series")
        self.X_RightEyeSeriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.X_RightEyeSeriesLabel.setGeometry(QtCore.QRect(180, 650, 141, 16))
        self.X_RightEyeSeriesLabel.setObjectName("X_RightEyeSeriesLabel")
        self.RightEye_X_Series = QtWidgets.QFrame(self.centralwidget)
        self.RightEye_X_Series.setGeometry(QtCore.QRect(180, 670, 891, 80))
        self.RightEye_X_Series.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightEye_X_Series.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightEye_X_Series.setObjectName("RightEye_X_Series")
        self.Y_RightEyeSeriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.Y_RightEyeSeriesLabel.setGeometry(QtCore.QRect(180, 770, 141, 16))
        self.Y_RightEyeSeriesLabel.setObjectName("Y_RightEyeSeriesLabel")
        self.Track_X_RE = QtWidgets.QCheckBox(self.centralwidget)
        self.Track_X_RE.setGeometry(QtCore.QRect(110, 650, 61, 17))
        self.Track_X_RE.setObjectName("Track_X_RE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 21))
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
        self.LeftEyeLabel.setText(_translate("MainWindow", "Left Eye"))
        self.RightEyeLabel.setText(_translate("MainWindow", "Right Eye"))
        self.ThresholdLabel.setText(_translate("MainWindow", "Threshold"))
        self.leftCheckBox.setText(_translate("MainWindow", "Track"))
        self.rightCheckBox.setText(_translate("MainWindow", "Track"))
        self.leftThresholdLabel.setText(_translate("MainWindow", "Left Thresh"))
        self.rightThresholdLabel.setText(_translate("MainWindow", "Right Thresh"))
        self.X_LeftEyeSeriesLabel.setText(_translate("MainWindow", "Left Eye (x - coord)"))
        self.Y_LeftEyeSeriesLabel.setText(_translate("MainWindow", "Left Eye (y - coord)"))
        self.Track_X_LE.setText(_translate("MainWindow", "Track"))
        self.KF_CheckBox.setText(_translate("MainWindow", "KF"))
        self.Save_Data_Button.setText(_translate("MainWindow", "Save Data"))
        self.X_RightEyeSeriesLabel.setText(_translate("MainWindow", "Right Eye (x - coord)"))
        self.Y_RightEyeSeriesLabel.setText(_translate("MainWindow", "Right Eye (y - coord)"))
        self.Track_X_RE.setText(_translate("MainWindow", "Track"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze "))
