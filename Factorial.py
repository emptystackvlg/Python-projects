def factorial (x) :
    count = x       # счетчик для цикла вычисления факториала 

    sum = int (1)

    while count > 0 :

        sum *= count

        count -= 1 
        
    print ("\n" + "Факториал числа " + str (x) + " равен :  "+ str(sum) + "\n")


print ("Введите число :" + "\n")

a = int (input ("> "))

factorial (a)
