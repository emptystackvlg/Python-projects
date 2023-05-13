from colorama import Fore,Back,Style
from easygui import fileopenbox
import matplotlib.pyplot as plt
from os import system
from math import sqrt,ceil

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
    num_of_intervals = int (input("Введите количество интервалов\n> "))
    h = (x_max - x_min)/num_of_intervals
    h = ceil(h)
    print ("Шаг равен : " + str (h))
    for i in range (num_of_intervals):
        current_x = float (x_min)
        intervals [i] = [float (current_x + h*i),float (current_x + h*(i+1))]
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
        print ("Ошибка, сумма ni != nss")
        exit(0)
def relative_freq (mass_of_ni, count_n):
    rel_freq = []
    for ni in mass_of_ni:
        ni /= count_n
        rel_freq.append (ni)
    return rel_freq

def mid_of_intervals (intervals):
    mid = []
    for key in intervals.keys():
        ci = sum(intervals[key]) / 2
        mid.append (ci)
    return mid

def params (mass_of_ni,mid):
    x_v = 1 
    summ = 0
    for i in range (len(mass_of_ni)):
        summ += mass_of_ni [i] * mid[i]
    x_v = float("{0:.3f}".format(summ/len(mass_of_ni)))
    summ = 0
    for i in range (len(mass_of_ni)):
        summ += mass_of_ni[i] * ((mid[i] - x_v)**2)
    d_v = float("{0:.3f}".format(summ/len (mass_of_ni)))
    Sigma_v = float("{0:.3f}".format(sqrt (d_v)))
    parametrs = {'x_v': x_v, 'd_v' : d_v, 'Sigma_v' : Sigma_v}
    return parametrs


main_mass = input_var()
main_mass.sort()
print (main_mass)
intervals = make_intervals(main_mass)
print ("Частоты :" + str(intervals_freq(main_mass,intervals)))
mass_ni = intervals_freq(main_mass,intervals)
rel_freq = relative_freq (mass_ni,len (main_mass))
print ("Относительные частоты : " + str (rel_freq))
mid = mid_of_intervals (intervals)
parametrs = params (mass_ni,mid)
print ("Параметры равны : \n")
for key in parametrs.keys():
    print (key + " : " + str(parametrs[key]))