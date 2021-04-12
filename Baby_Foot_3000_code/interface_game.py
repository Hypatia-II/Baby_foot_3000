# -*- coding: utf-8 -*-

__author__ = "Inès BENITO & Sacha HIRSCH"

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principale_ihm(object):
    def setupUi(self, Principale_ihm):
        Principale_ihm.setObjectName("Principale_ihm")
        Principale_ihm.resize(1204, 949)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/players.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principale_ihm.setWindowIcon(icon)
        Principale_ihm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Conteneur = QtWidgets.QWidget(Principale_ihm)
        self.Conteneur.setObjectName("Conteneur")
        self.lcdNumber = QtWidgets.QLCDNumber(self.Conteneur)
        self.lcdNumber.setGeometry(QtCore.QRect(690, 690, 111, 106))
        self.lcdNumber.setMinimumSize(QtCore.QSize(64, 106))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 740, 91, 100))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_4.setGeometry(QtCore.QRect(980, 690, 81, 91))
        self.textBrowser_4.setStyleSheet("")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_5.setGeometry(QtCore.QRect(980, 780, 81, 101))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_6.setGeometry(QtCore.QRect(100, 780, 91, 101))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_7.setGeometry(QtCore.QRect(100, 680, 91, 101))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_8.setGeometry(QtCore.QRect(890, 730, 91, 91))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.Conteneur)
        self.lcdNumber_3.setGeometry(QtCore.QRect(370, 690, 111, 106))
        self.lcdNumber_3.setMinimumSize(QtCore.QSize(64, 106))
        self.lcdNumber_3.setDigitCount(2)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.display = QtWidgets.QWidget(self.Conteneur)
        self.display.setGeometry(QtCore.QRect(80, 20, 1031, 631))
        self.display.setStyleSheet("")
        self.display.setObjectName("display")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.display)
        self.lcdNumber_2.setGeometry(QtCore.QRect(360, 140, 331, 341))
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(64, 106))
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_9.setGeometry(QtCore.QRect(190, 740, 91, 100))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_10.setGeometry(QtCore.QRect(1060, 730, 91, 91))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.Conteneur)
        self.textBrowser_11.setGeometry(QtCore.QRect(520, 690, 131, 111))
        self.textBrowser_11.setStyleSheet("")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.display.raise_()
        self.lcdNumber.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_5.raise_()
        self.textBrowser_6.raise_()
        self.textBrowser_7.raise_()
        self.textBrowser_8.raise_()
        self.lcdNumber_3.raise_()
        self.textBrowser_9.raise_()
        self.textBrowser_10.raise_()
        self.textBrowser_11.raise_()
        Principale_ihm.setCentralWidget(self.Conteneur)
        self.menubar = QtWidgets.QMenuBar(Principale_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1204, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Principale_ihm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principale_ihm)
        self.statusbar.setObjectName("statusbar")
        Principale_ihm.setStatusBar(self.statusbar)
        self.actionStart_new_game = QtWidgets.QAction(Principale_ihm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/table-football.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_new_game.setIcon(icon)
        self.actionStart_new_game.setObjectName("actionStart_new_game")
        self.actionHelp = QtWidgets.QAction(Principale_ihm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Photos/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon1)
        self.actionHelp.setObjectName("actionHelp")
        self.actionQuit = QtWidgets.QAction(Principale_ihm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Photos/exitt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionStatistics = QtWidgets.QAction(Principale_ihm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/bars-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatistics.setIcon(icon3)
        self.actionStatistics.setObjectName("actionStatistics")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/settings-work-tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings = QtWidgets.QAction(Principale_ihm)
        self.actionSettings.setIcon(icon4)
        self.actionSettings.setObjectName("actionSettings")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/copyright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCredits = QtWidgets.QAction(Principale_ihm)
        self.actionCredits.setIcon(icon5)
        self.actionCredits.setObjectName("actionCredits")
        self.menuFile.addAction(self.actionStart_new_game)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionStatistics)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCredits)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Principale_ihm)
        self.actionQuit.triggered.connect(Principale_ihm.close)
        QtCore.QMetaObject.connectSlotsByName(Principale_ihm)

    def retranslateUi(self, Principale_ihm):
        _translate = QtCore.QCoreApplication.translate
        Principale_ihm.setWindowTitle(_translate("Principale_ihm", "Playground"))
        self.textBrowser_3.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">KICK</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Game/space.png\" /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">UP</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Game/arrow-up2.png\" /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">DOWN</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Game/arrow-pointing-down1.png\" /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">DOWN</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt; font-weight:600;\">S</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">UP</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt; font-weight:600;\">Z</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">KICK</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Game/keyboard-key-enter1.png\" /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Principale_ihm",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">CATCH</span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt; font-weight:600;\">A</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("Principale_ihm",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">CATCH</span></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Game/shift-keyboard-key.png\" /></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("Principale_ihm",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">RESET BALL</span></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">R</span></p></body></html>"))
        self.menuFile.setTitle(_translate("Principale_ihm", "File"))
        self.actionStart_new_game.setText(_translate("Principale_ihm", "Start new game"))
        self.actionStart_new_game.setShortcut(_translate("Principale_ihm", "Ctrl+G"))
        self.actionHelp.setText(_translate("Principale_ihm", "Help"))
        self.actionHelp.setShortcut(_translate("Principale_ihm", "Ctrl+H"))
        self.actionQuit.setText(_translate("Principale_ihm", "Quit"))
        self.actionQuit.setShortcut(_translate("Principale_ihm", "Esc"))
        self.actionStatistics.setText(_translate("Principale_ihm", "Statistics"))
        self.actionStatistics.setShortcut(_translate("Principale_ihm", "Ctrl+S"))
        self.actionSettings.setText(_translate("Principale_ihm", "Settings"))
        self.actionCredits.setText(_translate("Principale_ihm", "Credits"))


import images_rc
