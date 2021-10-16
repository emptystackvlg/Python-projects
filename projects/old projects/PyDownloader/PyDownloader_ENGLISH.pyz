from __future__ import unicode_literals
import youtube_dl
import easygui as g
import pyperclip
import os
url = g.buttonbox(title = 'Link to file' , msg = "                  \tCopy link and press 'DOWNLOAD' button \t",
choices = ['  DOWNLOAD  '])
if url == "  DOWNLOAD  " :
    link = pyperclip.paste()
if link == '':
    fail = g.msgbox(title="Error!" , msg = "            I don`t find a link  ")
    quit(0)
save = g.diropenbox(title = "Select directory to save")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    os.chdir(save)
    ydl.download([str(link)])
info = g.msgbox (title = "Done! ",msg="Your file was downloaded to :" + "\n" + save)
