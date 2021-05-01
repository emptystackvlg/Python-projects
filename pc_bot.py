import telebot 
import os 
from pyautogui import click
import datetime as dt 
from win10toast import ToastNotifier
print ("Бот работает")

bot = telebot.TeleBot('1763819681:AAHp6CEje8vyPNti_uMEQ2mNb7vOevX8Ui4')


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ("Браузер","Spotify","VS Code")
keyboard.row ("GitHub Desktop","Visual Studio")
keyboard.row ("Arduino IDE", "Processing")
keyboard.row ("qBittorrent" , "Krita")
@bot.message_handler (commands=['start'])

def start (message) :
    bot.send_message(message.chat.id , "Бот запущен " , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def main (message) : 
    if message.text.lower () == "браузер" : 
        bot.send_message (message.chat.id ,"Запускаю браузер",reply_markup=keyboard)
        ToastNotifier().show_toast("BOT","Запускаю Google Chrome",threaded=True)
        click()
        os.system ('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    
    elif message.text.lower () == "spotify" :
        bot.send_message (message.chat.id ,"Запускаю Spotify",reply_markup=keyboard)
        ToastNotifier().show_toast("BOT","Запускаю Spotify" , threaded=True)
        click()
        os.system('"C:/Users/Alexandr/AppData/Roaming/Spotify/Spotify.exe"')

    elif message.text.lower() == "vs code" : 
        bot.send_message (message.chat.id ,"Запускаю Visual Studio Code",reply_markup=keyboard)
        ToastNotifier().show_toast("BOT","Запускаю Visual Studio Code" , threaded=True)
        click()
        os.system( '"C:/Users/Alexandr/AppData/Local/Programs/Microsoft VS Code/Code.exe"' )   

    elif message.text.lower()=="github desktop" : 
        bot.send_message (message.chat.id ,"Запускаю GitHub Desktop",reply_markup=keyboard)
        ToastNotifier().show_toast("BOT" , "Запускаю GitHub Desktop" , threaded=True)
        click()
        os.system('C:/Users/Alexandr/AppData/Local/GitHubDesktop/GitHubDesktop.exe')


    elif message.text.lower () == "visual studio" : 
        bot.send_message (message.chat.id ,"Запускаю Visual Studio 2019",reply_markup=keyboard)
        ToastNotifier().show_toast("BOT" , "Запускаю Visual Studio 2019" , threaded=True)
        click()
        os.system('"C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE/devenv.exe"')
    
    elif message.text.lower() == "arduino ide" :
        bot.send_message (message.chat.id , "Запускаю Arduino IDE")
        ToastNotifier().show_toast("BOT", "Запускаю Arduino IDE" , threaded=True)
        click()
        os.system('"C:/Program Files (x86)/Arduino/arduino.exe"')

    elif message.text.lower () == "processing" : 
        bot.send_message(message.chat.id,"Запускаю Processing 13 ")
        ToastNotifier().show_toast("BOT" , "Запускаю Processing 13" , threaded=True)
        click()
        os.system('"C:\processing-3.5.4\processing.exe"')

    elif message.text.lower () == "qbittorrent" : 
        bot.send_message(message.chat.id , "Запускаю qBittorrent")
        ToastNotifier().show_toast("BOT" , "Запускаю qBittorrent" , threaded=True)
        click()
        os.system('"C:/Program Files/qBittorrent/qbittorrent.exe"')

    elif message.text.lower () == "krita" : 
        bot.send_message(message.chat.id , "Запускаю Krita Desktop")
        ToastNotifier().show_toast("BOT" , "Запускаю Krita Desktop" , threaded=True)
        click()
        os.system('"C:/Program Files/Krita (x64)/bin/krita.exe"')
bot.polling(none_stop=True)