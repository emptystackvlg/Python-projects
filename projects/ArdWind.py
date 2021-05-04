import serial 

ser = serial.Serial ('COM3' ,9600)

current = ser.read ()

print (current)