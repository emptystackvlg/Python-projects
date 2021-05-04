import os 

import datetime as dt 

import time as t

def factorial (x) :
    count = x       # счетчик для цикла вычисления факториала 
    
    sum = int (1)   # значение факториала

    
    while count > 0 :

        sum *= count 

        count -= 1 

    first = t.strftime("%S")
   
    os.system ("cls")

    print (str(float (first)))

    

    


    print ("\n" + "Факториал числа " + str (x) + " равен : "+ str(sum) + "\n")

    
    second = dt.timedelta (milliseconds = int  (first))

    print (str(float(second)))

    os.system ("pause")
    
    os.system ("cls")

    return 0


def start () :
    
    print ("Введите число :" + "\n" )

    a = int (input ("> "))

    factorial  (a)

start ()