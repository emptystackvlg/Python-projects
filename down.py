from __future__ import unicode_literals
from PyQt6 import QtCore, QtGui, QtWidgets
from win10toast_click import ToastNotifier as tf 

import youtube_dl
import easygui as g
import pyperclip
import os






class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(152, 244)
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
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
        link = pyperclip.paste()
        if link == '':
           Dialog.show()
        save = g.diropenbox(title="Выберите папку для сохранения")
        ydl_opts = {
                'quiet': True
                 }
        def open () :
            os.startfile(save)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            os.chdir(save)
            ydl.download([str(link)])
            
            tf().show_toast("PyDownloader","Ваш файл скачался , нажмите чтобы открыть",duration=10,threaded=True, 
            callback_on_click=open)
    except:
        Dialog.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
