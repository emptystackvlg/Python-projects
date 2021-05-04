from googletrans import Translator
import easygui as g
import pyperclip

lg = g.buttonbox( title="Выбор языка для перевода  ", msg = "              Выберите язык на который хотите перевести текст" ,
choices = ['  РУССКИЙ  ' , '  АНГЛИЙСКИЙ  ' , '  НЕМЕЦКИЙ  ' , '  ФРАНЦУЗСКИЙ  ' , '  ИТАЛЬЯНСКИЙ  ' , '  ИСПАНСКИЙ  '] )



if lg == '  РУССКИЙ  ' :
    dest1 = 'Russian'
 
    
elif lg == '  АНГЛИЙСКИЙ  ' :
    dest1 = 'English'

elif lg == '  НЕМЕЦКИЙ  ' :
    dest1 = 'German'

elif lg == '  ФРАНЦУЗСКИЙ  ' :
    dest1 = 'Frehch'

elif lg == '  ИТАЛЬЯНСКИЙ  ' :
    dest1 = 'Italian'

elif lg == '  ИСПАНСКИЙ  '  :
    dest1 = 'Spanish'

input = g.buttonbox(title = "Выбор метода ввода" , msg = "          Вы можете ввести текст или открыть файл для перевода" ,
choices = ['  ВВЕСТИ ТЕКСТ  ' , '  ОТКРЫТЬ ФАЙЛ  '])

if input == "  ВВЕСТИ ТЕКСТ  " :
    string = g.enterbox("      Введите текст который хотите перевести" )
elif input == "  ОТКРЫТЬ ФАЙЛ  " :
    f = g.msgbox (title ="Поддерживаемые форматы" , msg = "                Вы можете открыть файл в формате .txt ")
    file = g.fileopenbox(title = "Выбор файла")
    fl = open (file , 'r')
    string = fl.read()


translator = Translator()
ou = translator.translate(str(string) , dest = dest1)
result = g.buttonbox (title = "Результат перевода", msg = str(ou.text) ,
choices = ['  СКОПИРОВАТЬ  ' , '  ВЫХОД  '])
if result == "  СКОПИРОВАТЬ  " :
    pyperclip.copy(str(ou.text))
    copy = g.msgbox(title = "Успех!" , msg = "                          Текст скопирован в буфер обмена")