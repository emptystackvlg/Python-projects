import telebot 
import os 
from pytube import YouTube
print ("Бот работает")

bot = telebot.TeleBot('1763819681:AAHp6CEje8vyPNti_uMEQ2mNb7vOevX8Ui4')


k = telebot.types.ReplyKeyboardMarkup(True)
k.row = "СКАЧАТЬ"
@bot.message_handler (commands=['start'])

def start (message) :
    bot.send_message(message.chat.id , "Бот запущен " , reply_markup=k)

@bot.message_handler(content_types=['text'])

def main (message) : 
    if message.text.lower () == "скачать" :
        bot.send_message (message.chat.id , "Отправьте ссылку на ролик" , reply_markup=k)
        bot.register_next_step_handler(message, download)
        
def download (message) : 
    os.chdir("C:/Users/Alexandr/Downloads")
    YouTube(str(message.text)).streams.get_highest_resolution().download()



bot.polling(none_stop=True)