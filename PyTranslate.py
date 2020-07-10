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
input = g.buttonbox(title = "Выбор метода ввода" , msg = "          Вы можете ввести текст или открыть файл для перевода" ,
choices = ['  ВВЕСТИ ТЕКСТ  ' , '  ОТКРЫТЬ ФАЙЛ  '])

if input == "  ВВЕСТИ ТЕКСТ  " :
    string = g.enterbox("      Введите текст который хотите перевести" )
elif input == "  ОТКРЫТЬ ФАЙЛ  " :
    f = g.msgbox (title ="Поддерживаемые форматы" , msg = "                Вы можете открыть файл в формате .txt ")
    file = g.fileopenbox(title = "Выбор файла")
    fl = open (file , 'r')
    string = fl.read()


translator = Translator(to_lang=lan , from_lang = lang)
trans = translator.translate(string)
result = g.buttonbox (title = "Результат перевода", msg = str(trans) ,
choices = ['  СКОПИРОВАТЬ  ' , '  ВЫХОД  '])
if result == "  СКОПИРОВАТЬ  " :
    pyperclip.copy(str(trans))
    copy = g.msgbox(title = "Успех!" , msg = "                          Текст скопирован в буфер обмена")