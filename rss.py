import feedparser
import telebot

print("Бот работает")

bot = telebot.TeleBot('1763819681:AAHp6CEje8vyPNti_uMEQ2mNb7vOevX8Ui4')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ("ЧИТАТЬ НОВОСТИ")

switch = telebot.types.ReplyKeyboardMarkup(True)
switch.row ('ДАЛЕЕ------>>>')
switch.row ('<<<------НАЗАД В ГЛАВНОЕ МЕНЮ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен ", reply_markup = keyboard)


@bot.message_handler(content_types=['text'])
def main(message):
    
    if message.text.lower() == "читать новости":
       NewsFeed = feedparser.parse("https://bloknot-volgograd.ru/rss_news.php")
       for i in range(0,(len(NewsFeed.entries))):
            entry = NewsFeed.entries[i]
            bot.send_message(message.chat.id, entry.link,reply_markup = switch)
            i += 1

    elif message.text.lower () == '<<<------назад в главное меню' : 
        bot.send_message(message.chat.id, "Возврат в главное меню",reply_markup=keyboard)




bot.polling(none_stop=True)
