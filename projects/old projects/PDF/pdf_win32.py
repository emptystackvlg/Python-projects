import easygui as g 
import win32com.client
wdFormatPDF = 17

word = win32com.client.Dispatch('Word.Application')
indir = g.fileopenbox ("Выберите файл .docx")
doc = word.Documents.Open(indir)
outdir = g.filesavebox ("Выберите место для сохранения")
doc.SaveAs(outdir + ".pdf", FileFormat=wdFormatPDF)
doc.Close()
word.Quit()