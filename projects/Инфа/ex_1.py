# Написал Крыков Александр 
# Работа скрипта проверена на Python 3.8.5 (32-bit) 


i = int (100)                   # счетчик для основного цикла while

count = int ()                  # счетчик подходящих под условие задачи  чисел 

while i != 1000 :
    old = i
    
    s = i // 100
    d =  (i - ( 100 * s ) ) // 10
    e = i % 10
    
    new_str =  str (s) + str (e) 
    new = int (new_str)
    
    if old / 13 == new :
        count += old 
    
    i += 1 

print (str (count) )