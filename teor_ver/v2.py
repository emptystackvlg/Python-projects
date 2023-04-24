from colorama import Fore,Back,Style
from os import system
from collections import Counter
def input_var ():
    system("cls")
    path = str(input("Укажите путь к файлу\n> "))
    try:
        with open(path, "r") as file:
            line = file.readline()
            read_line = [float(x) for x in line.split()]
            return (read_line)
    except FileNotFoundError:     #если файл не найден
        print("Файл не найден")
        system("pause")
        input_var()
def freq (main_list):
    mass_freq = []
    old_i = []
    for i in main_list:
            if (i not in old_i):
                mass_freq.append(main_list.count(i))
            old_i.append(i)
    print (mass_freq)







def show_table (main_mass,mass_freq):
    print (Fore.GREEN + "|x|",end = "")
    for i in main_mass:
        print (Fore.RED + "|" + str(i) + "|",end="")
    print (Style.RESET_ALL)
    print (Fore.LIGHTYELLOW_EX + "|n|",end = "")
    for i in mass_freq:
        print (Fore.RED + "|" + str(i) + "|",end="")
mass = input_var()
mass.sort()
freq(mass)