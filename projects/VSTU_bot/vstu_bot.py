import telebot 
from pyowm.owm import OWM

print("Бот запущен")

owm = OWM('api key')

bot = telebot.TeleBot('1192738735:AAG-n0SkhhJWqoA4PcHbST-u7FhHWLMlz4k')


@bot.message_handler(commands=['start'])

def start_message(message):

    bot.send_message(message.chat.id,"Привет " + str(message.from_user.first_name) +  " !")




@bot.message_handler(content_types=['text',"audio","photo"])

def main_text (message) :
    if message.text.lower () == "привет" :
        bot.send_message (message.chat.id , "И тебе привет")
bot.polling(none_stop=True) 