import telebot
bot = telebot.TeleBot('7205754290:AAFhTQ1zOcjt4H3r6Zgd2AIuhRZfPhcTIHQ')
test_key = telebot.types.ReplyKeyboardMarkup(True)
test_key.row ("Проверка")

area = telebot.types.ReplyKeyboardMarkup(True)
area.row ('Краснооктябрьский','Центральный')
area.row ('Ворошиловский','Советский')

people_red_oct = telebot.types.ReplyKeyboardMarkup(True)
people_red_oct.row ('Могилевская Ирина')
@bot.message_handler(commands=['start','help'])

def start_message(message):
    match message.text.lower ():
        case '/start':
            bot.send_message (message.chat.id, "<strong>Привет " + str(message.from_user.first_name) +  " !\nВыберите район:</strong>", 
                              reply_markup = area,
                              parse_mode = 'HTML'
                                )
        case '/help':
            bot.send_message (message.chat.id,"Привет " + str(message.from_user.first_name) +  " !\nРаздел в разработке", reply_markup = area)
@bot.message_handler(content_types=['text',"audio","photo"])

def main_send (message):
    match message.text.lower():
        case "краснооктябрьский" | "/красный октябрь":
            bot.send_message (message.chat.id, 'Вы выбрали Краснооктябрьский ', reply_markup = people_red_oct)
        case "центральный":
            bot.send_message (message.chat.id, 'Вы выбрали Центральный', reply_markup = area)    
        case "ворошиловский":
            bot.send_message (message.chat.id, 'Вы выбрали Ворошиловский', reply_markup = area) 
        case "советский":
            bot.send_message (message.chat.id, 'Вы выбрали Советский', reply_markup = area ) 
        case "могилевская ирина":
            bot.send_message (message.chat.id, 'Контакты тренера:\n\nМогилевская Ирина\n\ntg:@mogiirina',reply_markup=people_red_oct)
print ('Work')
bot.polling(none_stop=True)