from pytube import YouTube
import easygui as g
import pyperclip
import os
url = g.buttonbox(title = 'Ссылка на видео' , msg = "               Скопируйте ссылку на видео и нажмите кнопку 'СКАЧАТЬ'",
choices = ['  СКАЧАТЬ  '])
if url == "  СКАЧАТЬ  " :
    link = pyperclip.paste()
if link == '':
    fail = g.msgbox(title="Ошибка!" , msg = "  В буфере нет ссылки на видео , скопируйте ссылку на видео и попробуйте снова")
    quit(0)

        
qt1 = g.buttonbox(title = 'Выбор качества ', msg = "                             Выберите качество            " , choices= ['  360p  ' , '  720p  '])
post = g.msgbox("После скачивания появится окно с указанием пути , по которому хранится скачанный файл")
if qt1 == "  360p  " :
     qt = 18




elif qt1 == "  720p  " :
    qt = 22




YouTube(str( link)).streams.get_by_itag(int(qt)).download()
cwd = os.getcwd()
print (cwd)
info = g.buttonbox (title = "Путь к видео ",msg="Ваше видео находится по пути : " + "\n" + str(cwd),
choices = ['  ОТКРЫТЬ ПАПКУ С ВИДЕО  '])
if info == '  ОТКРЫТЬ ПАПКУ С ВИДЕО  ' :
    p=os.path.abspath(cwd) 
    os.system('explorer '+ str(p) )

