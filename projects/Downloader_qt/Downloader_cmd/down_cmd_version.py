from __future__ import unicode_literals
from os import chdir, system
import sys
from win10toast import ToastNotifier as tf 
from youtube_dl import YoutubeDL
from pyfiglet import Figlet
import easygui as gui
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
    save = gui.diropenbox(title="Выберите папку для сохранения")
    try:
        ydl_opts = {}
        with YoutubeDL(ydl_opts) as ydl:
            chdir(save)
            ydl.download([str(link)])
        print ("Загрузка завершена !")
        system ("pause")
    except:
        print ("Ошибка,попробуйте еще раз")
        system ("pause")
        system ("cls")
        youtube_downloader()        
        
youtube_downloader()


