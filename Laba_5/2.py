from colorama import Fore,Back,Style
from easygui import fileopenbox
import matplotlib.pyplot as plt
from os import system
from math import sqrt,ceil,fabs

def input_var ():
    system("cls")
    path = fileopenbox (msg = "Выберите файл с данными")
    temp_mass = []
    main_mass = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines: 
            read_line = [float(x) for x in line.split()]
            temp_mass.append(read_line)
        for i in range (len(temp_mass)):
            for j in temp_mass[i] :
                main_mass.append(j)
    return (main_mass)

def make_intervals (main_mass):
    intervals = {}
    x_min = min(main_mass)
    x_max = max(main_mass)
    num_of_intervals = float (input("Введите количество интервалов\n> "))
    global h
    h = (x_max - x_min)/num_of_intervals
    dh = float ((ceil(h) - h))
    dh *= num_of_intervals
    dh = (float("{0:.4f}".format(dh)))
    print (dh/2)
    h = ceil(h)  
    print ("Шаг равен : " + str (h))
    
    current_x = float ("{0:.1f}".format (x_min - dh/2))
    for i in range (int (num_of_intervals)):
        intervals [i] = [float ("{0:.1f}".format(current_x)) + float("{0:.1f}".format(h*i)),float ("{0:.1f}".format(current_x)) + float("{0:.1f}".format(h*(i+1)))]
    for key in intervals.keys():
        print (intervals[key])
    return intervals

def intervals_freq (main_mass,intervals):
    freq_intervals = []
    for key in intervals.keys():
        ni = 0 
        for var in main_mass:
            if (intervals[key][0]<= var <intervals[key][1]):
                ni += 1
        freq_intervals.append (ni) 
    if (sum (freq_intervals) == len (main_mass)):
        return freq_intervals            
    else :
        print ("Ошибка, сумма ni != n")
        exit(0)
def relative_freq (mass_of_ni, count_n):
    rel_freq = []
    for ni in mass_of_ni:
        ni /= count_n
        rel_freq.append (float("{0:.4f}".format(ni)))
    return rel_freq

def mid_of_intervals (intervals):
    mid = []
    for key in intervals.keys():
        ci = sum(intervals[key]) / 2
        mid.append (ci)
    return mid

def params (mass_of_ni,mid,n):
    x_v = 1 
    summ = 0
    for i in range (len(mass_of_ni)):
        summ += mass_of_ni [i] * mid[i]
    x_v = float("{0:.3f}".format(summ/n))
    summ = 0
    for i in range (len(mass_of_ni)):
        summ += mass_of_ni[i] * ((mid[i] - x_v)**2)
    d_v = float("{0:.3f}".format(summ/len (mass_of_ni)))
    Sigma_v = float("{0:.3f}".format(sqrt (d_v)))
    parametrs = {'x_v': x_v, 'd_v' : d_v, 'Sigma_v' : Sigma_v}
    return parametrs

def F_x (intervals,rel_freq):
    variables = []
    interval = []
    for value in intervals.values():
        for i in range (2):
            interval.append (value[i])
    sorted_intervals = []
    for i in interval:
        if (i not in sorted_intervals):
            sorted_intervals.append(i)

    for i in range (len(sorted_intervals)):
            if (i!=0 ):
                summ = 0 
                for j in range (i):
                    summ += rel_freq[j]
                variables.append(float("{0:.3f}".format(summ)))
            else : 
                variables.append(0)
    variables.append(float("{0:.1f}".format((sum(rel_freq)))))
    strings = []
    for i in range (len(sorted_intervals)):
        if (i!=0):
            strings.append ("F_x = " + str(variables[i]) + "\t при \t\t" + str(sorted_intervals[i-1]) + " < " + " x  <=  " + str (sorted_intervals[i]))
        else : 
            print ("\n\n")
            strings.append ("F_x = " + str (variables[i]) + " \t при\t\t" + "x  <=  " + str (sorted_intervals[i]))
    for i in strings:
        print (i + "\n\n")
    
    print (variables)
    sorted_intervals.insert(0,sorted_intervals[0]-1)
    print (sorted_intervals)
    plt.grid()
    plt.xticks(sorted_intervals)
    plt.yticks(variables)
    plt.xlabel (r'$x$')
    plt.ylabel(r'$F_x$')
    plt.title ("График эмпирической функции распределения")
    plt.ylim(0,1.05)
    plt.plot (sorted_intervals,variables,'-bo')
    plt.show()



def hyst_of_freq (x,intervals):
    interval = []
    for value in intervals.values():
        for i in range (2):
            interval.append (value[i])
    sorted_intervals = []
    for i in interval:
        if (i not in sorted_intervals):
            sorted_intervals.append(i)
    print (sorted_intervals)
    if (min(sorted_intervals) >= 0):
        plt.xlim (0,max(sorted_intervals) + 1)
    else :
        plt.xlim (min(sorted_intervals) -1,max(sorted_intervals) + 1)
    nh = []
    for n in x:
        nh.append(float("{0:.3f}".format(n/h)))
    mass_x = []
    for x in sorted_intervals:
        if (x == sorted_intervals[0]) :
            for j in range (2):
                mass_x.append(x)
        else:
            for j in range (3):
                mass_x.append(x)
    mass_x.pop()
    mass_y = []
    mass_y.append(0)
    for y in nh:
        for i in range (2):
            mass_y.append(y)
        mass_y.append(0)
    if (min(sorted_intervals) >= 0):
        plt.xlim (0,max(sorted_intervals) + 1)
    else :
        plt.xlim (min(sorted_intervals) -1,max(sorted_intervals) + 1)
    plt.grid(axis='y')
    plt.title ("Гистограмма частот")
    plt.xticks(sorted_intervals)
    plt.yticks(nh)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$ni/h$')
    plt.ylim (0,max(nh) + 0.1 )
    plt.plot (mass_x,mass_y,'r')
    plt.show()

def hyst_of_rel_freq (freq_y,intervals):
    interval = []
    for value in intervals.values():
        for i in range (2):
            interval.append (value[i])
    sorted_intervals = []
    for i in interval:
        if (i not in sorted_intervals):
            sorted_intervals.append(i)
    mass_x = []
    for x in sorted_intervals:
        if (x == sorted_intervals[0]) :
            for j in range (2):
                mass_x.append(x)
        else:
            for j in range (3):
                mass_x.append(x)
    mass_x.pop()
    mass_y = []
    mass_y.append(0)
    for y in freq_y:
        for i in range (2):
            mass_y.append(float("{0:.3f}".format(y/h)))
        mass_y.append(0)
    y_to_plot = []
    for yp in freq_y:
        y_to_plot.append(float("{0:.3f}".format(yp/h)))
    print (mass_x)
    print (mass_y)
    if (min(sorted_intervals) >= 0):
        plt.xlim (0,max(sorted_intervals) + 1)
    else :
        plt.xlim (min(sorted_intervals) -1,max(sorted_intervals) + 1)
    plt.grid(axis='y')
    plt.title ("Гистограмма относительных частот")
    plt.xlabel(r'$x$')
    plt.ylabel(r'$wi/h$')
    plt.xticks(sorted_intervals)
    plt.yticks(y_to_plot)
    plt.ylim (0,max(mass_y)+ 0.1)
    plt.plot (mass_x,mass_y)
    plt.show()

main_mass = input_var()
main_mass.sort()
print (main_mass)
intervals = make_intervals(main_mass)
print ("Частоты :" + str(intervals_freq(main_mass,intervals)))
mass_ni = intervals_freq(main_mass,intervals)
rel_freq = relative_freq (mass_ni,len (main_mass))
print ("Относительные частоты : " + str (rel_freq))
mid = mid_of_intervals (intervals)
#parametrs = params (mass_ni,mid,len(main_mass))
#print ("Параметры равны : \n")
#for key in parametrs.keys():
#  print (key + " : " + str(parametrs[key]))
hyst_of_freq(mass_ni,intervals)
hyst_of_rel_freq(rel_freq,intervals)
#F_x(intervals,rel_freq)