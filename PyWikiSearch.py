import wikipedia as wiki
from wikipedia.exceptions import PageError
import easygui as g
import pyperclip

wiki.set_lang ('ru')
req = g.enterbox (title = "Поиск информации ",msg = "       Что Вы хотите найти ?           ")
try:
    w = wiki.summary (str(req) , redirect=True)
    result = g.buttonbox (title = "Результат поиска " , msg = str(w) , choices = ["  СКОПИРОВАТЬ  "])    
    if result == "  СКОПИРОВАТЬ  " :
        pyperclip.copy(str(w))
        copy = g.msgbox(title = "Успех!" , msg = "                          Текст скопирован в буфер обмена")
except (PageError):
    err = g.msgbox(title = "Ошибка поиска ",msg = '                        Не найдено ! Попробуйте снова                    ')
while True :
    print ("Hello world")

