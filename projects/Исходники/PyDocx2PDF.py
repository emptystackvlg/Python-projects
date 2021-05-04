from docx2pdf import convert
import easygui as g
open = g.fileopenbox(title ="Выберите файл в формате .docx")
save = g.filesavebox(title = "Выберите папку для сохранения")
convert(open,save + ".pdf")
info = g.msgbox(title ="Успех!" , msg = "Ваш PDF готов и находится по пути:"  +"\n" + str(save) + ".pdf")