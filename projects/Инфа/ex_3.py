# Написал Крыков Александр 
# Работа скрипта проверена на Python 3.8.5 (32-bit) 

a = int (input ("\nВведите число A \n> "))

b = int (input ("\nВведите число B (A < B) \n> "))

x = int (input ("\nВведите искомую цифру X (0 < X < 10) \n> "))

i = a                                   # счетчик для основного цикла while

element = int (0)                       # объект элемента списка для проверки чисел на условие задачи                    

count = int (0)                         # счетчик подходящих под условие задачи  чисел 

old = int (0)                           # переменная для проверки чисел на повторное появление одной цифры

while i != b + 1 : 

    ml = list (str (i))

    for element in ml :

        if int (element) == x and old != int (element) :
            count += 1 
        
        old = int (element)
    
    i = i + 1 
    
print ("\n"+ str (count))
 
