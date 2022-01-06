from PyQt6 import QtCore, QtGui, QtWidgets
from urllib.request import urlretrieve as save 
from win10toast_click import ToastNotifier as tf 
from easygui import diropenbox
from os import chdir


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 311)
        MainWindow.setMaximumSize (352, 311)
        MainWindow.setMinimumSize (352, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DistroBox = QtWidgets.QComboBox(self.centralwidget)
        self.DistroBox.setGeometry(QtCore.QRect(60, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DistroBox.setFont(font)
        self.DistroBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.DistroBox.setEditable(False)
        self.DistroBox.setIconSize(QtCore.QSize(32, 32))
        self.DistroBox.setObjectName("DistroBox")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DistroBox.addItem("")
        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(60, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        self.DownloadButton.setFont(font)
        self.DownloadButton.setObjectName("DownloadButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linux Downloader"))
        self.DistroBox.setItemText(0, _translate("MainWindow", "Linux Mint (Cinamon)"))
        self.DistroBox.setItemText(1, _translate("MainWindow", "Linux Mint (Mate)"))
        self.DistroBox.setItemText(2, _translate("MainWindow", "Linux Mint (Xfce)"))
        self.DistroBox.setItemText(3, _translate("MainWindow", "MX Linux (KDE)"))
        self.DistroBox.setItemText(4, _translate("MainWindow", "MX Linux (Xfce)"))
        self.DistroBox.setItemText(5, _translate("MainWindow", "MX Linux (Fluxbox)"))
        self.DistroBox.setItemText(6, _translate("MainWindow", "Manjaro (KDE)"))
        self.DistroBox.setItemText(7, _translate("MainWindow", "Manjaro (Xfce)"))
        self.DistroBox.setItemText(8, _translate("MainWindow", "Manjaro (GNOME)"))
        self.DistroBox.setItemText(9, _translate("MainWindow", "KDE Neon"))
        self.DistroBox.setItemText(10, _translate("MainWindow", "Ubuntu"))
        self.DistroBox.setItemText(11, _translate("MainWindow", "Kubuntu"))
        self.DistroBox.setItemText(12, _translate("MainWindow", "Lubuntu"))
        self.DistroBox.setItemText(13, _translate("MainWindow", "Xubuntu"))
        self.DistroBox.setItemText(14, _translate("MainWindow", "Fedora"))
        self.DistroBox.setItemText(15, _translate("MainWindow", "Deepin Linux"))
        self.DistroBox.setItemText(16, _translate("MainWindow", "Zorin OS"))
        self.DistroBox.setItemText(17, _translate("MainWindow", "Pop!_OS"))
        self.DistroBox.setItemText(18, _translate("MainWindow", "Clear Linux"))
        self.DistroBox.setItemText(19, _translate("MainWindow", "Garuda Linux"))
        self.DownloadButton.setText(_translate("MainWindow", "Скачать"))
        self.DownloadButton.clicked.connect (lambda : download (self.DistroBox.currentIndex()))
        self.label.setText(_translate("MainWindow", "DistroDowloader"))



def download (id):
    
    try : 
        MainWindow.hide () 
        if id == 0 :
            dir = diropenbox ("Выберите место для сохранения")
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Cinamon) началось", duration = 10, threaded = True)
            save ("http://mirrors.powernet.com.ru/linuxmint/stable/20.2/linuxmint-20.2-cinnamon-64bit.iso", "Linux Mint (Cinamon).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Cinamon) завершено", duration = 10, threaded = True)       
        elif id == 1:
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Mate) началось", duration = 10, threaded = True)
            save ("https://mirror.yandex.ru/linuxmint/stable/20.2/linuxmint-20.2-mate-64bit.iso", "Linux Mint (Mate).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Mate) завершено", duration = 10, threaded = True)  
        elif id == 2 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Xfce) началось", duration = 10, threaded = True)
            save ("http://mirrors.powernet.com.ru/linuxmint/stable/20.2/linuxmint-20.2-xfce-64bit.iso", "Linux Mint (Xfce).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Linux Mint (Xfce) завершено", duration = 10, threaded = True)    
        elif id == 3 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (KDE) началось", duration = 10, threaded = True)
            save ("https://sourceforge.net/projects/mx-linux/files/Final/KDE/MX-21_KDE_x64.iso/download", "MX Linux (KDE).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (KDE) завершено", duration = 10, threaded = True) 
        elif id == 4 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (Xfce) началось", duration = 10, threaded = True)
            save ("https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-21_x64.iso/download", "MX Linux (Xfce).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (Xfce) завершено", duration = 10, threaded = True) 
        elif id == 5 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (Fluxbox) началось", duration = 10, threaded = True)
            save ("https://sourceforge.net/projects/mx-linux/files/Final/Fluxbox/MX-21_fluxbox_x64.iso/download", "MX Linux (Fluxbox).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание MX Linux (Fluxbox) завершено", duration = 10, threaded = True) 
        elif id == 6 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (KDE) началось", duration = 10, threaded = True)
            save ("https://download.manjaro.org/kde/21.2.1/manjaro-kde-21.2.1-220103-linux515.iso", "Manjaro (KDE).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (KDE) завершено", duration = 10, threaded = True) 
        elif id == 7 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (Xfce) началось", duration = 10, threaded = True)
            save ("https://download.manjaro.org/xfce/21.2.1/manjaro-xfce-21.2.1-220103-linux515.iso", "Manjaro (Xfce).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (Xfce) завершено", duration = 10, threaded = True) 
        elif id == 8 : 
            dir = diropenbox ("Выберите место для сохранения")   
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (GNOME) началось", duration = 10, threaded = True)
            save ("https://download.manjaro.org/gnome/21.2.1/manjaro-gnome-21.2.1-220103-linux515.iso", "Manjaro (GNOME).iso")      
            tf().show_toast("Linux Downloader" , "Скачивание Manjaro (GNOME) завершено", duration = 10, threaded = True) 
        elif id == 9 : 
            dir = diropenbox ("Выберите место для сохранения")
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание KDE Neon началось", duration = 10 , threaded = True)
            save ("https://files.kde.org/neon/images/user/20211230-0945/neon-user-20211230-0945.iso", "KDE Neon.iso")
            tf().show_toast("Linux Downloader" , "Скачивание KDE Neon закончилось", duration = 10 , threaded = True)
        elif id == 10 :
            dir = diropenbox ("Выберите место для сохранения")
            chdir (dir)
            tf().show_toast("Linux Downloader" , "Скачивание Ubuntu началось" , duration = 10 , threaded = True)
            save ("https://releases.ubuntu.com/20.04.3/ubuntu-20.04.3-desktop-amd64.iso","Ubuntu.iso")
            tf().show_toast("Linux Downloader" , "Скачивание Ubuntu закончилось" , duration = 10 , threaded = True)
    except: 
        
        tf().show_toast("Linux Downloader" , "Что-то пошло не так , попробуйте еще раз", duration = 10, threaded = True)
        MainWindow.show ()
        print ("Error")
    MainWindow.show ()



    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())