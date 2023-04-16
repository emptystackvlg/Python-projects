from __future__ import unicode_literals
from os import chdir, system
from win10toast import ToastNotifier as tf 
from yt_dlp import YoutubeDL
from pyfiglet import Figlet
from easygui import diropenbox
system ("cls")

def youtube_downloader () :
    system ("cls")
    text = Figlet (font = 'slant')
    print (text.renderText("Py_Downloader"))
    link = str ()
    link = input ("Введите ссылку на видео\n> ")
    if link == '':
        system ("cls")
        youtube_downloader()
    save = diropenbox(title="Выберите папку для сохранения")
    try:
        ydl_opts = {}
        with YoutubeDL(ydl_opts) as ydl:
            chdir(save)
            ydl.download([str(link)])
        print ("Загрузка завершена !")
        system ("pause")
        youtube_downloader()        
    except:
        print ("Ошибка,попробуйте еще раз")
        system ("pause")
        system ("cls")
        youtube_downloader()        


youtube_downloader()


