# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtMultimedia
import glob

class audio_player(QtMultimedia.QMediaPlayer):
    def __init__(self):
        super(audio_player, self).__init__()
        self.currentDataHolder = ""

    def change_media(self, url, dataholder_name):
        self.currentDataHolder = dataholder_name
        self.url = url
        self.content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(self.url))
        self.setMedia(self.content)

class data_holder(object):
    def __init__(self, parent_object, text, url, dataholder_name, file_name):
        self.text = text
        self.parent_object = parent_object
        self.url = url
        self.dataholder_name = dataholder_name
        self.file_name = file_name
        self.audio_position = 0
        self.audio_duration = 0

        self.frame_3 = QtWidgets.QFrame(self.parent_object)
        self.frame_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(900, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setFormat("")
        # self.progressBar.setObjectName("progressBar")
        self.progressBar = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.frame_2)
        self.gridLayout_3.addWidget(self.progressBar, 0, 0, 1, 3)
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setText("")
        self.toolButton.setIcon(QIcon('play.png'))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.play)
        self.gridLayout_3.addWidget(self.toolButton, 1, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_3.setText("")
        self.toolButton_3.setIcon(QIcon('pause.png'))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.pause)
        self.gridLayout_3.addWidget(self.toolButton_3, 1, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(QIcon('stop.png'))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.stop)
        self.gridLayout_3.addWidget(self.toolButton_2, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.allow_edit_text)
        self.gridLayout_4.addWidget(self.radioButton, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_5)
        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        player.positionChanged.connect(self.changeLabel)
        self.retranslateUi()

    def allow_edit_text(self):
        if self.radioButton.isChecked():
            self.lineEdit.setReadOnly(False)
            self.lineEdit.setFocus()
        else:
            self.lineEdit.setReadOnly(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.radioButton.setText(_translate("MainWindow", "Edit"))
        self.pushButton.setText(_translate("MainWindow", "Open Editor"))
        self.label.setText(_translate("MainWindow", self.file_name))
        self.lineEdit.setText(self.text)

    def changeLabel(self):
        if self.dataholder_name == player.currentDataHolder:
            if player.duration() == 0:
                progress_value = 0
            else:
                progress_value = int((player.position() / player.duration()) * 100)
            self.progressBar.setSliderPosition(progress_value)
            print(progress_value)

    def play(self):
        player.change_media(self.url, self.dataholder_name)
        player.setPosition(self.audio_position)
        player.play()
        self.update_media_status()

    def pause(self):
        player.pause()
        self.update_media_status()

    def stop(self):
        player.stop()
        self.update_media_status()
        self.audio_position = 0

    def update_media_status(self):
        self.audio_position = player.position()
        self.audio_duration = player.duration()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1169, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1149, 726))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.read_data("/home/othman/Downloads/Nos_Ketab_Final/GUI_trial/")
        self.read_wavs("/home/othman/Downloads/Nos_Ketab_Final/GUI_trial/")

        global player
        player = audio_player()
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(self.wav_paths[0]))
        player.setMedia(content)

        for i, p in enumerate(self.text_paths):
            file = open(p, "r")
            text = file.read()
            url = self.wav_paths[i]
            url = url.split("/")
            print(url)
            dataholder_name = "dataholder" + str(i)
            exec("self." + dataholder_name + "= data_holder(self.centralwidget, text, url, dataholder_name, url[-1])")
            exec("self.verticalLayout.addWidget(self." + dataholder_name + ".frame_3)")
            exec("self.verticalLayout.addItem(self." + dataholder_name + ".spacerItem)")

        # self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frame_3.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        # self.frame_3.setSizePolicy(sizePolicy)
        # self.frame_3.setMinimumSize(QtCore.QSize(900, 101))
        # self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_3.setObjectName("frame_3")
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.frame_2 = QtWidgets.QFrame(self.frame_3)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        # self.frame_2.setSizePolicy(sizePolicy)
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        # self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        # self.gridLayout_3.setObjectName("gridLayout_3")
        # self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        # self.gridLayout_3.addWidget(self.progressBar, 0, 0, 1, 3)
        # self.toolButton = QtWidgets.QToolButton(self.frame_2)
        # self.toolButton.setText("")
        # self.toolButton.setObjectName("toolButton")
        # self.gridLayout_3.addWidget(self.toolButton, 1, 0, 1, 1)
        # self.toolButton_3 = QtWidgets.QToolButton(self.frame_2)
        # self.toolButton_3.setText("")
        # self.toolButton_3.setObjectName("toolButton_3")
        # self.gridLayout_3.addWidget(self.toolButton_3, 1, 1, 1, 1)
        # self.toolButton_2 = QtWidgets.QToolButton(self.frame_2)
        # self.toolButton_2.setText("")
        # self.toolButton_2.setObjectName("toolButton_2")
        # self.gridLayout_3.addWidget(self.toolButton_2, 1, 2, 1, 1)
        # self.horizontalLayout.addWidget(self.frame_2)
        # self.frame_4 = QtWidgets.QFrame(self.frame_3)
        # self.frame_4.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(70)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        # self.frame_4.setSizePolicy(sizePolicy)
        # self.frame_4.setAutoFillBackground(False)
        # self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_4.setObjectName("frame_4")
        # self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        # self.gridLayout_4.setObjectName("gridLayout_4")
        # self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.gridLayout_4.addWidget(self.pushButton_2, 1, 2, 1, 1)
        # self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.lineEdit.setFont(font)
        # self.lineEdit.setObjectName("lineEdit")
        # self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 3)
        # self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        # self.radioButton.setSizePolicy(sizePolicy)
        # self.radioButton.setObjectName("radioButton")
        # self.gridLayout_4.addWidget(self.radioButton, 1, 0, 1, 1)
        # self.pushButton = QtWidgets.QPushButton(self.frame_4)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        # self.pushButton.setSizePolicy(sizePolicy)
        # self.pushButton.setObjectName("pushButton")
        # self.gridLayout_4.addWidget(self.pushButton, 1, 1, 1, 1)
        # self.horizontalLayout.addWidget(self.frame_4)
        # self.frame_5 = QtWidgets.QFrame(self.frame_3)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(10)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        # self.frame_5.setSizePolicy(sizePolicy)
        # self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_5.setObjectName("frame_5")
        # self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        # self.gridLayout_5.setObjectName("gridLayout_5")
        # self.label = QtWidgets.QLabel(self.frame_5)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        # self.horizontalLayout.addWidget(self.frame_5)
        # self.verticalLayout.addWidget(self.frame_3)
        # spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # self.verticalLayout.addItem(spacerItem)
        # self.frame_40 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frame_40.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        # self.frame_40.setSizePolicy(sizePolicy)
        # self.frame_40.setMinimumSize(QtCore.QSize(900, 101))
        # self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_40.setObjectName("frame_40")
        # self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_40)
        # self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_13.setSpacing(0)
        # self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        # self.frame_44 = QtWidgets.QFrame(self.frame_40)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        # self.frame_44.setSizePolicy(sizePolicy)
        # self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_44.setObjectName("frame_44")
        # self.gridLayout_39 = QtWidgets.QGridLayout(self.frame_44)
        # self.gridLayout_39.setObjectName("gridLayout_39")
        # self.progressBar_13 = QtWidgets.QProgressBar(self.frame_44)
        # self.progressBar_13.setProperty("value", 24)
        # self.progressBar_13.setObjectName("progressBar_13")
        # self.gridLayout_39.addWidget(self.progressBar_13, 0, 0, 1, 3)
        # self.toolButton_37 = QtWidgets.QToolButton(self.frame_44)
        # self.toolButton_37.setText("")
        # self.toolButton_37.setObjectName("toolButton_37")
        # self.gridLayout_39.addWidget(self.toolButton_37, 1, 0, 1, 1)
        # self.toolButton_38 = QtWidgets.QToolButton(self.frame_44)
        # self.toolButton_38.setText("")
        # self.toolButton_38.setObjectName("toolButton_38")
        # self.gridLayout_39.addWidget(self.toolButton_38, 1, 1, 1, 1)
        # self.toolButton_39 = QtWidgets.QToolButton(self.frame_44)
        # self.toolButton_39.setText("")
        # self.toolButton_39.setObjectName("toolButton_39")
        # self.gridLayout_39.addWidget(self.toolButton_39, 1, 2, 1, 1)
        # self.horizontalLayout_13.addWidget(self.frame_44)
        # self.frame_48 = QtWidgets.QFrame(self.frame_40)
        # self.frame_48.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(70)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        # self.frame_48.setSizePolicy(sizePolicy)
        # self.frame_48.setAutoFillBackground(False)
        # self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_48.setObjectName("frame_48")
        # self.gridLayout_40 = QtWidgets.QGridLayout(self.frame_48)
        # self.gridLayout_40.setObjectName("gridLayout_40")
        # self.pushButton_25 = QtWidgets.QPushButton(self.frame_48)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        # self.pushButton_25.setSizePolicy(sizePolicy)
        # self.pushButton_25.setObjectName("pushButton_25")
        # self.gridLayout_40.addWidget(self.pushButton_25, 1, 2, 1, 1)
        # self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_48)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.lineEdit_13.setFont(font)
        # self.lineEdit_13.setObjectName("lineEdit_13")
        # self.gridLayout_40.addWidget(self.lineEdit_13, 0, 0, 1, 3)
        # self.radioButton_13 = QtWidgets.QRadioButton(self.frame_48)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.radioButton_13.sizePolicy().hasHeightForWidth())
        # self.radioButton_13.setSizePolicy(sizePolicy)
        # self.radioButton_13.setObjectName("radioButton_13")
        # self.gridLayout_40.addWidget(self.radioButton_13, 1, 0, 1, 1)
        # self.pushButton_26 = QtWidgets.QPushButton(self.frame_48)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        # self.pushButton_26.setSizePolicy(sizePolicy)
        # self.pushButton_26.setObjectName("pushButton_26")
        # self.gridLayout_40.addWidget(self.pushButton_26, 1, 1, 1, 1)
        # self.horizontalLayout_13.addWidget(self.frame_48)
        # self.frame_49 = QtWidgets.QFrame(self.frame_40)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(10)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        # self.frame_49.setSizePolicy(sizePolicy)
        # self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_49.setObjectName("frame_49")
        # self.gridLayout_41 = QtWidgets.QGridLayout(self.frame_49)
        # self.gridLayout_41.setObjectName("gridLayout_41")
        # self.label_13 = QtWidgets.QLabel(self.frame_49)
        # self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_13.setObjectName("label_13")
        # self.gridLayout_41.addWidget(self.label_13, 0, 0, 1, 1)
        # self.horizontalLayout_13.addWidget(self.frame_49)
        # self.verticalLayout.addWidget(self.frame_40)
        # spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # self.verticalLayout.addItem(spacerItem1)
        # self.frame_50 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frame_50.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        # self.frame_50.setSizePolicy(sizePolicy)
        # self.frame_50.setMinimumSize(QtCore.QSize(900, 101))
        # self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_50.setObjectName("frame_50")
        # self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_50)
        # self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_14.setSpacing(0)
        # self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        # self.frame_51 = QtWidgets.QFrame(self.frame_50)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        # self.frame_51.setSizePolicy(sizePolicy)
        # self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_51.setObjectName("frame_51")
        # self.gridLayout_42 = QtWidgets.QGridLayout(self.frame_51)
        # self.gridLayout_42.setObjectName("gridLayout_42")
        # self.progressBar_14 = QtWidgets.QProgressBar(self.frame_51)
        # self.progressBar_14.setProperty("value", 24)
        # self.progressBar_14.setObjectName("progressBar_14")
        # self.gridLayout_42.addWidget(self.progressBar_14, 0, 0, 1, 3)
        # self.toolButton_40 = QtWidgets.QToolButton(self.frame_51)
        # self.toolButton_40.setText("")
        # self.toolButton_40.setObjectName("toolButton_40")
        # self.gridLayout_42.addWidget(self.toolButton_40, 1, 0, 1, 1)
        # self.toolButton_41 = QtWidgets.QToolButton(self.frame_51)
        # self.toolButton_41.setText("")
        # self.toolButton_41.setObjectName("toolButton_41")
        # self.gridLayout_42.addWidget(self.toolButton_41, 1, 1, 1, 1)
        # self.toolButton_42 = QtWidgets.QToolButton(self.frame_51)
        # self.toolButton_42.setText("")
        # self.toolButton_42.setObjectName("toolButton_42")
        # self.gridLayout_42.addWidget(self.toolButton_42, 1, 2, 1, 1)
        # self.horizontalLayout_14.addWidget(self.frame_51)
        # self.frame_52 = QtWidgets.QFrame(self.frame_50)
        # self.frame_52.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(70)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        # self.frame_52.setSizePolicy(sizePolicy)
        # self.frame_52.setAutoFillBackground(False)
        # self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_52.setObjectName("frame_52")
        # self.gridLayout_43 = QtWidgets.QGridLayout(self.frame_52)
        # self.gridLayout_43.setObjectName("gridLayout_43")
        # self.pushButton_27 = QtWidgets.QPushButton(self.frame_52)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        # self.pushButton_27.setSizePolicy(sizePolicy)
        # self.pushButton_27.setObjectName("pushButton_27")
        # self.gridLayout_43.addWidget(self.pushButton_27, 1, 2, 1, 1)
        # self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_52)
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.lineEdit_14.setFont(font)
        # self.lineEdit_14.setObjectName("lineEdit_14")
        # self.gridLayout_43.addWidget(self.lineEdit_14, 0, 0, 1, 3)
        # self.radioButton_14 = QtWidgets.QRadioButton(self.frame_52)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(20)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.radioButton_14.sizePolicy().hasHeightForWidth())
        # self.radioButton_14.setSizePolicy(sizePolicy)
        # self.radioButton_14.setObjectName("radioButton_14")
        # self.gridLayout_43.addWidget(self.radioButton_14, 1, 0, 1, 1)
        # self.pushButton_28 = QtWidgets.QPushButton(self.frame_52)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(40)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        # self.pushButton_28.setSizePolicy(sizePolicy)
        # self.pushButton_28.setObjectName("pushButton_28")
        # self.gridLayout_43.addWidget(self.pushButton_28, 1, 1, 1, 1)
        # self.horizontalLayout_14.addWidget(self.frame_52)
        # self.frame_53 = QtWidgets.QFrame(self.frame_50)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(10)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        # self.frame_53.setSizePolicy(sizePolicy)
        # self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_53.setObjectName("frame_53")
        # self.gridLayout_44 = QtWidgets.QGridLayout(self.frame_53)
        # self.gridLayout_44.setObjectName("gridLayout_44")
        # self.label_14 = QtWidgets.QLabel(self.frame_53)
        # self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_14.setObjectName("label_14")
        # self.gridLayout_44.addWidget(self.label_14, 0, 0, 1, 1)
        # self.horizontalLayout_14.addWidget(self.frame_53)
        # self.verticalLayout.addWidget(self.frame_50)
        # spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # self.verticalLayout.addItem(spacerItem2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1169, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPlay = QtWidgets.QMenu(self.menubar)
        self.menuPlay.setObjectName("menuPlay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPlay_Selected = QtWidgets.QAction(MainWindow)
        self.actionPlay_Selected.setObjectName("actionPlay_Selected")
        self.actionPlay_All = QtWidgets.QAction(MainWindow)
        self.actionPlay_All.setObjectName("actionPlay_All")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuPlay.addAction(self.actionPlay_Selected)
        self.menuPlay.addAction(self.actionPlay_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlay.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPlay.setTitle(_translate("MainWindow", "Play"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPlay_Selected.setText(_translate("MainWindow", "Play Selected"))
        self.actionPlay_All.setText(_translate("MainWindow", "Play All"))

    def read_data(self, path):
        text_paths = path + "*.txt"
        self.text_paths = sorted(glob.glob(text_paths))

    def read_wavs(self, path):
        wav_paths = path + "*.wav"
        self.wav_paths = sorted(glob.glob(wav_paths))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
