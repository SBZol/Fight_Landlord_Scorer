# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Project\Fight_Landlord_Scorer\fiight_landlor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from game import Game

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 391, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nameButton_p2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nameButton_p2.setObjectName("nameButton_p2")
        self.gridLayout.addWidget(self.nameButton_p2, 2, 1, 1, 1)
        self.nameButton_p4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nameButton_p4.setObjectName("nameButton_p4")
        self.gridLayout.addWidget(self.nameButton_p4, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.nameButton_p1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nameButton_p1.setObjectName("nameButton_p1")
        self.gridLayout.addWidget(self.nameButton_p1, 1, 1, 1, 1)
        self.nameButton_p3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nameButton_p3.setObjectName("nameButton_p3")
        self.gridLayout.addWidget(self.nameButton_p3, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.nameButton_p5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nameButton_p5.setObjectName("nameButton_p5")
        self.gridLayout.addWidget(self.nameButton_p5, 5, 1, 1, 1)
        self.scoreLabel_p1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scoreLabel_p1.setObjectName("scoreLabel_p1")
        self.gridLayout.addWidget(self.scoreLabel_p1, 1, 2, 1, 1)
        self.scoreLabel_p2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scoreLabel_p2.setObjectName("scoreLabel_p2")
        self.gridLayout.addWidget(self.scoreLabel_p2, 2, 2, 1, 1)
        self.scoreLabel_p3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scoreLabel_p3.setObjectName("scoreLabel_p3")
        self.gridLayout.addWidget(self.scoreLabel_p3, 3, 2, 1, 1)
        self.scoreLabel_p4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scoreLabel_p4.setObjectName("scoreLabel_p4")
        self.gridLayout.addWidget(self.scoreLabel_p4, 4, 2, 1, 1)
        self.scoreLabel_p5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.scoreLabel_p5.setObjectName("scoreLabel_p5")
        self.gridLayout.addWidget(self.scoreLabel_p5, 5, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_p5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_p5.setObjectName("label_p5")
        self.gridLayout_2.addWidget(self.label_p5, 0, 8, 1, 1)
        self.nameEdit_p3 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.nameEdit_p3.setObjectName("nameEdit_p3")
        self.gridLayout_2.addWidget(self.nameEdit_p3, 0, 5, 1, 1)
        self.nameEdit_p1 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.nameEdit_p1.setObjectName("nameEdit_p1")
        self.gridLayout_2.addWidget(self.nameEdit_p1, 0, 1, 1, 1)
        self.nameEdit_p2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.nameEdit_p2.setObjectName("nameEdit_p2")
        self.gridLayout_2.addWidget(self.nameEdit_p2, 0, 3, 1, 1)
        self.label_p3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_p3.setObjectName("label_p3")
        self.gridLayout_2.addWidget(self.label_p3, 0, 4, 1, 1)
        self.nameEdit_p5 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.nameEdit_p5.setObjectName("nameEdit_p5")
        self.gridLayout_2.addWidget(self.nameEdit_p5, 0, 9, 1, 1)
        self.label_p1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_p1.setObjectName("label_p1")
        self.gridLayout_2.addWidget(self.label_p1, 0, 0, 1, 1)
        self.label_p2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_p2.setObjectName("label_p2")
        self.gridLayout_2.addWidget(self.label_p2, 0, 2, 1, 1)
        self.label_p4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_p4.setObjectName("label_p4")
        self.gridLayout_2.addWidget(self.label_p4, 0, 6, 1, 1)
        self.nameEdit_p4 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.nameEdit_p4.setObjectName("nameEdit_p4")
        self.gridLayout_2.addWidget(self.nameEdit_p4, 0, 7, 1, 1)
        self.addPlayerButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addPlayerButton.setObjectName("addPlayerButton")
        self.gridLayout_2.addWidget(self.addPlayerButton, 0, 10, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(460, 90, 281, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.boomCount = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.boomCount.setObjectName("boomCount")
        self.gridLayout_4.addWidget(self.boomCount, 1, 1, 1, 1)
        self.boomLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.boomLabel.setObjectName("boomLabel")
        self.gridLayout_4.addWidget(self.boomLabel, 1, 0, 1, 1)
        self.landlordsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.landlordsLabel.setText("")
        self.landlordsLabel.setObjectName("landlordsLabel")
        self.gridLayout_4.addWidget(self.landlordsLabel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.landlordWinButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.landlordWinButton.setObjectName("landlordWinButton")
        self.gridLayout_4.addWidget(self.landlordWinButton, 2, 0, 1, 1)
        self.farmerWinButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.farmerWinButton.setObjectName("farmerWinButton")
        self.gridLayout_4.addWidget(self.farmerWinButton, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.nameButtons = [self.nameButton_p1, self.nameButton_p2, self.nameButton_p3, self.nameButton_p4, self.nameButton_p5]
        self.scoreLabels = [self.scoreLabel_p1, self.scoreLabel_p2, self.scoreLabel_p3, self.scoreLabel_p4, self.scoreLabel_p5]
        self.h_buttons = []

        self.addAction()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameButton_p2.setText(_translate("MainWindow", "Player2"))
        self.nameButton_p4.setText(_translate("MainWindow", "Player4"))
        self.label_2.setText(_translate("MainWindow", "Score"))
        self.nameButton_p1.setText(_translate("MainWindow", "Player1"))
        self.nameButton_p3.setText(_translate("MainWindow", "Player3"))
        self.label.setText(_translate("MainWindow", "Player"))
        self.nameButton_p5.setText(_translate("MainWindow", "Player5"))
        self.scoreLabel_p1.setText(_translate("MainWindow", "0"))
        self.scoreLabel_p2.setText(_translate("MainWindow", "0"))
        self.scoreLabel_p3.setText(_translate("MainWindow", "0"))
        self.scoreLabel_p4.setText(_translate("MainWindow", "0"))
        self.scoreLabel_p5.setText(_translate("MainWindow", "0"))
        self.label_p5.setText(_translate("MainWindow", "Player5"))
        self.nameEdit_p1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_p3.setText(_translate("MainWindow", "Player3"))
        self.label_p1.setText(_translate("MainWindow", "Player1"))
        self.label_p2.setText(_translate("MainWindow", "Player2"))
        self.label_p4.setText(_translate("MainWindow", "Player4"))
        self.addPlayerButton.setText(_translate("MainWindow", "AddPlayer"))
        self.boomLabel.setText(_translate("MainWindow", "     BOOM!"))
        self.label_3.setText(_translate("MainWindow", "   Landlord"))
        self.landlordsLabel.setText('！！！！！！！')
        self.landlordWinButton.setText(_translate("MainWindow", "landlord win!"))
        self.farmerWinButton.setText(_translate("MainWindow", "farmer win!"))
        

    def addAction(self):
        self.addPlayerButton.clicked.connect(self.addPlayerButton_clicked)
        self.nameButton_p1.clicked.connect(lambda: self.nameButton_clicked(self.nameButton_p1))
        self.nameButton_p2.clicked.connect(lambda: self.nameButton_clicked(self.nameButton_p2))
        self.nameButton_p3.clicked.connect(lambda: self.nameButton_clicked(self.nameButton_p3))
        self.nameButton_p4.clicked.connect(lambda: self.nameButton_clicked(self.nameButton_p4))
        self.nameButton_p5.clicked.connect(lambda: self.nameButton_clicked(self.nameButton_p5))
        self.landlordWinButton.clicked.connect(lambda: self.winButton_clicked(self.landlordWinButton))
        self.farmerWinButton.clicked.connect(lambda: self.winButton_clicked(self.farmerWinButton))

    # button actions
    def addPlayerButton_clicked(self):
        name_p1 = self.nameEdit_p1.toPlainText()
        name_p2 = self.nameEdit_p2.toPlainText()
        name_p3 = self.nameEdit_p3.toPlainText()
        name_p4 = self.nameEdit_p4.toPlainText()
        name_p5 = self.nameEdit_p5.toPlainText()
        player_names = [name_p1, name_p2, name_p3, name_p4, name_p5]

        self.game = Game(player_names)
        self.setPlayerName()
        self.updateScoreLabel()

    def nameButton_clicked(self, sender):
        self.game.setLandlord(sender.text())
        self.setLandlordLabel()

    
    def winButton_clicked(self, sender):
        
        self.game.booms = int(self.boomCount.text())
        print(self.boomCount.text())
        if sender.text() == 'landlord win!':
            self.game.landlord_win()
        elif sender.text() == 'farmer win!':
            self.game.farmer_win()

        self.updateScoreLabel()

    

        

    # update UI

    def setPlayerName(self):
        self.nameButton_p1.setText(self.game.player1.name)
        self.nameButton_p2.setText(self.game.player2.name)
        self.nameButton_p3.setText(self.game.player3.name)
        self.nameButton_p4.setText(self.game.player4.name)
        self.nameButton_p5.setText(self.game.player5.name)
        
    def setLandlordLabel(self):
        landlord_names = ''
        for name in self.game.landlords:
            landlord_names = landlord_names + ' ' + name
        self.landlordsLabel.setText(landlord_names)

    def updateScoreLabel(self):
        for i, sender in enumerate(self.scoreLabels):
            sender.setText(str(self.game.players[i].score))

    def restore_default(self):
        self.landlordsLabel.setText('！！！！！！！')
        self.boomCount.setdefault()