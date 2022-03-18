from urllib.request import urlretrieve as download 
import xlrd
from os import chdir , remove
from colorama import Fore
chdir ("C:/Users/Alexandr/Documents/GitHub/Python-projects/vstu")
try : 
    remove ("C:/Users/Alexandr/Documents/GitHub/Python-projects/vstu/vstu.xls")
except:
    pass
download ("https://www.vstu.ru/upload/raspisanie/z/%D0%9E%D0%9D_%D0%A4%D0%AD%D0%92%D0%A2_1%20%D0%BA%D1%83%D1%80%D1%81.xls","vstu.xls")

global  book
global worksheet
book = xlrd.open_workbook ("C:/Users/Alexandr/Documents/GitHub/Python-projects/vstu/vstu.xls")
worksheet = book.sheet_by_index(0)

def subjects () : 
    i = 0 
    for i in range (20,220) :
        item = worksheet.cell_value (rowx = i , colx = 35)
        if str(item.isupper ()) == "True" and str (item) != "":
            print (Fore.BLUE +"Предмет " + Fore.WHITE + item)
def techers():
    i = 0 
    for i in range (20,220) :
        item = worksheet.cell_value (rowx = i , colx = 35)
        if str (item) != "" and str(item.isupper ()) == "False": 
            print (Fore.RED +"Препод " + Fore.WHITE + item)

def classrooms () : 
    for i in range (20,220) : 
        item =  worksheet.cell_value (rowx = i , colx = 38)
        item_2 = worksheet.cell_value (rowx = i , colx = 37)
        if str(item) != "" : 
            print (Fore.GREEN +"Аудитория " + Fore.WHITE + str (item))
        elif str(item_2) != "" and str(item_2) != "лаб." and str(item_2) != "пр.":
            print (Fore.GREEN +"Аудитория " + Fore.WHITE + str (item_2))


subjects()
techers()
classrooms ()