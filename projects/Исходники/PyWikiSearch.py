import wikipedia as wiki
from wikipedia.exceptions import PageError
import easygui as g
import pyperclip
lang = g.buttonbox(title = "Language" , msg = "                             Choose your language " , choices = ["  Russian  " , "  English  "] )
if lang == "  Russian  " :
    wiki.set_lang ('ru')
else:
    wiki.set_lang('en')
req = g.enterbox (title = "Поиск информации ",msg = "       Что Вы хотите найти ? \ What are you looking for ?          ")
try:
    w = wiki.summary (str(req) , redirect=True)
    result = g.buttonbox (title = "Результат поиска " , msg = str(w) , choices = ["  СКОПИРОВАТЬ \ COPY  "])    
    if result == "  СКОПИРОВАТЬ \ COPY  " :
        pyperclip.copy(str(w))
        copy = g.msgbox(title = "Успех!" , msg = "                  Текст скопирован в буфер обмена \ Successful")
except (PageError):
    err = g.msgbox(title = "Ошибка поиска ",msg = '                        Не найдено ! Попробуйте снова \ Don`t find , try again                    ')