import telebot

bot = telebot.TeleBot('ваш токен')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row ('Описание','Исходный код на GitHub')
keyboard1.row ('ПО и API с помощью которых был написан бот')
keyboard1.row ('Ссылки и контакты')

keyboard2 = telebot.types.ReplyKeyboardMarkup (True)
keyboard2.row ('<<--- Назад в гланое меню')
keyboard2.row ('1.Язык программирования Python')
keyboard2.row ('2.Библиотека pyTelegramBotAPI')
keyboard2.row ('3.Среда разработки PyCharm')
keyboard2.row ('4.Клиент Telegram для Windows')



keyboard3 = telebot.types.ReplyKeyboardMarkup (True)
keyboard3.row('<<--- Назад в гланое меню')
keyboard3.row ('Группа в VK', 'Канал в Telegram')
keyboard3.row ('Тема на 4PDA','Discord сервер')



@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id,"Привет " + str(message.from_user.first_name) +  " !",reply_markup = keyboard1)


@bot.message_handler(content_types=['text',"audio","photo"])

def send_text(message):
    f = open('кот.jpg', 'rb')

    if message.text.lower() == "пока":
        bot.send_message (message.chat.id,"Пока "+ str(message.from_user.first_name) +" !",reply_markup = keyboard1)

    elif message.text.lower() =="описание":
        bot.send_message (message.chat.id, "Мой создатель не дал мне описания",reply_markup = keyboard1)
        bot.send_photo (message.chat.id,f)
        bot.send_message (message.chat.id, "Напишите и выскажите ему всё своё недовольство по этому поводу" + "\n"+"https://vk.com/empty_stack",reply_markup = keyboard1)


    elif message.text.lower() == "исходный код на github":
        bot.send_message(message.chat.id ,"https://github.com/SoskaVLG/Python-projects/blob/master/bot.py"+ "\n" + "Данный код и все связанные с ним материалы являются общедоступными" )

    elif message.text.lower() == "по и api с помощью которых был написан бот":
        bot.send_message (message.chat.id ,"Вот список :",reply_markup = keyboard2)


    elif message.text.lower() == "1.язык программирования python":
        bot.send_message (message.chat.id , "Вот ссылка для скачивания : https://www.python.org/downloads/ " , reply_markup = keyboard2)


    elif message.text.lower() == "2.библиотека pytelegrambotapi":
        bot.send_message (message.chat.id , "Вот ссылка для скачивания и документация :  https://pypi.org/project/pyTelegramBotAPI/ " , reply_markup = keyboard2)


    elif message.text.lower() == "<<--- назад в гланое меню":
        bot.send_message(message.chat.id, "Возврат в главное меню " , reply_markup = keyboard1)


    elif message.text.lower () == "3.среда разработки pycharm":
        bot.send_message(message.chat.id, "Вот ссылка для скачивания : https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows " , reply_markup = keyboard2)


    elif message.text.lower() == "4.клиент telegram для windows":
        bot.send_message (message.chat.id , "Вот ссылка для скачиавания : https://tlgrm.ru/ " , reply_markup = keyboard2)


    elif message.text.lower() == "ссылки и контакты":
        bot.send_message(message.chat.id, "Вот список : ", reply_markup=keyboard3)



    elif message.text.lower() == "группа в vk":
        bot.send_message(message.chat.id, "Вот ссылка : https://vk.com/empty_telebot ", reply_markup=keyboard3)


    elif message.text.lower() == "канал в telegram":
        bot.send_message(message.chat.id, "Вот ссылка : @telebotch ", reply_markup=keyboard3)


    elif message.text.lower() == "discord сервер":
        bot.send_message(message.chat.id, "Вот ссылка : https://discord.gg/D34SJj ", reply_markup=keyboard3)


    elif message.text.lower() == "тема на 4pda":
        bot.send_message(message.chat.id, "Вот ссылка : http://4pda.ru/forum/index.php?showtopic=996428", reply_markup=keyboard3)




bot.polling()