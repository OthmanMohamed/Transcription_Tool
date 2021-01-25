# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtCore import pyqtSignal


class editor_window(QtWidgets.QMainWindow):
    quit = pyqtSignal()
    def __init__(self, parent=None, file_name = ""):
        super(editor_window, self).__init__(parent)
        self.file_name = file_name
        self.saveButton = QtWidgets.QPushButton(None)

    def setupUi(self, text, file_name):
        self.file_name = file_name
        self.setObjectName("MainWindow")
        self.resize(685, 398)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 667, 336))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editorFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.editorFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.editorFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.editorFrame.setLineWidth(0)
        self.editorFrame.setObjectName("editorFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.editorFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.editorFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        # self.plainTextEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.editorFrame)
        self.bottomFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveFrame = QtWidgets.QFrame(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveFrame.sizePolicy().hasHeightForWidth())
        self.saveFrame.setSizePolicy(sizePolicy)
        self.saveFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveFrame.setObjectName("saveFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.saveFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.saveButton = QtWidgets.QPushButton(self.saveFrame)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_4.addWidget(self.saveButton, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.saveFrame)
        self.playerFrame = QtWidgets.QFrame(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerFrame.sizePolicy().hasHeightForWidth())
        self.playerFrame.setSizePolicy(sizePolicy)
        self.playerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playerFrame.setObjectName("playerFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.playerFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.playerFrame)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 3)
        self.playButton = QtWidgets.QToolButton(self.playerFrame)
        self.playButton.setIcon(QIcon('play.png'))
        self.playButton.setObjectName("playButton")
        self.gridLayout_2.addWidget(self.playButton, 1, 0, 1, 1)
        self.pauseButton = QtWidgets.QToolButton(self.playerFrame)
        self.pauseButton.setIcon(QIcon('pause.png'))
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout_2.addWidget(self.pauseButton, 1, 1, 1, 1)
        self.stopButton = QtWidgets.QToolButton(self.playerFrame)
        self.stopButton.setIcon(QIcon('stop.png'))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 1, 2, 1, 1)
        self.playerLabel = QtWidgets.QLabel(self.playerFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.playerLabel.setFont(font)
        self.playerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.playerLabel.setObjectName("playerLabel")
        self.gridLayout_2.addWidget(self.playerLabel, 2, 0, 1, 3)
        self.horizontalLayout.addWidget(self.playerFrame)
        self.cancelFrame = QtWidgets.QFrame(self.bottomFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelFrame.sizePolicy().hasHeightForWidth())
        self.cancelFrame.setSizePolicy(sizePolicy)
        self.cancelFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cancelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cancelFrame.setObjectName("cancelFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.cancelFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cancelButton = QtWidgets.QPushButton(self.cancelFrame)
        self.cancelButton.clicked.connect(self.close)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout_5.addWidget(self.cancelButton, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.cancelFrame)
        self.verticalLayout.addWidget(self.bottomFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(text)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, text):
        _translate = QtCore.QCoreApplication.translate
        print(self.parent)
        if self.file_name:
            self.setWindowTitle(_translate("MainWindow", self.file_name))
        else:
            self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.playButton.setText(_translate("MainWindow", ""))
        self.pauseButton.setText(_translate("MainWindow", ""))
        self.stopButton.setText(_translate("MainWindow", ""))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.plainTextEdit.setPlainText(text)

    def closeEvent(self, event):
        self.quit.emit()
        event.accept()
    #     close = QMessageBox()
    #     close.setText("You sure?")
    #     close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    #     close = close.exec()
    #
    #     if close == QMessageBox.Yes:
    #         self.quit.emit()
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = editor_window()
    ui.setupUi("sss")
    ui.show()
    sys.exit(app.exec_())
