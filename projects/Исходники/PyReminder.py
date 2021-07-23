from plyer import notification
import time
import easygui as g
text = g.enterbox(title="Текст напоминания" , msg = "                    Введите напоминание                            ")
t = g.enterbox(title = "Промежуток напоминаний " , msg = "Введите время в минутах , через которое PyReminder будет 'напоминать' ")
T = int(t) * 60
info = g.msgbox(title = "Информация" , msg ="       Pyreminder будет 'напоминать' весь день с указанными промежутками" )
while True:
    notification.notify (title = 'Напоминание', message = str(text) , app_name ='PyReminder' , app_icon = "" , timeout = 15)
    time.sleep(T)
