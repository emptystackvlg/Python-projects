from __future__ import unicode_literals
from os import startfile , chdir, system
def install_libs () :
        system ("pip install easygui")
        system ("pip install win10toast")
        system ("pip install PyQt6")
        system ("pip install PySide6")
        system ("pip install pyperclip")
        system ("pip install yt_dlp")
        system ("cls")
        print ("Библиотеки установлены, перезапустите программу")
        system ("pause")
        exit (0)
try :
    import threading 
    from PyQt6 import QtCore, QtGui, QtWidgets
    from win10toast_click import ToastNotifier as tf 
    from yt_dlp import YoutubeDL
    from easygui import diropenbox
    from pyperclip import paste
except: 
    install_libs ()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(152, 244)
        Dialog.setMaximumSize(QtCore.QSize(152,244))
        Dialog.setMinimumSize(QtCore.QSize(152,244))
        Dialog.setStyleSheet("background {\n"
"rgb(223, 238, 237)}")
        self.download = QtWidgets.QPushButton(Dialog)
        self.download.setGeometry(QtCore.QRect(10, 140, 131, 101))
        self.download.setObjectName("download")
        self.download.clicked.connect(down)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 111))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyDownloader"))
        self.download.setText(_translate("Dialog", "СКАЧАТЬ"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Скопируйте ссылку </span></p><p><span style=\" font-size:11pt; font-weight:700;\">и нажмите кнопку</span></p></body></html>"))

def down():
    try:
        Dialog.hide()
        link = paste()
        if link == '':
           Dialog.show()
        save = diropenbox(title="Выберите папку для сохранения")
        ydl_opts = {
                'quiet': True
                 }
        def open () :
            startfile(save)
        with YoutubeDL(ydl_opts) as ydl:
            tf().show_toast("PyDownloader","Скачивание началось",duration=5,threaded=True)
            chdir(save)
            ydl.download([str(link)])
            
            tf().show_toast("PyDownloader","Ваш файл скачался , нажмите чтобы открыть",duration=10,threaded=True, 
            callback_on_click=open)
            Dialog.show()
    except:
        tf().show_toast("PyDownloader","Что-то пошло не так,попробуйте еще раз",duration=10,threaded=True,callback_on_click= None)
        Dialog.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    main_thread = threading.Thread (target= Dialog.show())
    sys.exit(app.exec())



