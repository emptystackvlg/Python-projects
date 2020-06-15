import telebot

bot = telebot.TeleBot('ВАШ ТОКЕН')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Описание', 'Пока')
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id,"Привет " + str(message.from_user.first_name) +  " !",reply_markup = keyboard1)


@bot.message_handler(content_types=['text',"audio","photo"])

def send_text(message):
    f = open('кот.jpg','rb')
    if message.text.lower() == "пока":
        bot.send_message(message.chat.id,"Пока "+ str(message.from_user.first_name) +" !",reply_markup = keyboard1)
    elif message.text.lower() =="описание":
        bot.send_message(message.chat.id, "Меня еще ничему не научили",reply_markup = keyboard1)
        bot.send_photo(message.chat.id,f)


bot.polling()