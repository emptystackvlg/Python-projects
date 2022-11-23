def romanToInt(s: str) -> int:
        roman_to_int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ = int(0)
        for i in s:
            summ += roman_to_int [i]
            print (i)
            print (summ)
        return summ

romanToInt("MCMXCIV")