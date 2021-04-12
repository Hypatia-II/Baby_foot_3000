# -*- coding: utf-8 -*-

__author__ = "Inès BENITO"

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principale_ihm(object):
    def setupUi(self, Principale_ihm):
        Principale_ihm.setObjectName("Principale_ihm")
        Principale_ihm.resize(930, 877)
        Principale_ihm.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/players.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principale_ihm.setWindowIcon(icon)
        self.Conteneur = QtWidgets.QWidget(Principale_ihm)
        self.Conteneur.setObjectName("Conteneur")
        self.widget = QtWidgets.QWidget(self.Conteneur)
        self.widget.setGeometry(QtCore.QRect(0, 0, 921, 851))
        self.widget.setStyleSheet("background-image:url(:/Credits/credits.png);\n"
                                  "background-repeat: no repeat;\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(600, 390, 261, 91))
        self.widget_2.setStyleSheet(
            "background-image: url(:/Credits/thumbnail_logo-ENSTA-Bretagne-sans-bords-RVB.jpg);\n"
            "background-repeat: no repeat;\n"
            "")
        self.widget_2.setObjectName("widget_2")
        self.QuitButton = QtWidgets.QPushButton(self.Conteneur)
        self.QuitButton.setGeometry(QtCore.QRect(780, 770, 111, 41))
        self.QuitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.QuitButton.setStyleSheet("font: 25 12pt \"Bahnschrift Light\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/exitt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuitButton.setIcon(icon1)
        self.QuitButton.setObjectName("QuitButton")
        Principale_ihm.setCentralWidget(self.Conteneur)
        self.menubar = QtWidgets.QMenuBar(Principale_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Principale_ihm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principale_ihm)
        self.statusbar.setObjectName("statusbar")
        Principale_ihm.setStatusBar(self.statusbar)
        self.actionStart_new_game = QtWidgets.QAction(Principale_ihm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/table-football.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_new_game.setIcon(icon2)
        self.actionStart_new_game.setObjectName("actionStart_new_game")
        self.actionStats = QtWidgets.QAction(Principale_ihm)
        self.actionStats.setObjectName("actionStats")
        self.actionHelp = QtWidgets.QAction(Principale_ihm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionHelp.setObjectName("actionHelp")
        self.actionQuit = QtWidgets.QAction(Principale_ihm)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName("actionQuit")
        self.actionStatistics = QtWidgets.QAction(Principale_ihm)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/bars-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatistics.setIcon(icon4)
        self.actionStatistics.setObjectName("actionStatistics")
        self.actionSettings = QtWidgets.QAction(Principale_ihm)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/settings-work-tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionStart_new_game)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionStatistics)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Principale_ihm)
        self.actionQuit.triggered.connect(Principale_ihm.close)
        self.QuitButton.clicked.connect(Principale_ihm.close)
        QtCore.QMetaObject.connectSlotsByName(Principale_ihm)

    def retranslateUi(self, Principale_ihm):
        _translate = QtCore.QCoreApplication.translate
        Principale_ihm.setWindowTitle(_translate("Principale_ihm", "Playground"))
        self.QuitButton.setText(_translate("Principale_ihm", "Quit"))
        self.QuitButton.setShortcut(_translate("Principale_ihm", "Esc"))
        self.menuFile.setTitle(_translate("Principale_ihm", "File"))
        self.actionStart_new_game.setText(_translate("Principale_ihm", "Start new game"))
        self.actionStart_new_game.setShortcut(_translate("Principale_ihm", "Return"))
        self.actionStats.setText(_translate("Principale_ihm", "Statistics"))
        self.actionStats.setShortcut(_translate("Principale_ihm", "S"))
        self.actionHelp.setText(_translate("Principale_ihm", "Help"))
        self.actionHelp.setShortcut(_translate("Principale_ihm", "H"))
        self.actionQuit.setText(_translate("Principale_ihm", "Quit"))
        self.actionQuit.setShortcut(_translate("Principale_ihm", "Esc"))
        self.actionStatistics.setText(_translate("Principale_ihm", "Statistics"))
        self.actionStatistics.setShortcut(_translate("Principale_ihm", "S"))
        self.actionSettings.setText(_translate("Principale_ihm", "Settings"))


import images_rc
