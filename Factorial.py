import os 

def factorial (x) :
    count = x       # счетчик для цикла вычисления факториала 
    
    sum = int (1)   # значение факториала

   

    while count > 0 :

        os.system ("ECHO \rПожалуйста подождите.... \r")

        sum *= count 

        count -= 1 

        os.system ("cls")

    print ("\n" + "Факториал числа " + str (x) + " равен : "+ str(sum) + "\n")

    os.system ("pause")
    
    os.system ("cls")

    return 0


def start () :
    
    print ("Введите число :" + "\n" )

    a = int (input ("> "))

    factorial  (a)

start ()