# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MAIN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 331)
        MainWindow.setMinimumSize(QSize(268, 167))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 278, 631, 20))
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)
        self.open_file_dir_btn = QPushButton(self.centralwidget)
        self.open_file_dir_btn.setObjectName(u"open_file_dir_btn")
        self.open_file_dir_btn.setGeometry(QRect(674, 54, 75, 23))
        self.f_log_browser = QTextBrowser(self.centralwidget)
        self.f_log_browser.setObjectName(u"f_log_browser")
        self.f_log_browser.setGeometry(QRect(19, 83, 731, 181))
        self.transed_file_dir = QLineEdit(self.centralwidget)
        self.transed_file_dir.setObjectName(u"transed_file_dir")
        self.transed_file_dir.setGeometry(QRect(20, 55, 551, 20))
        self.transed_file_dir.setReadOnly(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 27, 541, 21))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.select_file_dir_btn = QPushButton(self.centralwidget)
        self.select_file_dir_btn.setObjectName(u"select_file_dir_btn")
        self.select_file_dir_btn.setGeometry(QRect(588, 53, 75, 23))
        self.run_translate_btn = QPushButton(self.centralwidget)
        self.run_translate_btn.setObjectName(u"run_translate_btn")
        self.run_translate_btn.setGeometry(QRect(674, 275, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Manga-Translator", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.open_file_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ubc88\uc5ed\ud560 \ud30c\uc77c\uc774 \uc788\ub294 \ud3f4\ub354 \uc704\uce58: <span style=\" color:#ff0000;\">\ud30c\uc77c \ubc88\uc5ed \uc804\uc5d0 \ubc88\uc5ed\ud560 \uc0ac\uc9c4\ub4e4\uc774 \uc788\ub294 \ud3f4\ub354\ub97c \uc120\ud0dd\ud558\uc138\uc694! </span></p></body></html>", None))
        self.select_file_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.run_translate_btn.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed\ud558\uae30", None))
    # retranslateUi

