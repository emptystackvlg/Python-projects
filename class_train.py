import os
import time

os.system("cls")

class Hot_Dog ():
    def __init__(self, meat, addons, souse):

        self.meat = meat
        self.addons = addons
        self.souse = souse

    def cook(self):
        print("Ваша сосиска готовится" + "\n")
        i = int(0)
        for i in range(1, 6):
            print("." * i)
            time.sleep(1)
        os.system("cls")

    def pay(self):
        final_price = int(0)
        if self.meat == "курица":
            final_price += 50
        elif self.meat == "свинина":
            final_price += 70
        elif self.meat == "говядина":
            final_price += 70
        if self.addons == "сыр":
            final_price += 30
        elif self.addons == "капуста" or self.addons == "лук":
            final_price += 15
        final_price += 30

        print("Вам нужно заплатить " + str(final_price) +
              " У.Е. , прежде чем получить сосиску" + "\n")
        print("Введите нужную сумму и подтвердите операцию , введя 'ОПЛАТИТЬ' :" + "\n")
        check_price = int(input("> "))
        if int (check_price) != final_price :
            print ("Не хватает")
            exit (0)
        сonfirm = str(input("> "))
        print("Операция  успешно выполнена ! " + "\n")

    def take(self):
        print("Получите и распишитесь :" + "\n" + "сосиска из " +
              self.meat + " c " + self.addons + " и " + self.souse + "\n")

    def bay(self):
        print("Спасибо за покупку , всего хорошего !!!!")


os.system("cls")
print("Выберите мясо , из которого будет сделана сосиска :  " + "\n" +
      "1. Курица " + "\n" + "2. Свинина" + "\n" + "3. Говядина " + "\n")
meat_choice = int(input("> "))
if meat_choice == 1:
    first = "курица"
elif meat_choice == 2:
    first = "свинина"
elif meat_choice == 3:
    first = "говядина"
os.system("cls")

print("\n" + "Выберите дополнительный ингредиент : " + "\n" +
      "1. Сыр " + "\n" + "2. Капуста" + "\n" + "3. Лук" + "\n")
addons_choice = int(input("> "))
if addons_choice == 1:
    second = "сыр"
elif addons_choice == 2:
    second = "капуста"
elif addons_choice == 3:
    second = "лук"
os.system("cls")

print("\n" + "Выберите соус : " + "\n" + "1. Кетчуп " + "2. Горчица" + "\n")
souse_choice = int(input("> "))
if souse_choice == 1:
    third = "кетчуп"
elif souse_choice == 2:
    third = "горчица"
os.system("cls")

My_Hot_Dog = Hot_Dog(first, second, third)

My_Hot_Dog.cook()
My_Hot_Dog.pay()
My_Hot_Dog.take()
My_Hot_Dog.bay()
