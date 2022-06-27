import feedparser
import telebot
import os
from telebot import apihelper
import subprocess


print("Бот работает")

bot = telebot.TeleBot('1217728629:AAF8E1uYby_LUyFTegPCTcTmsVjklwHJcWs')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row ("ЧИТАТЬ НОВОСТИ")

source = telebot.types.ReplyKeyboardMarkup(True)
source.row ("БЛОКНОТ") 



switch = telebot.types.ReplyKeyboardMarkup(True)
switch.row ('ДАЛЕЕ------>>>')
switch.row ('<<<------НАЗАД В ГЛАВНОЕ МЕНЮ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот запущен ", reply_markup = keyboard)


@bot.message_handler(content_types=['text'])
def main(message):
    i =int (0)
    if message.text.lower() == "читать новости":
        bot.send_message(message.chat.id, "Выберите новостной источник", reply_markup = source)
    
    elif message.text.lower () == "блокнот" : 
        news (message,i)
    elif message.text.lower() == "далее------>>>" :
        i += 1
        news(message ,i)

    elif message.text.lower () == '<<<------назад в главное меню' : 
        bot.send_message(message.chat.id, "Возврат в главное меню",reply_markup=keyboard)


def news (message ,l):
    NewsFeed = feedparser.parse("https://bloknot-volgograd.ru/rss_news.php")
    if l < (len(NewsFeed.entries)):
            entry = NewsFeed.entries[l]
            bot.send_message(message.chat.id, entry.link,reply_markup = switch)


bot.polling(none_stop=True)

