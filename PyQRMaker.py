import qrcode
import easygui as g
url = g.enterbox(title = "Ссылка" , msg = "Введите ссылку или текст для создания  QR кода")
save = g.diropenbox(title = "Выберите папку для сохранения")
img = qrcode.make(str(url))
img.save(str(save) + '\my_QRcode.png')
ok = g.msgbox(title = "Успех !" , msg = "Ваш QR код сохранен по пути :" + "\n" + str(save) + '\my_qrcode.png' )