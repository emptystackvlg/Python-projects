from plyer import notification
import time
import easygui as g
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 115)

text = g.enterbox(title="Текст напоминания" , msg = "                    Введите напоминание                            ")
t = g.enterbox(title = "Промежуток напоминаний " , msg = "Введите время в минутах , через которое PyReminder будет 'напоминать' ")
T = int(t) * 60
info = g.msgbox(title = "Информация" , msg ="       Pyreminder будет 'напоминать' весь день с указанными промежутками" )
while True:
    notification.notify (title = 'Напоминание', message = str(text) , app_name ='PyReminder' , app_icon = "" , timeout = 15)
    engine.say(str(text))
    engine.runAndWait()
    time.sleep(T)
