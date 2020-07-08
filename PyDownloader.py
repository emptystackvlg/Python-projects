from pytube import YouTube
import easygui as g
import os
hello = g.msgbox("        PyDownloader поможет Вам скачать видео с  YouTube в нужном качестве"                  )
post = g.msgbox("После скачивания появится окно с указанием пути , по которому хранится скачанный файл")
url = g.enterbox("  Вставьте ссылку на видео (сочетание ctrl + v на английской раскладке )            ")
qt1 = g.buttonbox("                         Выберите качество            " , choices= ['  360p  ' ,  '  720p  '])
if qt1 == "  360p  " :
     qt = 18


elif qt1 == "  720p  " :
    qt = 136





YouTube(str(url)).streams.get_by_itag(int(qt)).download()
cwd = os.getcwd()
info = g.msgbox ("Ваше видео находится по пути : " + "\n" + str(cwd))

