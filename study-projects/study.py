import matplotlib.pyplot as plt
def input_x (i):
    x_inputs = []
    var = float ()
    for i in range (1,i+1) :
        print (f"Введите значение X № {i}\n")
        var = input (">")
        print ("\n")
        x_inputs.append (var)
        i += 1
    return x_inputs
def input_y (i):
    y_inputs = []
    var = float ()
    for i in range (1,i+1) :
        print (f"Введите значение Y № {i}\n")
        var = input (">")
        print ("\n")
        y_inputs.append (var)
        i += 1
    return y_inputs

print ("Сколько значений ? \n")
i = int (input("> "))
plt.plot(input_x (i),input_y (i))
plt.title ("Тестовый график")
plt.show()



