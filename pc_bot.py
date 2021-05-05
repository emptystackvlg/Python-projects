import os
import telebot
print ("Hello")

print("Бот работает")

bot = telebot.TeleBot('1763819681:AAHp6CEje8vyPNti_uMEQ2mNb7vOevX8Ui4')

k = telebot.types.ReplyKeyboardMarkup(True)
k.row = "СКАЧАТЬ"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен ", reply_markup=k)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() == "скачать":
        bot.send_message(message.chat.id, "Сейчас")
    elif message.text.lower() == "пока":
        print("Пока до завтра")


def download(message):
    os.chdir("C:/Users/Alexandr/Downloads")


bot.polling(none_stop=True)
