from os import chdir , remove , system
def install_libs ()  :
        system ("pip install easygui")
        system ("pip install win10toast")
        system ("pip install PyQt6")
        system ("pip install PySide6")
        system ("pip install pywin32")
        system ("pip install Pillow")
        system ("cls")
        print ("Библиотеки установлены, перезапустите программу")
        system ("pause")
        exit (0)
try :
    from easygui import enterbox , fileopenbox , filesavebox
    from win32com.client import Dispatch
    from PIL import Image
    import threading 
    from win10toast import ToastNotifier as tf 
    from PyQt6 import QtCore, QtGui, QtWidgets 
except :
        install_libs ()

        
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setMinimumSize(QtCore.QSize(400,300))
        Dialog.setStyleSheet("background {\n"
"rgb(223, 238, 237)}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 91, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : launch(0))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 220, 101, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda : launch (1))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, -20, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyPDFConverter"))
        self.pushButton.setText(_translate("Dialog", "Изображения"))
        self.pushButton_2.setText(_translate("Dialog", "Word"))
        self.label.setText(_translate("Dialog", "Выберите тип файлов"))

def word2pdf () :
    try :
        Dialog.hide()
        indirec = fileopenbox ("Выберите файл .docx")
        wdFormatPDF = 17
        word = Dispatch('Word.Application')
        doc = word.Documents.Open(indirec)
        outdirec = filesavebox ("Выберите место для сохранения")
        doc.SaveAs(outdirec + ".pdf", FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        tf().show_toast("PDFConverter","Ваш PDF файл готов", duration= 10 , threaded= True)
        system (str(outdirec) + ".pdf")
        Dialog.show()
    except:
        Dialog.show()
        word.Quit()
    return 0 

def image2pdf () :
    try :
        Dialog.hide()
        indir = fileopenbox ("Выберите изображение в формате JPEG или PNG",multiple=True)
        print (indir)
        imagelist = []
        first_image =Image.open(str(indir [0]))
        first_convert = first_image.convert("RGB")
        for i in range (1,len (indir)):
            image = Image.open(str(indir[i]))
            converted_image = image.convert ('RGB')
            imagelist.append(converted_image)
        todir = filesavebox("Выберите место для сохранения")
        first_convert.save(str(todir) + ".pdf" , save_all= True , append_images=imagelist)
        tf().show_toast("PDFConverter","Ваш PDF файл готов", duration= 10 , threaded= True)
        system (str(todir) + ".pdf")
        Dialog.show()
    except:
        Dialog.show()
    return 0 

def launch (id) : 
    if id == 0 : 
        image_thread = threading.Thread(target = image2pdf())
        image_thread.start
        image_thread.join
    elif  id == 1 : 
        word_thread = threading.Thread (target = word2pdf()) 
        word_thread.start
        word_thread.join 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    main_thread = threading.Thread(target=Dialog.show())
    main_thread.start
    main_thread.join
    sys.exit(app.exec())


