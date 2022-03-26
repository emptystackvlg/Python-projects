from __future__ import unicode_literals
from os import startfile , chdir, system
def install_libs () :
        system ("pip install easygui")
        system ("pip install win10toast")
        system ("pip install pyperclip")
        system ("pip install yt_dlp")
        system ("cls")
        print ("Библиотеки установлены, перезапустите программу")
        system ("pause")
        exit (0)
        
try :
    from win10toast import ToastNotifier as tf 
    from yt_dlp import YoutubeDL
    from easygui import diropenbox
    from pyperclip import paste
    from pyfiglet import Figlet
except: 
    install_libs ()

def youtube_downloader () :
    try:
        text = Figlet (font = 'slant')
        print (text.renderText("VSTU SHEDULE"))
        link = input ("Введите ссылку на видео\n>")
        if link == '':
            print ("Ссылка пустая")
        save = diropenbox(title="Выберите папку для сохранения")
        ydl_opts = {
            'quiet': True
                    }
        with YoutubeDL(ydl_opts) as ydl:
            tf().show_toast("PyDownloader","Скачивание началось",duration=5,threaded=True)
            chdir(save)
            ydl.download([str(link)])
                
            tf().show_toast("PyDownloader","Ваш файл скачался , нажмите чтобы открыть",duration=10,threaded=True)
                
    except:
        tf().show_toast("PyDownloader","Что-то пошло не так,попробуйте еще раз",duration=10,threaded=True)
        
youtube_downloader()


