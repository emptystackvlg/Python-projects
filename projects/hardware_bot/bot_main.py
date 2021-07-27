import telebot
from telebot import types
from psutil import virtual_memory
bot = telebot.TeleBot ('')


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ('ВВЕСТИ ПАРОЛЬ')

main = telebot.types.ReplyKeyboardMarkup(True)
main.row ("ТЕСТ")



@bot.message_handler (commands = ['start'] ) 
def start_message (message) : 
    bot.send_message (message.chat.id , "Привет , я готов к работе !" , reply_markup=keyboard) 
@bot.message_handler(content_types = ['text'])

def send (message) : 
    if message.text.lower() == 'ввести пароль' :
        bot.send_message(message.chat.id , "Введите пароль",reply_markup=False)
        bot.register_next_step_handler(message,password)
    elif message.text.lower () == 'тест' : 
        memoryUse =virtual_memory()[4]/2.**30
        mem = float('{:.2f}'.format(memoryUse))
        bot.send_message (message.chat.id ,"Свободно памяти : " + str (mem) + " GB" )


def password (message) : 

    if message.text == '8664' :
        bot.send_message (message.chat.id , "Пароль введен правильно , доступ получен !",reply_markup=main)
        return 0
    else : 
        bot.send_message (message.chat.id , "Неверный пароль , попробуйте ещё раз !" , reply_markup=keyboard) 

bot.polling (none_stop=True)
