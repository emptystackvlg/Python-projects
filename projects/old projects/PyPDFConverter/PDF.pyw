#from PIL import Image
import easygui as g
#import win32com.client
def image2pdf () :
    num = g.enterbox (title = "Количество изображений " , msg = "Введите количество изображений , которые хотите добавить ")
    n = int (num)

    indir = g.fileopenbox ("Выберите изображение в формате JPEG или PNG")
    image1 = Image.open(str(indir))
    im1 = image1.convert ('RGB')
    n -= 1
    imagelist = []

    while n!=0 :
        indir_1 = g.fileopenbox ("Выберите изображение в формате JPEG или PNG")
        image2 = Image.open(str(indir_1))
        im2 = image2.convert ('RGB')
        imagelist.append (im2)
        n -= 1

    todir = g.filesavebox("Выберите место для сохранения" , default = "Без имени")
    im1.save(str(todir) + ".pdf" , save_all= True , append_images=imagelist)
    
    info = g.msgbox (title = "УСПЕХ!" , msg = "                                 Ваш PDF готов !")


def word2pdf () :
    wdFormatPDF = 17

    word = win32com.client.Dispatch('Word.Application')
    indirec = g.fileopenbox ("Выберите файл .docx" )
    
    doc = word.Documents.Open(indirec)
    
    outdirec = g.filesavebox ("Выберите место для сохранения" , default = "Без имени")
    doc.SaveAs(outdirec + ".pdf", FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

    info_1 = g.msgbox (title = "УСПЕХ!" , msg = "                                 Ваш PDF готов !")

menu = g.buttonbox (title = "Выбор типа файлов ", msg = "            Выберите тип файлов из которых Вы хотите сделать PDF ", 
                    choices = ["  Изображения  "   ,   "  Документ Word  "] )

if menu == "  Изображения  " :
    image2pdf ()

elif menu == "  Документ Word  " :
    word2pdf ()