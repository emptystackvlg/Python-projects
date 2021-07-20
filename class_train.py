import os 
import time 
os.system("cls")

class Hot_Dog () :
    def __init__ (self , meat , addons , souse):

        self.meat = meat
        self.addons  = addons
        self.souse = souse 

    def cook (self) : 
        print ("Ваша сосиска готовится" + "\n") 
        time.sleep(5)

    def pay (self) :
        final_price = int(0)
        if self.meat == "курица" :
            final_price += 50
        elif self.meat == "свинина" :
            final_price += 70 
        elif self.meat == "говядина" :
            final_price += 70
        if self.addons == "сыр" :
            final_price += 30
        elif self.addons == "капуста" or self.addons == "лук" :
            final_price += 15
        final_price +=30 
     
        print ("Вам нужно заплатить " + str(final_price)+" У.Е. , прежде чем получить сосиску" + "\n")
        print ("Введите нужную сумму и подтвердите операцию , введя 'ОПЛАТИТЬ' :" + "\n")
        check_price = int (input("> "))        
        сonfirm = str (input("> "))   
        print ("Операция  успешно выполнена ! " + "\a\n")

    def take (self):
        print ("Получите и распишитесь :" + "\n" + "сосиска из " + self.meat + " c " + self.addons + " и " + self.souse + "\n")

    def bay (self) : 
        print ("Спасибо за покупку , всего хорошего !!!!")

My_Hot_Dog = Hot_Dog("курица" , "сыр" , "горчица")

My_Hot_Dog.pay()
My_Hot_Dog.cook()
My_Hot_Dog.take()
My_Hot_Dog.bay()

