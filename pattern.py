print ("Введите число\n")
digit = int (input (">"))
match digit :
    case 0 :
        print ("Вы ввели ноль")
    case 1 : 
        print ("Вы ввели единицу")
    case _ :
        print ("Не знаю таких чисел")