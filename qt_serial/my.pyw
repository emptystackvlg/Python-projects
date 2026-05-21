from PyQt6 import QtWidgets,uic
from PyQt6.QtSerialPort import QSerialPort,QSerialPortInfo
from PyQt6.QtCore import QIODevice,QTimer
import datetime as dt

app = QtWidgets.QApplication([])
current_port = QSerialPort ()
timer = QTimer()



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
            ui.pushButtonConnect.setText("Отключить")
            ui.comboBoxPort.setEnabled(0)
            ui.comboBoxSpeed.setEnabled(0)
            ui.pushButtonUpdatePortList.setEnabled(0)
            ui.pushButtonStartStop.setEnabled(1)
            ui.port_label.setText (f"Порт: {ui.comboBoxPort.currentText()} ({(ui.comboBoxSpeed.currentText())})")

    elif (ui.pushButtonConnect.text() == "Отключить"):                  #если закрываем порт
        current_port.close()
        ui.pushButtonConnect.setText("Подключить")
        ui.port_label.setText ("Порт:")
        ui.comboBoxPort.setEnabled(1)
        ui.comboBoxSpeed.setEnabled(1)
        ui.pushButtonUpdatePortList.setEnabled(1)
        ui.pushButtonStartStop.setEnabled(0)

def read_data():
    data = current_port.readLine().data()
    if not data:
        return
    data  = data.decode('utf-8', errors='ignore')
    if (ui.tabWidget.currentIndex() == 0):                              #если открыта вкладка "Мониторинг", обновляем в ней все данные
        ui.lcdVoltage.display(int (data))
        ui.lcdCurrent.display(int (data))
        ui.lcdPower.display(int (data)*int (data))
        
def fan_speed_checkbox ():                                              #функция для работы со скоростью вентиляторов
    if (str(ui.checkBoxFanMode.checkState()) == "CheckState.Unchecked"):
        ui.pushButtonFanSpeed.setEnabled(1)
        ui.lineEditFanSpeed.setReadOnly (0)
    elif (str(ui.checkBoxFanMode.checkState()) == "CheckState.Checked"):
        ui.pushButtonFanSpeed.setEnabled(0)
        ui.lineEditFanSpeed.setReadOnly (1)





ui = uic.loadUi("C:\\Users\\Alexandr\\Documents\\GitHub\\Python-projects\\qt_serial\\my.ui")
ui.setWindowTitle ("Electronic load monitor")
ui.setFixedSize(ui.size())

update_ports()
update_time()


timer.start(1000)

ui.pushButtonUpdatePortList.clicked.connect (update_ports)
ui.pushButtonConnect.clicked.connect(open_close_port)
ui.checkBoxFanMode.checkStateChanged.connect (fan_speed_checkbox)
timer.timeout.connect (update_time)




ui.show ()
app.exec()





