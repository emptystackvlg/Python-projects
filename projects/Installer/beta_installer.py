from urllib.request import urlretrieve as download
from easygui import diropenbox , msgbox
from os import chdir , system , remove
from time import sleep 
import subprocess

main_tuple = (  'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user' , 'https://sourceforge.net/projects/qbittorrent/files/qbittorrent-win32/qbittorrent-4.3.6/qbittorrent_4.3.6_x64_setup.exe/download',            
                'https://download.scdn.co/SpotifySetup.exe','https://telegram.org/dl/desktop/win64','https://storage.googleapis.com/media.amperka.com/arduino-ide/arduino-latest-windows.exe',
                'http://www.hibitsoft.ir/HiBitUninstaller/HiBitUninstaller-setup-2.6.15.exe',
                'https://github.com/git-for-windows/git/releases/download/v2.32.0.windows.2/Git-2.32.0.2-64-bit.exe','https://central.github.com/deployments/desktop/desktop/latest/win32',
                'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245029_d3c52aa6bfa54d3ca74e617f18309292','https://files3.codecguide.com/K-Lite_Codec_Pack_1635_Full.exe',
                'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.1.2/npp.8.1.2.Installer.exe','https://cdn-fastly.obsproject.com/downloads/OBS-Studio-27.0.1-Full-Installer-x64.exe',
                'https://www.tracker-software.com/product/pdf-xchange-viewer/download?fileid=446','https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe',
                'https://download.aida64.com/aida64extreme633.exe'
                )

def get_apps (links) : 
    dest = diropenbox (title="Выберите место для сохранения")
    chdir (dest)
    i = int (0)
    count = int (0)
    print ("Скачивание началось" + "\n")
    for i in range (len(links)) : 
        name = str(count) + ".exe"
        print ("Скачиваю файл номер " + str (count) + "\n")
        download (links [i] , name)
        count += 1
    sleep(5)

def clean_dir(length):
    file_number = int (0)
    for file_number in range (length):
        remove ( str(file_number) + ".exe")
        print ("Файл номер " + str (file_number) + " успешно удален" + "\n")

def install_apps (lenght):
    number = int (0)
    path = diropenbox()
    chdir (path)
    for number in range(lenght):
        name = str(number) + ".exe"
        subprocess.call(name, shell=True)
        pause = msgbox ("Продолжить ?")
        number += 1


install_apps(len(main_tuple))