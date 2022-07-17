import  os
from easygui import diropenbox
from moviepy.editor import * 
from pyfiglet import Figlet
text = Figlet (font = 'slant')
print (text.renderText("Py_Converter"))
directory = diropenbox ("Выбериите папку с видео")
files = os.listdir(directory) 
print('\n'.join(files)) 
print (type (files))
dir_to_save = diropenbox ("Выберите папку для сохранения музыки")
for file in files: 
    audioclip = AudioFileClip(directory+"\\"+file) 
    audioclip.write_audiofile(dir_to_save+"\\"+file+".mp3") 
    print(file+".mp3")
perm_for_del = str (input ("Удалить видео ? (Y/N)\n> "))
if perm_for_del == "Y":
    for file in files : 
        os.remove(directory + "\\" + file)

else:
    exit (0)