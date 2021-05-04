import pyspeedtest
import easygui as eg
m = eg.buttonbox(title = "Подтверждение " ,msg="               Нажмите 'OK' , чтобы начать тестирование (около 5 секунд)                      " , 
                    choices = ['  ОК  ', '  ВЫХОД  '])
if m == "  ВЫХОД  " :
    quit(0)
elif m == "  ОК  " :
    st = pyspeedtest.SpeedTest()
    down = st.download()
    down1  = int(down)  // 1000000 
    up = st.upload()
    up1 = int (up) // 1000000
    ping = st.ping()
    ping1 = int(ping)
    result = eg.msgbox (title = "Результаты тестирования",msg="Скрость скачивания  : " + str(down1) + " mbps" + "\n" + "Скрость загрузки : " + str(up1) + " mbps" + "\n" + "Пинг : " + 
    str(ping1) + " мс")
