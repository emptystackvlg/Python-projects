import telebot


bot = telebot.TeleBot('1479693109:AAGTRGTHO7ktN1_7_2izly1g2RfNK-IiZeE')


key_1 = telebot.types.ReplyKeyboardMarkup(True)
key_1.row ("Написать пожелание" )

key_1.row ("Исходный код")

key_2 = telebot.types.ReplyKeyboardMarkup(True)
key_2.row ("Написать ещё одно пожелание")

link = telebot.types.InlineKeyboardMarkup ()
url = telebot.types.InlineKeyboardButton (text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/bot_2021.py")
link.add (url)




print ("Бот запущен")

@bot.message_handler(commands=['start'])

def start_message(message):

    bot.send_message (message.chat.id,"Привет " + str(message.from_user.first_name) +  " !" , reply_markup = key_1)

    #s = open ('hello.webp' , 'rb')
    
    #bot.send_sticker(message.chat.id , s)


@bot.message_handler(content_types=['text',"audio","photo"])



def send_text(message):
    if message.text.lower() == "написать пожелание":
        bot.send_message (message.chat.id,"Отлично , чего бы Вы хотели пожелать ?")
        bot.register_next_step_handler (message , save_text)
        


    elif message.text.lower () == "написать ещё одно пожелание" :

        bot.send_message (message.chat.id , "Ладно , что на этот раз ?")
        bot.register_next_step_handler (message , save_text )



    elif message.text.lower () == "исходный код" :

        bot.send_message (message.chat.id , "Вот ссылка :" , reply_markup = link)

def save_text (message) :
    
    chat = "-291625440"
    bot.forward_message (chat, message.chat.id,message.message_id)

    bot.send_message (message.chat.id , "Я записал ")

    end = open ('end.webp' , 'rb')

    bot.send_sticker (message.chat.id , end)

    bot.send_message (message.chat.id , "Хотите написать ещё одно пожелание ?",reply_markup = key_2)


bot.polling(none_stop=True)