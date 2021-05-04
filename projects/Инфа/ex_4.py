# Написал Крыков Александр 
# Работа скрипта проверена на Python 3.8.5 (32-bit)

x = int (input ("\nВведите число X \n> "))
n = ""                                      # строка для перевода входного числа в двоичный вид

line = ""                                   # строка для формирования двоичной записи выходного числа 

while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)
ml = list (n) 

s_1 = ml [ 3 ]
s_2 = ml [ 4 ]

fs_end = ml [ len (ml) - 3 ]
sd_end = ml [ len (ml) - 2 ]
th_end = ml [ len (ml) - 1 ] 

fs = ml [ 0 ]
sd = ml [ 1 ]
th = ml [ 2 ]

end_list = list ()
end_list.append (fs_end)
end_list.append (sd_end)
end_list.append (th_end)
end_list.append (s_1)
end_list.append (s_2)
end_list.append (fs)
end_list.append (sd)
end_list.append (th)


line =''.join(end_list)


print ("\n"+ str (int (line , 2 )))




