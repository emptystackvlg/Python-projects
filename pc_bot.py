import telebot 
print ("Бот работает")

bot = telebot.TeleBot('1763819681:AAHp6CEje8vyPNti_uMEQ2mNb7vOevX8Ui4')


keyboard = telebot.types.ReplyKeyboardMarkup(True)
@bot.message_handler (commands=['start'])

def start (message) :
    bot.send_message(message.chat.id , "Бот запущен " , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def main (message) : 
    
bot.polling(none_stop=True)