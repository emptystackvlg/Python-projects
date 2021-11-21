from os import chdir , remove , system
from urllib.request import urlretrieve as download
def install_libs () :
        system ("pip install easygui")
        system ("pip install win10toast")
        system ("pip install PyQt6")
        system ("pip install PySide6")
        system ("cls")
        print ("Библиотеки установлены, перезапустите программу")
        system ("pause")
        exit (0)
try :
        from easygui import diropenbox , ccbox
        from win10toast import ToastNotifier as tf
        import subprocess
        from PyQt6 import QtCore, QtGui, QtWidgets
        from easygui.boxes.choice_box import make_list_or_none
except :
        install_libs ()
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PyInstaller")
        MainWindow.resize(323, 279) 
        MainWindow.setMaximumSize (323, 279)
        MainWindow.setMinimumSize (323, 279) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(10, 160, 81, 71))
        self.Download.setObjectName("Download")
        self.Download.clicked.connect (lambda : get_apps(main_tuple))
        self.Install = QtWidgets.QPushButton(self.centralwidget)
        self.Install.setGeometry(QtCore.QRect(120, 160, 81, 71))
        self.Install.setObjectName("Install")
        self.Install.clicked.connect (lambda : install_apps (len (main_tuple)))
        self.Remove = QtWidgets.QPushButton(self.centralwidget)
        self.Remove.setGeometry(QtCore.QRect(230, 160, 81, 71))
        self.Remove.setObjectName("Remove")
        self.Remove.clicked.connect (lambda : clean_dir (len (main_tuple)))
        self.Installer = QtWidgets.QLabel(self.centralwidget)
        self.Installer.setGeometry(QtCore.QRect(100, 30, 121, 51))
        self.Installer.setObjectName("Installer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyInstaller"))
        self.Download.setText(_translate("MainWindow", "Скачать\n"
"программы"))
        self.Install.setText(_translate("MainWindow", "Установить\n"
"программы "))
        self.Remove.setText(_translate("MainWindow", "Удалить \n"
"установщики"))
        self.Installer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">INSTALLER</span></p></body></html>"))


main_tuple = (  'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user' , 'https://sourceforge.net/projects/qbittorrent/files/qbittorrent-win32/qbittorrent-4.3.6/qbittorrent_4.3.6_x64_setup.exe/download',            
                'https://download.scdn.co/SpotifySetup.exe','https://telegram.org/dl/desktop/win64','https://storage.googleapis.com/media.amperka.com/arduino-ide/arduino-latest-windows.exe',
                'http://www.hibitsoft.ir/HiBitUninstaller/HiBitUninstaller-setup-2.6.15.exe','https://zoom.us/client/5.8.4.1736/ZoomInstaller.exe?archType=x64', 
                'https://github.com/git-for-windows/git/releases/download/v2.32.0.windows.2/Git-2.32.0.2-64-bit.exe','https://central.github.com/deployments/desktop/desktop/latest/win32',
                'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245029_d3c52aa6bfa54d3ca74e617f18309292','https://files3.codecguide.com/K-Lite_Codec_Pack_1635_Full.exe',
                'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.1.2/npp.8.1.2.Installer.exe','https://cdn-fastly.obsproject.com/downloads/OBS-Studio-27.0.1-Full-Installer-x64.exe',
                'https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=ru','https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe',
                'https://www.7-zip.org/a/7z1900-x64.exe' , 'https://aka.ms/vs/17/release/vs_community.exe' , 'http://qttabbar.wdfiles.com/local--files/qttabbar1/QTTabBar_1043.zip' ,
                'https://go.microsoft.com/fwlink/p/?LinkID=869426&clcid=0x419&culture=ru-ru&country=RU&lm=deeplink&lmsrc=groupChatMarketingPageWeb&cmpid=directDownloadWin64',
                'https://sourceforge.net/projects/equalizerapo/files/latest/download',
                
                
                )

def get_apps (links) : 
    try :
        MainWindow.hide ()
        dest = diropenbox (title="Выберите папку для сохранения")
        chdir (dest)
        i = int (0)
        count = int (0)
        print ("Скачивание началось" + "\n")
        for i in range (len(links)) : 
                name = str(count) + ".exe"
                print ("Скачиваю файл номер " + str (count) + "\n")
                tf().show_toast("PyInstaller", "Скачиваю файл номер " + str (count) + "\n" ,duration=5 , threaded=True)
                download (links [i] , name)
                count += 1
                
        tf().show_toast("PyInstaller", "Скачивание завершено" ,duration=5 , threaded=True)
        MainWindow.show()
    except : 
            MainWindow.show ()    

def install_apps (lenght):
        try :
                MainWindow.hide ()
                number = int (0)
                path = diropenbox(title = 'Выберите папку')
                chdir (path)
                for number in range (lenght):
                        name = str(number) + ".exe"
                        subprocess.call(name, shell=True)
                        msg = "Вы хотите продолжить установку ?"
                        title = "Подтверждение"
                        if ccbox(msg, title):     
                                pass  
                        else: 
                                break
                        number += 1
                tf().show_toast("PyInstaller", "Установка завершена" ,duration=5 , threaded=True)
                MainWindow.show ()
        except :
                MainWindow.show ()

def clean_dir(length):
    try :
        MainWindow.hide()
        file_number = int (0)
        directory = diropenbox(title="Выберите папку")
        chdir (directory)
        for file_number in range (length):
                remove ( str(file_number) + ".exe")
                print ("Файл номер " + str (file_number) + " успешно удален" + "\n")
        tf().show_toast("PyInstaller", "Удаление завершено" ,duration=5 , threaded=True)
        MainWindow.show ()
    except : 
            MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
 
    MainWindow.show()
    sys.exit(app.exec())
