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
        """ if i == 0:
            intervals[i] = [float (current_x - dh/2),float ((current_x - dh/2) + h)]
        elif i == num_of_intervals:
            intervals[i] = [float (current_x+h*i),float (current_x + dh/2 + h*(i+1))]
        else: """
        intervals [i] = [float (current_x + h*i),float (current_x + h*(i+1))]
            
    for key in intervals.keys():
        print (intervals[key])

    return intervals
def intervals_sort (main_mass,intervals):
    sort_intervals = []
    for key in intervals.keys():
        ni = 0 
        for var in main_mass:
            if (intervals[key][0]<= var <intervals[key][1]):
                ni += 1
        sort_intervals.append (ni) 
    if sum(sort_intervals) == len (main_mass):
        return sort_intervals            
main_mass = input_var()
main_mass.sort()
print (main_mass)
intervals = make_intervals(main_mass)
print (intervals_sort(main_mass,intervals))