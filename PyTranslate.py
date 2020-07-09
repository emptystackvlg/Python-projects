from translate import Translator
import easygui as g
import pyperclip

lg1 = g.buttonbox( title="Выбор языка для перевода 1/2  ", msg = "              Выберите язык на который хотите перевести текст" ,
choices = ['  РУССКИЙ  ' , '  АНГЛИЙСКИЙ  ' , '  НЕМЕЦКИЙ  ' , '  ФРАНЦУЗСКИЙ  ' , '  ИТАЛЬЯНСКИЙ  ' , '  ИСПАНСКИЙ  '] )



lg = g.buttonbox(title="Выбор языка для перевода 2/2  ", msg = "                 Выберите язык с которого хотите перевести текст" ,
choices = ['  РУССКИЙ  ' , '  АНГЛИЙСКИЙ  ' , '  НЕМЕЦКИЙ  ' , '  ФРАНЦУЗСКИЙ  ' , '  ИТАЛЬЯНСКИЙ  ' , '  ИСПАНСКИЙ  '] )




if lg1 == '  РУССКИЙ  ' :
    lan = 'ru'

elif lg1 =='  АНГЛИЙСКИЙ  ':
    lan = 'English'

elif lg1== '  НЕМЕЦКИЙ  ' :
    lan = 'German'

elif lg1 == '  ФРАНЦУЗСКИЙ  ':
    lan = 'French'

elif lg1==  '  ИТАЛЬЯНСКИЙ  ' :
    lan = 'Italian'

elif lg1 == '  ИСПАНСКИЙ  ' :
    lan = 'Spanish'


if lg == '  РУССКИЙ  ' :
    lang = 'Russian'
 
    
elif lg == '  АНГЛИЙСКИЙ  ' :
    lang = 'English'

elif lg == '  НЕМЕЦКИЙ  ' :
    lang = 'German'

elif lg == '  ФРАНЦУЗСКИЙ  ' :
    lang = 'Frehch'

elif lg == '  ИТАЛЬЯНСКИЙ  ' :
    lang = 'Italian'

elif lg == '  ИСПАНСКИЙ  '  :
    lang = 'Spanish'


string = g.enterbox("      Введите текст который хотите перевести" )
translator = Translator(to_lang=lan , from_lang = lang)
trans = translator.translate(str(string))
result = g.buttonbox (title = "Результат перевода", msg = str(trans) ,
choices = ['  СКОПИРОВАТЬ  ' , '  ВЫХОД  '])
if result == "  СКОПИРОВАТЬ  " :
    pyperclip.copy(str(trans))
    copy = g.msgbox(title = "Успех!" , msg = "                          Текст скопирован в буфер обмена")