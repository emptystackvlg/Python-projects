import telebot 
import os 
import datetime as dt 
from win10toast import ToastNotifier
print ("Бот запущен")

bot = telebot.TeleBot('1217728629:AAFVe-1pLS4IFZHmuQgJVI19MxTNu1K9vOA')


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ("Браузер","Spotify")

@bot.message_handler (commands=['start'])

def start (message) :
    bot.send_message(message.chat.id , "Бот запущен " , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def main (message) : 
    toaster = ToastNotifier()
    if message.text.lower () == "браузер" : 
        
        bot.send_message (message.chat.id ,"Запускаю браузер",reply_markup=keyboard)
       
        toaster.show_toast("BOT","Запускаю Яндекс.Браузер",threaded=True)
        os.system ("C:/Users/Alexandr/AppData/Local/Yandex/YandexBrowser/Application/browser.exe")
    elif message.text.lower () == "spotify" :
        toaster.show_toast("BOT","Запускаю Spotify" , threaded=True)
        os.system('"C:/Users/Alexandr/AppData/Roaming/Spotify/Spotify.exe"')

      

bot.polling(none_stop=True)