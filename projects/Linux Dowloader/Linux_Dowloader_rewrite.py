from tkinter.font import names


def install_libs () : 
    from os import system
    system ("pip install easygui")
    system ("pip install win10toast_click")
    system ("pip install PyQt6")
    system ("pip install PySide6")
try :
    from PyQt6 import QtCore, QtGui, QtWidgets
    from urllib.request import urlretrieve as save 
    from win10toast_click import ToastNotifier as tf 
    from easygui import diropenbox
    from os import chdir
except : 
    install_libs ()
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
        self.DownloadButton.setText(_translate("MainWindow", "Скачать"))
        self.DownloadButton.clicked.connect (lambda : download (self.DistroBox.currentIndex()))
        self.label.setText(_translate("MainWindow", "LinuxDowloader"))



#def cbk(a,b,c):
    #per=100.0*a*b/c
    #if per>100:
    #    per=100
   # print (int (per))


def download (id):
    names = ("Linux Mint (Cinamon)" ,"Linux Mint (Mate)","Linux Mint (Xfce)" , "MX Linux (KDE)" , "MX Linux (Xfce)" ,
            "MX Linux (Fluxbox)","Manjaro (KDE)","Manjaro (Xfce)","Manjaro (GNOME)","KDE Neon","Ubuntu","Kubuntu","Lubuntu",
            "Xubuntu","Fedora","Deepin Linux","Zorin OS","Pop!_OS")
    links = ("http://mirrors.powernet.com.ru/linuxmint/stable/20.2/linuxmint-20.2-cinnamon-64bit.iso","https://mirror.yandex.ru/linuxmint/stable/20.2/linuxmint-20.2-mate-64bit.iso",
            "http://mirrors.powernet.com.ru/linuxmint/stable/20.2/linuxmint-20.2-xfce-64bit.iso","https://sourceforge.net/projects/mx-linux/files/Final/KDE/MX-21_KDE_x64.iso/download",
            "https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-21_x64.iso/download","https://sourceforge.net/projects/mx-linux/files/Final/Fluxbox/MX-21_fluxbox_x64.iso/download",
            "https://download.manjaro.org/kde/21.2.1/manjaro-kde-21.2.1-220103-linux515.iso","https://download.manjaro.org/xfce/21.2.1/manjaro-xfce-21.2.1-220103-linux515.iso",
            "https://download.manjaro.org/gnome/21.2.1/manjaro-gnome-21.2.1-220103-linux515.iso","https://files.kde.org/neon/images/user/20211230-0945/neon-user-20211230-0945.iso"
            "https://releases.ubuntu.com/20.04.3/ubuntu-20.04.3-desktop-amd64.iso","https://cdimage.ubuntu.com/kubuntu/releases/21.10/release/kubuntu-21.10-desktop-amd64.iso",
            "https://cdimage.ubuntu.com/lubuntu/releases/21.10/release/lubuntu-21.10-desktop-amd64.iso","https://mirror.yandex.ru/ubuntu-cdimage/xubuntu/releases/20.04/release/xubuntu-20.04.3-desktop-amd64.iso",
            "https://download.fedoraproject.org/pub/fedora/linux/releases/35/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-35-1.2.iso","https://sourceforge.net/projects/deepin/files/20.2.2/deepin-desktop-community-20.2.2-amd64.iso",
            "https://mirrors.edge.kernel.org/zorinos-isos/16/Zorin-OS-16-Core-64-bit-r4.iso","https://pop-iso.sfo2.cdn.digitaloceanspaces.com/21.10/amd64/intel/3/pop-os_21.10_amd64_intel_3.iso")
    try: 
        MainWindow.hide () 
        dir = diropenbox ("Выберите место для сохранения")   
        chdir (dir)
        tf().show_toast("Linux Downloader" , "Скачивание " + names[id]+ " началось", duration = 10, threaded = True)
        save (links[id], names[id]+".iso")#,cbk)      
        tf().show_toast ("Linux Downloader" , "Скачивание " + names[id] + " завершено", duration = 10, threaded = True)
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