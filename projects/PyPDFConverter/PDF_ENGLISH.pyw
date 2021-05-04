from PIL import Image
import easygui as g
import win32com.client
def image2pdf () :
    num = g.enterbox (title = "Images" , msg = "\t Enter the number of images to add \t")
    n = int (num)

    indir = g.fileopenbox ("Select JPEG or PNG image") 
    image1 = Image.open(str(indir))
    im1 = image1.convert ('RGB')
    n -= 1
    imagelist = []

    while n!=0 :
        indir_1 = g.fileopenbox ("Select JPEG or PNG image")
        image2 = Image.open(str(indir_1))
        im2 = image2.convert ('RGB')
        imagelist.append (im2)
        n -= 1

    todir = g.filesavebox("Choose a directory to save" , default = "Untitled")
    im1.save(str(todir) + ".pdf" , save_all= True , append_images=imagelist)
    
    info = g.msgbox (title = "DONE!" , msg = "\t Your PDF is ready ! \t")


def word2pdf () :
    wdFormatPDF = 17

    word = win32com.client.Dispatch('Word.Application')
    indirec = g.fileopenbox ("Select .docx file" )
    
    doc = word.Documents.Open(indirec)
    
    outdirec = g.filesavebox ("Выберите место для сохранения" , default = "Без имени")
    doc.SaveAs(outdirec + ".pdf", FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

    info_1 = g.msgbox (title = "DONE!" , msg = "                                 Ваш PDF готов !")

menu = g.buttonbox (title = "File type selection ", msg = "\t Select the type of files you want to make PDF \t ", 
                    choices = ["  Images  "   ,   "  Word Document  "] )

if menu == "  Images  " :
    image2pdf ()

elif menu == "  Word Document  " :
    word2pdf ()