import telebot
import requests
import datetime
import schedule
import  time
global s

bot = telebot.TeleBot('1293717665:AAEb7-Eqv15tUO1khA30w_CU7mw1cT56J8w')




def main():

    print ("Запущен")




    @bot.message_handler(commands=['start'])

    def start_message(message):

        bot.send_message(message.chat.id,"Здравствуйте " + str(message.from_user.first_name) +  " !")





    @bot.message_handler(content_types=['text' , 'photo','audio','document','sticker','voice' ,'video' ,'location' ,'contact' , 'new_chat_participant', 'left_chat_participant' , 'new_chat_title' ,'new_chat_photo' , 'delete_chat_photo' ,'group_chat_created'])



    def all(message):
        now = datetime.datetime.now()
        m = now.minute
        h = now.hour
        if h == 16 and m ==16:
            s = requests.Session()
            s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2} '.format(
            '1293717665:AAEb7-Eqv15tUO1khA30w_CU7mw1cT56J8w', message.message_id, message.chat.id ))
            schedule.cancel_job(job1)





    bot.polling(none_stop=False)


job1 = schedule.every().day.at("16:16").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
























