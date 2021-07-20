class Hot_Dog () :
    def __init__ (self , meat , addons , souse):

        self.meat = meat
        self.addons  = addons
        self.souse = souse 

    def cook (self) : 
        print ("Ваша сосиска готовится") 

    def pay (self) : 
        print ("Вам нужно заплатить , прежде чем получить сосиску")

    def take (self):

        print ("Получите распишитесь :" + "\n" + "сосиска из " + self.meat + " c " + self.addons + " и " + self.souse)

    def bay (self) : 

        print ("Спасибо за покупку , всего хорошего !!!!")

My_Hot_Dog = Hot_Dog("курица" , "сыр" , "горчица")

My_Hot_Dog.pay()
My_Hot_Dog.cook()
My_Hot_Dog.take()
My_Hot_Dog.bay()
    