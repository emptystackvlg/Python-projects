from prettytable import PrettyTable
from colorama import Fore,Back,Style
from os import chdir
#главный словарь 'Код' : ["Ссылка на скачивание","Название"]
main_dictionary = {
    'GC' : ["link","Google Chrome"],
    'YB' : ["link","Yandex Browser"],
    'OB' : ["link","Opera Browser"],
    'ME' : ["link","Microsoft Edge"],
    'FB' : ["link","Firefox Browser"],
    'TM' : ["link","Telegram Messenger"],
    'VM' : ["link","Viber Messenger"],
    'WM' : ["link","WhatsApp Messenger"],
    'MT' : ["link","Microsoft Teams"],
    'DC' : ["link","Discord Client"],
    'ZC' : ["link","Zoom Client"],
    'MC' : ["link","Media Codec Pack"],
    'VP' : ["link","VLC Player"],
    'AP' : ["link","AIMP Player"],
    'KP' : ["link","KMPlayer"],
    'DW' : ["link","DirectX Web Setup"],
    'VR' : ["link","Visual C++ Runtimes"],
    'JR' : ["link","Java Runtime"],
    'OL' : ["link","OpenAL Library"],
    'DB' : ["link","Driver Booster"],
    'HU' : ["link","HiBit Uninstaller"],
    'A6' : ["link","AIDA64"],
    'HM' : ["link","HWMonitor"],
    'CZ' : ["link","CPU-Z"],
    'GZ' : ["link","GPU-Z"],
    'CDI' : ["link","Crystal Disk Info"],
    'CDM' : ["link","Crystal Disk Mark"],
    'SP' : ["link","Sumatra PDF"],
    'PV' : ["link","PDF-XChange Viewer"],
    'QC' : ["link","qBittorrent"],
    '7Z' : ["link","7-ZIP"],
    'MA' : ["link","MSI Afterburner"],
}


def print_table():
    main_table = PrettyTable()
    main_table.field_names = ["Название программы", "Код"]
    for key in main_dictionary.keys():
        main_table.add_row([main_dictionary[key][1],key])
        main_table.add_row(["------------------------------","----"])
    print (main_table)


def create_download_list():
    download_string = ""
    answer = int (1)
    print ("Что скачать ?")
    download_string += input ("> ")
    while answer != "n":
        print ("Добавить еще ?\n")
        answer = input ("> ")
        print (answer)
        if answer =="y":
            download_string += " "
            download_string += input ("> ")
    download_list = list(download_string.split())
    print (download_list)
    return download_list

def download (download_list):
    
    for code in download_list:
        try:
            link,name = main_dictionary[code][0],main_dictionary[code][1]
            print (link)
            print (name)
        except KeyError:
            print ("Нет такого кода")




print_table()
download (create_download_list())