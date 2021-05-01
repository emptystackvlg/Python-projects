import telebot 
import os 
import datetime as dt 
from win10toast import ToastNotifier
print ("Бот")

bot = telebot.TeleBot('1217728629:AAFVe-1pLS4IFZHmuQgJVI19MxTNu1K9vOA')


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ("Браузер","Spotify")

@bot.message_handler (commands=['start'])

def start (message) :
    bot.send_message(message.chat.id , "Бот запущен " , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def main (message) : 
    if message.text.lower () == "браузер" : 
        
        bot.send_message (message.chat.id ,"Запускаю браузер",reply_markup=keyboard)
       
        ToastNotifier().show_toast("BOT","Запускаю Google Chrome",threaded=True)
        os.system ('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    elif message.text.lower () == "spotify" :
        ToastNotifier().show_toast("BOT","Запускаю Spotify" , threaded=True)
        os.system('"C:/Users/Alexandr/AppData/Roaming/Spotify/Spotify.exe"')

      

bot.polling(none_stop=True)