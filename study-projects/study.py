import random 
a = [random.randint (-10,10) for i in range (10)]
b = [abs(i) for i in a]

print (a)
print (b)