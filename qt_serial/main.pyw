try:
    from PyQt6 import QtWidgets,uic
    from PyQt6.QtSerialPort import QSerialPort,QSerialPortInfo
    from PyQt6.QtCore import QIODevice,QTimer,QByteArray
    from PyQt6.QtGui import QIntValidator
    import datetime as dt
    from time import sleep
except ModuleNotFoundError:
    from os import system
    system ("pip install PyQt6")
    system ("pip install datetime")

app = QtWidgets.QApplication([])
current_port = QSerialPort ()
timer = QTimer()
data_blocks = list()                                                     #глобальная перменная для хранения блоков полученных данных
data = ""
fan_update_flag = 1                                                      #глобальная переменная для выключения обновления показаний скорости вентиляторов при ручной регулировке




def show_params():                                                      #функция  для обработки и обновления данных в  интерфейсе
    global data,data_blocks,fan_update_flag 
    print ("Show!")                                       
    match (ui.tabWidget.currentIndex()):                              #если открыта вкладка "Мониторинг", обновляем в ней все данные
        case (0):
            print ("1110") 
            try:    
                print ("111")                                                      #обрабатываем ошибки, которые могут возникнуть, если данных еще нет
                ui.lcdVoltage.display(int (data_blocks[0]))
                ui.lcdCurrent.display(int (data_blocks[1]))
                ui.lcdPower.display(int (data_blocks[0])*int (data_blocks[1]))
                print ("111")  
                
                #заготовка для обновления скорости внетилтяоров
                if (fan_update_flag == 1):
                    pass
            except IndexError: 
                print ("1!")             
                return
            except ValueError:
                print ("2!")
                return
        case (2):                         #если открыта вкладка "Отладка", обновляем в ней все данные
            formatted_time = dt.datetime.now().strftime("%H:%M:%S")
            textEdit_text = str ((str(formatted_time) + " ->  " + data.data().decode('utf-8',errors="ignore").strip()))
            ui.textEditDebug.append (textEdit_text)
        case (  3):
            pass

def update_ports():                                                      #функция для обновления списка доступных COM-портов
    ui.comboBoxPort.clear()
    ui.comboBoxSpeed.setCurrentIndex (3)
    portlist = []
    ports = QSerialPortInfo().availablePorts()
    for port in ports:
        portlist.append (port.portName())
        ui.comboBoxPort.addItem (port.portName())


def update_time():                                                      #функция для обновления времени внизу окна
    ui.time_label.setText (f"Время: {dt.datetime.now().strftime("%H:%M:%S")}")


def open_close_port ():                                                 #функция для открытия\закрытия порта
    if (ui.pushButtonConnect.text() == "Подключить"):                   #если открываем порт
        current_port.setPortName (str(ui.comboBoxPort.currentText()))
        current_port.setBaudRate (int(ui.comboBoxSpeed.currentText()))
        current_port.open(QIODevice.OpenModeFlag.ReadWrite)
        if (current_port.isOpen()):
            current_port.readyRead.connect (read_data)                  #подключение функции при появлении данных в буфере
            message = "OX"                                              #отправка START кода для начала обмена
            data = QByteArray(message.encode('utf-8'))
            current_port.write(data)
            current_port.waitForBytesWritten(1000)
            ui.pushButtonConnect.setText("Отключить")
            ui.comboBoxPort.setEnabled(0)
            ui.comboBoxSpeed.setEnabled(0)
            ui.pushButtonUpdatePortList.setEnabled(0)
            ui.pushButtonStartStop.setEnabled(1)
            ui.port_label.setText (f"Порт: {ui.comboBoxPort.currentText()} ({(ui.comboBoxSpeed.currentText())})")


    elif (ui.pushButtonConnect.text() == "Отключить"):                  #если закрываем порт
        if (current_port.isOpen()):
            current_port.waitForReadyRead(1000)
            message = "NX"                                              #отправка STOP кода для начала обмена
            data = QByteArray(message.encode('utf-8'))
            current_port.write(data)
            current_port.waitForBytesWritten(1000)
        current_port.close()
        ui.pushButtonConnect.setText("Подключить")
        ui.port_label.setText ("Порт:")
        ui.comboBoxPort.setEnabled(1)
        ui.comboBoxSpeed.setEnabled(1)
        ui.pushButtonUpdatePortList.setEnabled(1)
        ui.pushButtonStartStop.setEnabled(0)

def startup_routine ():
    if (ui.pushButtonStartStop.text() == "Старт"):
        ui.pushButtonStartStop.setText("Стоп") 
    elif (ui.pushButtonStartStop.text() == "Стоп"):
        ui.pushButtonStartStop.setText ("Старт")



def read_data():
    global data,data_blocks
    while (current_port.canReadLine()):                                 #читаем данные и вызываем функцию отображения параметров в интерфейсе
        data = current_port.readLine()
        data_text = data.data().decode('utf-8',errors="ignore").strip().split('X')[0]   #отрезаем часть с "мусором"
        data_blocks = data_text.split("A")                                              #режем строку по разделителю "А" на  блоки данных
        show_params()
        print (data_blocks)
   
       # while (ui.pushButtonStartStop.text() == "Старт"):
         #   return
        

def fan_speed_checkbox ():                                              #функция для обработки переключения режима управления скоростью вентиляторов
    global fan_update_flag
    if (str(ui.checkBoxFanMode.checkState()) == "CheckState.Unchecked"):
        ui.pushButtonFanSpeed.setEnabled(1)
        ui.lineEditFanSpeed.setReadOnly (0)
        fan_update_flag = 0
    elif (str(ui.checkBoxFanMode.checkState()) == "CheckState.Checked"):
        ui.pushButtonFanSpeed.setEnabled(0)
        ui.lineEditFanSpeed.setReadOnly (1)
        fan_update_flag = 1




def set_fan_speed ():                                                   #функция обработки и отправки скорости вентиляторов
    try:
        
        fan_speed = int (ui.lineEditFanSpeed.text())
        if (fan_speed == 0):
            message = "bx"
            data = QByteArray(message.encode('utf-8'))
            current_port.write(data)
            current_port.waitForBytesWritten()
        elif (fan_speed == 1):
            message = "ax"
            data = QByteArray(message.encode('utf-8'))
            current_port.write(data)
            current_port.waitForBytesWritten()
        if (fan_speed >= 0):
            #сюда нужно написать формирование пакета и его отправку по UART на STM32
            print (fan_speed)
    except ValueError:
        pass


def ui_connect ():
    ui.pushButtonUpdatePortList.clicked.connect (update_ports)
    ui.pushButtonConnect.clicked.connect(open_close_port)
    ui.pushButtonStartStop.clicked.connect(startup_routine)
    ui.pushButtonFanSpeed.clicked.connect (set_fan_speed)
    ui.checkBoxFanMode.checkStateChanged.connect (fan_speed_checkbox)
    timer.timeout.connect (update_time)



ui = uic.loadUi("C:\\Users\\Alexandr\\Documents\\GitHub\\Python-projects\\qt_serial\\my.ui")
ui.setWindowTitle ("Electronic load monitor")
ui.setFixedSize(ui.size())
validator = QIntValidator (0,99)
ui.lineEditFanSpeed.setValidator (validator)




ui_connect ()
update_ports()
update_time()


timer.start(1000)





ui.show ()
app.exec()





