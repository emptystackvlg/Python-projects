import  os
from easygui import diropenbox
from moviepy.editor import * #подключаем пакет moviepy

directory = diropenbox ("Выбериите папку")
files = os.listdir(directory) 
print('\n'.join(files)) 
print (type (files))
for file in files: 
    audioclip = AudioFileClip(directory+"\\"+file) 
    audioclip.write_audiofile(directory+"\\"+file+".mp3") 
    print(file+".mp3")