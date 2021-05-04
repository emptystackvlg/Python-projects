# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 228)
        MainWindow.setStyleSheet("color : balck ;\n"
" background-color:rgb(188, 235, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 141, 81))
        self.pushButton_2.setStyleSheet("color : rgb(0, 0, 0);\n"
"background-color : rgb(255, 234, 0) ;\n"
"\n"
"font: 10pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect()
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 120, 141, 81))
        self.pushButton_3.setStyleSheet("color : rgb(0, 0, 0) ;\n"
"background-color : rgb(255, 0, 4) ;\n"
"\n"
"font: 10pt \"Times New Roman\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 19, 301, 61))
        font = QtGui.QFont()
        font.setFamily("GungsuhChe")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color :rgb(0, 0, 0)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def word2pdf (self) :
              print  ("Hello")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "ИЗОБРАЖЕНИЯ"))
        self.pushButton_3.setText(_translate("MainWindow", "ДОКУМЕНТ WORD"))
        self.label.setText(_translate("MainWindow", " ВЫБЕРИТЕ ТИП ФАЙЛОВ "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


