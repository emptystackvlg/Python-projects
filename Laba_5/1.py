from colorama import Fore,Back,Style
from easygui import fileopenbox
import matplotlib.pyplot as plt
from os import system
from math import sqrt
def input_var ():
    system("cls")
    path = fileopenbox (msg = "Выберите файл с данными")    
    with open(path, "r") as file:
        line = file.readline()
        read_line = [float(x) for x in line.split()]
    return (read_line)


def sort_mass (main_mass):
    sorted_mass = []
    for i in main_mass:
        if (i not in sorted_mass):
            sorted_mass.append(i)
    return (sorted_mass)
def freq (main_list):
    mass_freq = []
    old_i = []
    for i in main_list:
            if (i not in old_i):
                mass_freq.append(float (main_list.count(i)))
            old_i.append(i)
    return (mass_freq)

def relative_freq (sum_n,mass_freq):
    rel_freq = []
    x_freq = float (0)
    for i in mass_freq: 
        x_freq = 0 
        x_freq = i/sum_n
        rel_freq.append (x_freq)
    return rel_freq

def F_x (sort_mass,rel_freq):
    variables = []
    for i in range (len(sort_mass)):
        if (i!=0 ):
            summ = 0 
            for j in range (i):
                summ += rel_freq[j]
            variables.append(float("{0:.3f}".format(summ)))
        else : 
            variables.append(0)
    variables.append(float("{0:.1f}".format((sum(rel_freq)))))
    strings = []
    for i in range (len(sort_mass)):
        if (i!=0):
            strings.append ("F_x = " + str(variables[i]) + "\t при \t\t" + str(sort_mass[i-1]) + " < " + " x  <=  " + str (sort_mass[i]))
        else : 
            print ("\n\n")
            strings.append ("F_x = " + str (variables[i]) + " \t при\t\t" + "x  <=  " + str (sort_mass[i]))
    strings.append("F_x = " + str (variables[len(sort_mass)]) + "\t при \t\t" + "x  >  " + str(sort_mass[len(sort_mass)-1]))
    for i in strings:
        print (i + "\n\n")
    return variables


def params (mass,freq):
    n = len (mass)
    summ = 0
    X_v = (1/n) * sum(mass)
    for i in range (len(freq)):
        summ += ((freq[i] - X_v)**2*mass[i])
    D_v = (1/n) * summ
    Sigma_v = sqrt(D_v)
    return (X_v,D_v,Sigma_v)

def make_plot_fx (sorted_mass,variables):
    plt.grid()
    plt.xlim (0,max(sorted_mass)+1)
    plt.ylim (0,1.2)
    plt.xlabel (r'$x$')
    plt.ylabel(r'$F_x$')
    plt.title ("График эмпирической функции распределения")
    legend_x = []
    x_mass = []
    y_mass = []
    for x in sorted_mass:
        if (x == max(sorted_mass)):
            for i in range (2):
                x_mass.append(x)
            x_mass.append(x+1)
        else:
            for i in range (2):
                x_mass.append(x)    
    for y in variables:
        if (y == 0):
            y_mass.append(y)
        else:
            for i in range(2):
                y_mass.append(y)
    plt.plot (x_mass,y_mass)
    plt.show ()

def make_plot_of_freq (mass_x,mass_y):
    plt.grid()
    plt.xlim (0,max(mass_x)+1)
    plt.ylim (0,max (mass_y)+1)
    plt.xlabel (r'$xi$')
    plt.ylabel(r'$ni$')
    plt.title ("Полигон частот")
    legend_x = []
    legend_y = []
    for i in range (len(mass_x)):
        x = mass_x[i]
        y = mass_y[i]
        x = float("{0:.4f}".format(x))
        y = float("{0:.4f}".format(y))
        legend_x.append(x)
        legend_y.append(y)
    plt.plot (mass_x,mass_y, '-ro',markersize = 5)
    plt.show()  

def make_plot_of_rel_freq (mass_x,mass_y):
    plt.grid()
    plt.xlim (0,max(mass_x)+1)
    plt.ylim (0,1)
    plt.xlabel (r'$xi$')
    plt.ylabel(r'$ni/n$')
    plt.title ("Полигон относительных частот")
    legend_x = []
    legend_y = []
    for i in range (len(mass_x)):
            x = mass_x[i]
            y = mass_y[i]
            x = float("{0:.4f}".format(x))
            y = float("{0:.4f}".format(y))
            legend_x.append(x)
            legend_y.append(y)
    plt.plot (mass_x,mass_y, '-ro',markersize = 5)
    plt.show()  


def show_table (main_mass,sorted_mass,mass_freq):
    print ("Вариационный ряд: \n" + str (main_mass))
    print (Fore.GREEN + "|x|",end = "")
    for i in sorted_mass:
        print (Fore.RED + "|" + str(i) + "|",end="")
    print (Style.RESET_ALL)
    print (Fore.LIGHTYELLOW_EX + "|n|",end = "")
    for i in mass_freq:
        print (Fore.BLUE + "| " + str(i) + " |",end="")

mass = input_var()
mass.sort()

vars = (F_x(sort_mass(mass),relative_freq(sum(freq(mass)),freq(mass))))
sorted_mass = sort_mass(mass)
#make_plot_of_freq (sorted_mass,freq(mass))
#make_plot_of_rel_freq (sorted_mass,relative_freq(len(mass),freq(mass)))
make_plot_fx(sorted_mass,vars)

#print (params (sort_mass(mass),freq(mass)))

show_table (mass,sort_mass(mass),freq(mass))