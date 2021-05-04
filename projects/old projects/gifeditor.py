from moviepy.editor import *
from easygui import msgbox , diropenbox , fileopenbox
file = fileopenbox(title = "Выберите файл в формате mp4")
save = diropenbox (title = "Выберите папку для сохранения")
clip = VideoFileClip(file)
clip. write_gif(save +'\\output.gif')
ok = msgbox(title = "Успех!" , msg = "Ваш GIF сохранен по пути : " + "\n" + save + '\\output.gif')