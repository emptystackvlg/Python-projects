def main () :
    i = 100000

    j = 0 

    
    print ("Всё 'счастливые' числа : " + "\n" + "\n" + "\n" )

    while i < 1000000 :

        ml = list(str (i))

        one = int (ml[0])

        two = int (ml[1])

        three = int (ml [2])

        four = int (ml [3])

        five = int (ml [4])

        six = int (ml [5])

        f = one + two + three 

        s = four + five + six 

        if f == s :
            print (str (i) + "\n" + "\n")

            j += 1
        
        i += 1

    print ("\n"+"\n"+"\n")
    print ("Общее количество : " + str (j))

main ()