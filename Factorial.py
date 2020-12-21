def factorial (x) :
    count = x       # счетчик для цикла вычисления факториала 
    
    i = int (1)     # счетчик чисел 

    sum = int (1)

    while count > 0 :

        sum *= i 

        i += 1

        count -= 1 
        
    print ("\n" + "Факториал числа " + str (x) + " равен :  "+ str(sum) + "\n")


print ("Введите число :" + "\n")

a = int (input ("> "))

factorial (a)