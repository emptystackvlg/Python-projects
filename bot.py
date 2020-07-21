import telebot
from translate import Translator
from pyowm.commons.exceptions import NotFoundError
import wikipedia 
from wikipedia.exceptions import PageError
import time 
from pyowm.owm import OWM


3 
print("Бот запущен")


wikipedia.set_lang ('ru')

owm = OWM('token')

#не забыть поменять API  ключ

bot = telebot.TeleBot('token')


link1 = telebot.types.InlineKeyboardMarkup()
url1 = (telebot.types.InlineKeyboardButton(text = "Перейти в группу в VK", url = "https://vk.com/empty_telebot "))
link1.add (url1)

link2 = telebot.types.InlineKeyboardMarkup()
url2 = (telebot.types.InlineKeyboardButton(text = "Перейти в Telegram канал" , url = "https://teleg.run/telebotch" ))
link2.add (url2)


link3 = telebot.types.InlineKeyboardMarkup()
url3 = (telebot.types.InlineKeyboardButton (text = "Перейти на  GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/bot.py") )
link3.add (url3)


link4 = telebot.types.InlineKeyboardMarkup()
url4 = (telebot.types.InlineKeyboardButton(text = "Исходный код на GitHub" ,  url = "https://github.com/SoskaVLG/Python-projects/blob/master/PySpeedtest.py"))
link4.add (url4)


link5 = telebot.types.InlineKeyboardMarkup()
url5 = (telebot.types.InlineKeyboardButton(text = "Исходный код на  GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyDownloader.py"))
link5.add (url5)


link6 = telebot.types.InlineKeyboardMarkup()
url6 = (telebot.types.InlineKeyboardButton(text = "Исходный код на  GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyGeometryCalc.py"))
link6.add (url6)



link7 = telebot.types.InlineKeyboardMarkup()
url7 = (telebot.types.InlineKeyboardButton(text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyHWMonitor.py"))
link7.add (url7)



link8 = telebot.types.InlineKeyboardMarkup()
url8 = (telebot.types.InlineKeyboardButton (text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyTranslate.py"))
link8.add (url8)



link9 = telebot.types.InlineKeyboardMarkup()
url9 = (telebot.types.InlineKeyboardButton (text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyWikiSearch.py"))
link9.add(url9)



link10 = telebot.types.InlineKeyboardMarkup()
url10 = (telebot.types.InlineKeyboardButton(text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyReminder.py"))
link10.add(url10)



link11 = telebot.types.InlineKeyboardMarkup()
url11 = (telebot.types.InlineKeyboardButton(text = "Исходный код на GitHub" , url = "https://github.com/SoskaVLG/Python-projects/blob/master/PyQRMaker.py"))
link11.add(url11)



mainkey = telebot.types.ReplyKeyboardMarkup(True)
mainkey.row ('Ссылки и контакты')
mainkey.row ('Основные функции ')
mainkey.row ('Самописные программы')
mainkey.row ('| ТЕХНИЧЕСКАЯ ПОДДЕРЖКА |')



keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('<<--- Назад в гланое меню')
keyboard1.row ('Каталог программ')
keyboard1.row ('Узнать погоду','Наборы стикеров')
keyboard1.row ('Перевод текста' , 'Поиск по Wikipedia')




keyboard2 = telebot.types.ReplyKeyboardMarkup (True)
keyboard2.row ('<<--- Назад к контактам и ссылкам')
keyboard2.row ('1.Язык программирования Python')
keyboard2.row ('2.Библиотека pyTelegramBotAPI')
keyboard2.row ('3.Среда разработки PyCharm')
keyboard2.row ('4.Клиент Telegram для Windows')




keyboard3 = telebot.types.ReplyKeyboardMarkup (True)
keyboard3.row('<<--- Назад в гланое меню')
keyboard3.row ('Группа в VK', 'Канал в Telegram')
keyboard3.row ('Исходный код на GitHub')
keyboard3.row ('ПО и API с помощью которых был написан бот')



progm1 = telebot.types.ReplyKeyboardMarkup (True)
progm1.row ('<<--- Назад в гланое меню')
progm1.row ('@ Аудио и видео плееры @','@ Работа с мультимедиа @')
progm1.row ('@ Геймерам @','@ Мессенджеры @')
progm1.row ('Следующая страница --->>')


progm11 = telebot.types.ReplyKeyboardMarkup(True)
progm11.row("<<--- Назад к странице № 1")
progm11.row('@ Интернет браузеры @' , '@ Torrent клиенты @')
progm11.row ('@ Утилиты @' , '@ Системное ПО и драйвера @')
progm11.row ('@ Создание игр и 3D @', '@ Разработчикам @')
progm11.row ('@ Офисные приложения и PDF @')



progm2 = telebot.types.ReplyKeyboardMarkup (True)
progm2.row ("<<--- Назад к категориям")
progm2.row ("@ AIMP @","@ Winamp @")
progm2.row ("@ KMP player @","@ VLC плеер @")


progm3 = telebot.types.ReplyKeyboardMarkup (True)
progm3.row ("<<--- Назад к категориям")
progm3.row ("@ GIMP @","@ Kdenlive @")
progm3.row ("@ Audacity @" , "@ Format Factory @")


progm4 = telebot.types.ReplyKeyboardMarkup(True)
progm4.row ("<<--- Назад к категориям")
progm4.row ("@ Discord @","@ Steam @","@ Uplay @")
progm4.row ("@ EGS Launcher @" , "@ GOG Galaxy @", )
progm4.row ("@ Origin @","@ Bethesda Launcher @")
progm4.row ("@ Rockstar Games Laucher @")



progm5 = telebot.types.ReplyKeyboardMarkup(True)
progm5.row ("<<--- Назад к категориям")
progm5.row ('@ Telegram @','@ Viber @' ,'@ WhatsApp @')
progm5.row ('@ Skype @' , '@ Zoom @')



progm6 = telebot.types.ReplyKeyboardMarkup(True)
progm6.row ("<<--- Назад к категориям (стр № 2)")
progm6.row('@ Godot Engine @','@ Unity @')
progm6.row ('@ Blender @' , '@ MagicaVoxel @' )
progm6.row ('@ LibreCAD @' , '@ FreeCAD @')



progm7 =telebot.types.ReplyKeyboardMarkup (True)
progm7.row('<<--- Назад к категориям (стр № 2)')
progm7.row('@ Google Chrome @' , '@ Opera @')
progm7.row ('@ Mozilla Firefox @' , '@ OperaGX @')
progm7.row ('@ Microsoft Edge @' , '@ Яндекс.Браузер @')


progm8 =telebot.types.ReplyKeyboardMarkup (True)
progm8.row('<<--- Назад к категориям (стр № 2)')
progm8.row('@ Visual C++ Redistributable @' , '@ DirectX @')
progm8.row ('@ Driver booster @')
progm8.row ('@ Snappy Driver Insatller @')


progm9 = telebot.types.ReplyKeyboardMarkup(True)
progm9.row ('<<--- Назад к категориям (стр № 2)')
progm9.row ('@ qBittorrent @'  , '@ μTorrent @')
progm9.row (' @ Transmition @ ' , ' @ BitTorrent @')


progm10 = telebot.types.ReplyKeyboardMarkup(True)
progm10.row ('<<--- Назад к категориям (стр № 2)')
progm10.row ('@ CPU-Z @' , '@ GPU-Z @')
progm10.row ('@ Mem Reduct @' , '@ Process Lasso @')
progm10.row ('Следующaя страницa --->>') #заменена а


progm12 = telebot.types.ReplyKeyboardMarkup(True)
progm12.row ('<<--- Назад к категориям (стр № 2)')
progm12.row ('@ AIDA64 @' , '@ Msi Afterburner @')
progm12.row ('@ WinRAR @' , '@ 7-Zip @')
progm12.row ('@ Rufus @' , '@ Etcher @')


progm13 = telebot.types.ReplyKeyboardMarkup(True)
progm13.row ('<<--- Назад к категориям (стр № 2)')
progm13.row('@ Libre Office @' , '@ Open Office @')
progm13.row ('@ PDF Veiwer @' , "@ Sumatra PDF @")


progm14 = telebot.types.ReplyKeyboardMarkup(True)
progm14.row('<<--- Назад к категориям (стр № 2)')
progm14.row('@ PyCharm @' , '@ VS Code @' , '@ Eclipse @')
progm14.row ('@ IntelliJ IDEA @' , '@ CLion @')
progm14.row ('@ Visual Studio @' , '@ Komodo IDE @')


progm15 = telebot.types.ReplyKeyboardMarkup(True)
progm15.row ('<<--- Назад в гланое меню')
progm15.row ('PySpeedtest' , 'PyDownloader')
progm15.row ('PyGeometryCalc' , 'PyHWMonitor')
progm15.row('<<--ПОКАЗАТЬ ЕЩЕ ПРОГРАММЫ-->>')



progm16 = telebot.types.ReplyKeyboardMarkup(True)
progm16.row ('<<--- Назад в гланое меню')
progm16.row ('PyTranslate' , 'PyWikiSearch')
progm16.row('PyReminder' , 'PyQRMaker')




stick1 = telebot.types.ReplyKeyboardMarkup(True)
stick1.row('<<--- Назад в гланое меню')
stick1.row('Meme Pack' , 'STALKER Pack' , 'Путин Pack')
stick1.row('Fuck RKN Pack' , 'Tom Pack')



language = telebot.types.ReplyKeyboardMarkup(True)
language.row ('Английский' , 'Французский')
language.row ('Немецкий' , 'Итальянский' , 'Испанский')












@bot.message_handler(commands=['start'])

def start_message(message):
    s = open ('hello.webp' , 'rb')
   
    bot.send_message(message.chat.id,"Привет " + str(message.from_user.first_name) +  " !",reply_markup = mainkey)
    bot.send_sticker(message.chat.id , s)









@bot.message_handler(content_types=['text',"audio","photo"])



def send_text(message):

    f = open('кот.jpg', 'rb')




    if message.text.lower() == "пока":
        bot.send_message (message.chat.id,"Пока "+ str(message.from_user.first_name) +" !",reply_markup = keyboard1)


    elif message.text.lower()=='<<--- назад к контактам и ссылкам':
        bot.send_message(message.chat.id , "Возврат к контактам и ссылкам" , reply_markup = keyboard3)


    elif message.text.lower() == "@ aimp @":
        bot.send_message(message.chat.id , "AIMP — бесплатный аудиопроигрыватель с закрытым исходным кодом, написанный на Delphi"+ "\n" + "https://www.aimp.ru/?do=download")


    elif message.text.lower() == "@ winamp @":
        bot.send_message(message.chat.id , " Winamp - универсальный медиапроигрыватель компании Nullsoft" + "\n" + "http://ru.winamp.com/",reply_markup = progm2)


    elif message.text.lower() == "@ kmp player @":
        bot.send_message(message.chat.id , "The KMPlayer — корейский проигрыватель звуковых и видео файлов для Microsoft Windows и macOS, также есть мобильная версия для Android." + "\n" + "https://kmp-player.com/", reply_markup = progm2 )


    elif message.text.lower() == "@ vlc плеер @" :
        bot.send_message(message.chat.id,"VLC media player — свободный кроссплатформенный медиапроигрыватель, разрабатываемый проектом VideoLAN." +"\n" + "https://www.videolan.org/vlc/index.ru.html",reply_markup = progm2 )



    elif message.text.lower() == "@ gimp @":
        bot.send_message(message.chat.id, "GNU Image Manipulation Program или GIMP — свободно распространяемый растровый графический редактор, программа для создания и обработки растровой графики и частичной поддержкой работы с векторной графикой." + "\n" + "https://www.gimp.org/downloads/" ,reply_markup = progm3)




    elif message.text.lower() == "@ kdenlive @" :
        bot.send_message(message.chat.id , "Kdenlive — нелинейный видео редактор с открытым исходным кодом на основе Framework MLT и KDE." + "\n" + "https://sourceforge.net/projects/kdenlive/" , reply_markup = progm3)



    elif message.text.lower() == "@ audacity @" :
        bot.send_message(message.chat.id, "Audacity — свободный многоплатформенный аудиоредактор звуковых файлов, ориентированный на работу с несколькими дорожками. Программа была выпущена и распространяется на условиях GNU General Public License." + "\n" + "https://www.audacityteam.org/download/" , reply_markup = progm3)



    elif message.text.lower() == "@ format factory @":
        bot.send_message(message.chat.id , "Format Factory — бесплатная компьютерная программа для конвертации мультимедийных файлов. Программа может конвертировать видео-, аудио- и графические файлы, а также DVD в видеофайлы, CD в аудиофайлы." + "\n" + "https://sourceforge.net/projects/format-factory/" , reply_markup = progm3)



    elif message.text.lower() == "@ discord @" :
        bot.send_message(message.chat.id , "Discord — проприетарный бесплатный мессенджер с поддержкой VoIP, видеоконференций, предназначенный для использования различными сообществами геймеров, студентов/школьников и бизнеса. " + "\n" + "https://discord.com/download" , reply_markup = progm4)


    elif message.text.lower() == "@ steam @" :
        bot.send_message(message.chat.id , "Steam — онлайн-сервис цифрового распространения компьютерных игр и программ, разработанный и поддерживаемый компанией Valve. Steam выполняет роль средства технической защиты авторских прав, платформы для многопользовательских игр и потокового вещания, а также социальной сети для игроков." + "\n" + "https://store.steampowered.com/about/" , reply_markup = progm4)


    elif message.text.lower() == "@ egs launcher @":
        bot.send_message(message.chat.id , "Epic Games Store — онлайн-сервис цифрового распространения компьютерных игр, разработанный и управляемый американской компанией Epic Games." + "\n" + "https://www.epicgames.com/store/ru/" , reply_markup = progm4)


    elif message.text.lower() == "@ gog galaxy @" :
        bot.send_message(message.chat.id , "GOG GALAXY - это клиент GOG.com , который делает загрузку и установку игр максимально удобными, а также предоставляет ряд дополнительных возможностей." + "\n" + "https://www.gog.com/galaxy" , reply_markup = progm4)


    elif message.text.lower() == "@ uplay @" :
        bot.send_message(message.chat.id , "Uplay — сервис цифрового распространения, DRM, сетевой игры и общения, созданный компанией Ubisoft. Поддерживает систему достижений/трофеев, используемую в других подобных сервисах." + "\n" + "https://uplay.ubisoft.com/ru-RU" , reply_markup = progm4)


    elif message.text.lower() == "@ origin @":
        bot.send_message(message.chat.id , "Origin — платформа цифровой дистрибуции компании Electronic Arts, которая даёт возможность пользователям приобретать компьютерные игры через Интернет и загружать их с помощью клиента Origin. 3 июня 2011 EA Store был переименован в Origin." + "\n" + "https://www.origin.com/rus/ru-ru/store/download" , reply_markup = progm4)


    elif message.text.lower() == "@ bethesda launcher @" :
        bot.send_message(message.chat.id , "Играйте в самые новые игры от Bethesda на PC, в том числе в Fallout 76, RAGE 2, Wolfenstein: Youngblood и DOOM Eternal " + "\n" + "https://bethesda.net/ru/game/bethesda-launcher" , reply_markup = progm4)


    elif message.text.lower() == "@ rockstar games laucher @":
        bot.send_message(message.chat.id , "Rockstar Games Launcher – это новое приложение для Windows, которое позволяет быстро и легко управлять вашей коллекцией игр Rockstar для PC, как цифровыми, так и физическими версиями, в том числе приобретенными в различных цифровых магазинах. Кроме того, с помощью этого приложения можно покупать новые игры от Rockstar." + "\n" + "https://ru.socialclub.rockstargames.com/rockstar-games-launcher?_ga=2.192447210.1703547802.1568637144-350218922.1554468995" , reply_markup = progm4)



    elif message.text.lower() == "@ telegram @":
        bot.send_message(message.chat.id , "Telegram — кроссплатформенный мессенджер, позволяющий обмениваться сообщениями и медиафайлами многих форматов." + "\n" + "https://tlgrm.ru/ " , reply_markup = progm5)


    elif message.text.lower() == "@ viber @":
        bot.send_message(message.chat.id , "Viber — приложение-мессенджер, которое позволяет отправлять сообщения, совершать видео- и голосовые VoIP-звонки через интернет. Голосовые вызовы между пользователями с установленным Viber бесплатны. Также в Viber имеется возможность передачи изображений, видео- и аудиосообщений, документов и файлов." + "\n" + "https://www.viber.com/ru/download/" , reply_markup = progm5)


    elif message.text.lower() == "@ whatsapp @" :
        bot.send_message(message.chat.id , "WhatsApp — популярная бесплатная система мгновенного обмена текстовыми сообщениями для мобильных и иных платформ с поддержкой голосовой и видеосвязи. Позволяет пересылать текстовые сообщения, изображения, видео, аудио, электронные документы и даже программные установки через Интернет." + "\n" + "https://www.whatsapp.com/download/" , reply_markup = progm5)


    elif message.text.lower() == "@ skype @" :
        bot.send_message(message.chat.id , "Skype — бесплатное проприетарное программное обеспечение с закрытым кодом, обеспечивающее текстовую, голосовую и видеосвязь через Интернет между компьютерами, опционально используя технологии пиринговых сетей, а также платные услуги для звонков на мобильные и стационарные телефоны" + "\n" + "https://www.skype.com/ru/get-skype/" , reply_markup = progm5)



    elif message.text.lower() == "@ zoom @" :
        bot.send_message(message.chat.id , "Zoom — это сервис для проведения видеоконференций, онлайн-встреч и создания групповых чатов. Возможности Zoom: совместное использование экрана , групповые чаты для обмена текстом, изображениями и аудио." + "\n" + "https://zoom.us/support/download" , reply_markup = progm5)



    elif message.text.lower() == "@ godot engine @":
        bot.send_message(message.chat.id , "Godot Engine — открытый кроссплатформенный 2D и 3D игровой движок под лицензией MIT, который разрабатывается сообществом Godot Engine Community. До публичного релиза в виде открытого ПО движок использовался внутри некоторых компаний Латинской Америки. " + "\n" + "https://godotengine.org/download/windows" , reply_markup = progm6)


    elif message.text.lower() == "@ unity @":
        bot.send_message(message.chat.id , "Unity — межплатформенная среда разработки компьютерных игр, разработанная американской компанией Unity Technologies. Unity позволяет создавать приложения, работающие на более чем 25 различных платформах, включающих персональные компьютеры, игровые консоли, мобильные устройства, интернет-приложения и другие." + "\n" + "https://store.unity.com/ru#plans-individual" , reply_markup = progm6)


    elif message.text.lower() == "@ blender @" :
        bot.send_message(message.chat.id , "Blender — профессиональное cвободное и открытое программное обеспечение для создания трёхмерной компьютерной графики, включающее в себя средства моделирования, скульптинга, анимации, симуляции, рендеринга, постобработки и монтажа видео со звуком, компоновки с помощью «узлов», а также создания 2D-анимаций." + "\n" + "https://www.blender.org/download/" , reply_markup = progm6)


    elif message.text.lower() == "@ magicavoxel @" :
        bot.send_message(message.chat.id , "MagicaVoxel — бесплатный инструмент для создания пиксельной 3D-графики С его помощью можно быстро и без навыков сделать картинку в стиле Monument Valley и Crossy Road. Для создания первого 3D-проекта достаточно освоить три основных инструмента — вырезание клеток (Erase), добавление новых (Attach) и покраска (Paint)" + "\n" + "https://ephtracy.github.io/" , reply_markup = progm6)


    elif message.text.lower() == "@ librecad @" :
        bot.send_message(message.chat.id , "LibreCad — кроссплатформенная, открытая и свободная САПР для 2-мерного черчения и проектирования, создана на основе QCad. LibreCAD позволяет решать задачи двухмерного проектирования, такие как подготовка инженерных и строительных чертежей, схем и планов." + "\n" + "https://sourceforge.net/projects/librecad/" , reply_markup = progm6)


    elif message.text.lower() == "@ freecad @":
        bot.send_message(message.chat.id , "FreeCAD — параметрическая САПР общего назначения с открытыми исходными кодами. Основой геометрического моделирования твёрдых тел в FreeCAD является принцип граничного представления, в то же время имеется поддержка полигональных сеток. Геометрическим ядром FreeCAD является OpenCASCADE." + "\n" + "https://www.freecadweb.org/downloads.php" , reply_markup = progm6)


    elif message.text.lower() == "@ google chrome @" :
        bot.send_message(message.chat.id , "Google Chrome — браузер, разрабатываемый компанией Google на основе свободного браузера Chromium и движка Blink. Первая публичная бета-версия для Windows вышла 2 сентября 2008 года, а первая стабильная — 11 декабря 2008 года." + "\n" + "https://www.google.com/intl/ru/chrome/" , reply_markup = progm7)


    elif message.text.lower() == "@ opera @" :
        bot.send_message(message.chat.id , "Opera — веб-браузер и пакет прикладных программ для работы в Интернете, выпускаемый компанией Opera Software. Разработан в 1994 году группой исследователей из норвежской компании Telenor. С 1995 года — продукт компании Opera Software, образованной авторами первой версии браузера." + "\n" + "https://www.opera.com/ru/download" , reply_markup = progm7)


    elif message.text.lower() == "@ mozilla firefox @" :
        bot.send_message(message.chat.id , "Mozilla Firefox — свободный браузер на движке Gecko, разработкой и распространением которого занимается Mozilla Corporation. Второй по популярности браузер в мире и первый среди свободного ПО — в июне 2016 года его рыночная доля составила ▼14,15 %." + "\n" + "https://www.mozilla.org/ru/firefox/new/" , reply_markup = progm7)


    elif message.text.lower() == "@ operagx @" :
        bot.send_message(message.chat.id, "Opera GX — это веб-браузер, разработанный норвежской компанией Opera Software специально для геймеров под операционные системы Microsoft Windows и MacOS. Opera GX была анонсирована 11 июня, во время проведения E3 2019." + "\n" + "https://www.opera.com/ru/gx", reply_markup=progm7)


    elif message.text.lower() == "@ microsoft edge @" :
        bot.send_message(message.chat.id, "Microsoft Edge — браузер от компании Microsoft, впервые выпущенный в 2015 году одновременно с самой первой версией Windows 10. Пришёл на замену Internet Explorer, который тем не менее, остался в составе ОС для обеспечения совместимости корпоративных приложений." + "\n" + "https://www.microsoft.com/ru-ru/edge", reply_markup=progm7)


    elif message.text.lower() == "@ яндекс.браузер @":
        bot.send_message(message.chat.id , "Яндекс.Браузер — браузер, созданный компанией «Яндекс» на основе движка Blink, используемого в открытом браузере Chromium. Впервые был представлен 1 октября 2012 года на технологической конференции Yet another Conference. Обозреватель от Яндекса занимает второе место на рынке настольных компьютеров в рунете. " + "\n" + "https://browser.yandex.ru/" , reply_markup = progm7)


    elif message.text.lower () == "@ visual c++ redistributable @" :
        bot.send_message(message.chat.id , "Последние поддерживаемые версии Visual C++ для скачивания (все в одном)" + "\n" + "https://www.comss.ru/page.php?id=6271" , reply_markup = progm8)


    elif message.text.lower() == "@ directx @":
        bot.send_message(message.chat.id , "DirectX — это набор API, разработанных для решения задач, связанных с программированием под Microsoft Windows. Наиболее широко используется при написании компьютерных игр. Пакет средств разработки DirectX под Microsoft Windows бесплатно доступен на сайте Microsoft." + "\n" + "https://www.microsoft.com/ru-ru/Download/confirmation.aspx?id=35" , reply_markup = progm8)


    elif message.text.lower() == "@ driver booster @" :
        bot.send_message(message.chat.id , "IObit Driver Booster — программа для  установки свежих драйверов и обновления устаревших ." + "\n" + "https://ru.iobit.com/driver-booster.php" , reply_markup = progm8)


    elif message.text.lower() == "@ snappy driver insatller @" :
        bot.send_message(message.chat.id , "Snappy Driver Installer (SDI) - мощный инструмент для поиска, установки и обновления драйверов оборудования Вашего ПК." + "\n" + "https://sourceforge.net/projects/snappy-driver-installer/" , reply_markup = progm8)



    elif message.text.lower() == "@ qbittorrent @" :
        bot.send_message(message.chat.id , "qBittorrent — свободный кросс-платформенный клиент файлообменной сети BitTorrent. Клиент написан на языке C++, основан на библиотеке libtorrent-rasterbar, графический интерфейс написан на Qt. Поисковой движок требует установленный Python." + "\n" + "https://sourceforge.net/projects/qbittorrent/" , reply_markup = progm9)


    elif message.text.lower() == "@ μtorrent @" :
        bot.send_message(message.chat.id , "μTorrent — BitTorrent-клиент для Windows, macOS, Linux и Android, написанный на C++ и отличающийся небольшим размером и высокой скоростью работы при достаточно большой функциональности. В январе 2011 года количество пользователей в месяц достигло отметки в 100 миллионов." + "\n" + "https://www.utorrent.com/intl/ru/downloads/win" , reply_markup = progm9)


    elif message.text.lower() == "@ transmition @" :
        bot.send_message(message.chat.id , "Transmission — простой BitTorrent-клиент c открытым исходным кодом. Transmission — свободное программное обеспечение, большей частью под лицензией GNU GPL с небольшими фрагментами под лицензией MIT. Transmission возможно запустить на macOS, других Unix-подобных операционных системах " + "\n" + "https://sourceforge.net/projects/transmission-daemon-cfp/" , reply_markup = progm9)


    elif message.text.lower() == "@ bittorrent @" :
        bot.send_message(message.chat.id , "BitTorrent, или Mainline, — кроссплатформенное программное обеспечение для файлообмена по протоколу BitTorrent, разработано создателем протокола Брэмом Коэном. Написано на языке C++. Существуют версии для ОС Windows, macOS. Для Solaris и OpenSolaris доступна сборка на сайте Blastwave. Возможен поиск файлов по сети." + "\n" + "https://www.bittorrent.com/ru/" ,reply_markup = progm9)


    elif message.text.lower() == "@ cpu-z @" :
        bot.send_message(message.chat.id , "CPU-Z — это бесплатная прикладная программа-утилита для отображения технической информации о персональном компьютере пользователя, работающая под ОС Microsoft Windows начиная с версии Windows 98. Выпускается также специальная версия под Android." + "\n" + "https://www.cpuid.com/softwares/cpu-z.html" , reply_markup = progm10 )

    elif message.text.lower() == "@ gpu-z @" :
        bot.send_message(message.chat.id , "GPU-Z — бесплатная прикладная программа для отображения технической информации о видеоадаптере, работающая под ОС Microsoft Windows." + "\n" + "https://www.techpowerup.com/download/techpowerup-gpu-z/" , reply_markup = progm10)


    elif message.text.lower() == "@ mem reduct @" :
        bot.send_message(message.chat.id , "Mem Reduct - небольшое приложение для освобождения страниц памяти системы. Дает возможность освободить системный кэш, модифицированные и простаивающие страницы памяти. В результате позволяет до 25% уменьшить память. Не требует установки." + "\n" + "https://www.henrypp.org/product/memreduct" , reply_markup = progm10)

    elif message.text.lower() == "@ process lasso @" :
        bot.send_message(message.chat.id , "ОписаниеProcess Lasso — условно-бесплатная утилита для 32-битных и 64-разрядных операционных систем Microsoft Windows с закрытым исходным кодом, которая служит для мониторинга и управления процессами. " + "\n" + "https://bitsum.com/" , reply_markup = progm10)


    elif message.text.lower() == "@ aida64 @" :
        bot.send_message(message.chat.id , "AIDA64 — утилита FinalWire Ltd. для тестирования и идентификации компонентов персонального компьютера под управлением операционных систем Windows, предоставляющая детальные сведения об аппаратном и программном обеспечении." + "\n" + "https://www.aida64.com/downloads" , reply_markup = progm12)


    elif message.text.lower() == "@ winrar @" :
        bot.send_message(message.chat.id , "WinRAR — архиватор файлов для 32- и 64-разрядных операционных систем Windows, позволяющий создавать, изменять и распаковывать архивы RAR и ZIP, а также работать с множеством архивов других форматов." + "\n" + "https://www.win-rar.com/start.html?&L=4" , reply_markup = progm12)
        bot.send_message(message.chat.id , "Сообщение от разработчиков  WinRAR :" + "\n" + "Купите уже кто нибудь лицензию , нам нечего есть :(" , reply_markup = progm12 )

    elif message.text.lower() == "@ rufus @" :
       bot.send_message(message.chat.id , "Rufus — бесплатное портативное приложение с открытым исходным кодом для Microsoft Windows, которое можно использовать для форматирования и создания загрузочных USB-накопителей или Live USB. Приложение разработано Питом Батардом из Akeo Consulting. " + "\n" + "https://rufus.ie" , reply_markup = progm12)


    elif message.text.lower() == "@ msi afterburner @" :
        bot.send_message(message.chat.id , "MSI Afterburner – самая известная и широко используемая утилита для разгона видеокарт. Помимо этого, она служит для получения подробной информации об аппаратных компонентах компьютера и предлагает дополнительные функции, такие как регулировка вентиляторов, тестирование производительности, видеозапись. Утилита MSI Afterburner является бесплатной и работает с видеокартами любых брендов." + "\n" + "https://ru.msi.com/page/afterburner" , reply_markup = progm12)


    elif message.text.lower() == "@ 7-zip @" :
        bot.send_message(message.chat.id , "7-Zip — свободный файловый архиватор с высокой степенью сжатия данных. Поддерживает несколько алгоритмов сжатия и множество форматов данных, включая собственный формат 7z c высокоэффективным алгоритмом сжатия LZMA." + "\n" + "https://sourceforge.net/projects/sevenzip/" , reply_markup = progm12)


    elif message.text.lower() == "@ etcher @" :
        bot.send_message(message.chat.id , "balenaEtcher — свободное программное обеспечение с открытым исходным кодом, предназначенное для записи файлов образов дисков, таких как .iso и .img, а также архивов для создания LiveUSB флэш-накопителей." + "\n" + "https://www.balena.io/etcher/" , reply_markup = progm12 )


    elif message.text.lower() == "@ libre office @" :
        bot.send_message(message.chat.id , "LibreOffice — кроссплатформенный, свободно распространяемый офисный пакет с открытым исходным кодом, созданный как ответвление OpenOffice в 2010 году. Разрабатывается сообществом из более чем 480 программистов под эгидой некоммерческого фонда The Document Foundation за счёт пожертвований отдельных лиц и организаций" + "\n" + "https://www.libreoffice.org/download/download/")


    elif message.text.lower() == "@ open office @" :
        bot.send_message(message.chat.id , "Apache OpenOffice — свободный пакет офисных приложений. Конкурирует с коммерческими офисными пакетами как на уровне форматов, так и на уровне интерфейса пользователя. Одним из первых стал поддерживать новый открытый формат OpenDocument." + "\n" + "https://sourceforge.net/projects/openofficeorg.mirror/" )


    elif message.text.lower() == "@ pdf veiwer @" :
        bot.send_message(message.chat.id , "PDF-XChange Viewer — многофункциональная программа для просмотра и редактирования PDF документов. Бесплатная версия не имеет ограничений по времени использования и отличается от полной урезанной функциональностью, которая, однако достаточна для большинства традиционных операций с PDF документами. " + "\n" + "https://www.tracker-software.com/product/pdf-xchange-viewer")


    elif message.text.lower() == "@ sumatra pdf @" :
        bot.send_message(message.chat.id , "Sumatra PDF — свободная программа, предназначенная для просмотра и печати документов в форматах PDF, DjVu, FB2, ePub, MOBI, CHM, XPS, CBR/CBZ, для платформы Windows. Программа разрабатывается на базе движка MuPDF, имеет открытый исходный код и свободно распространяется на условиях лицензии GNU GPL." + "\n" + "https://www.sumatrapdfreader.org/free-pdf-reader.html")

    
    elif message.text.lower() == "@ pycharm @" :
        bot.send_message(message.chat.id , "PyCharm — интегрированная среда разработки для языка программирования Python. Предоставляет средства для анализа кода, графический отладчик, инструмент для запуска юнит-тестов и поддерживает веб-разработку на Django. PyCharm разработана компанией JetBrains на основе IntelliJ IDEA." + "\n" + "https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows")
    
    
    elif message.text.lower() == "@ vs code @" :
        bot.send_message(message.chat.id , "Visual Studio Code — редактор исходного кода, разработанный Microsoft для Windows, Linux и macOS. Позиционируется как «лёгкий» редактор кода для кроссплатформенной разработки веб- и облачных приложений." + "\n" + "https://code.visualstudio.com/download") 
    
    
    elif message.text.lower() == "@ eclipse @" :
        bot.send_message(message.chat.id , "Eclipse — свободная интегрированная среда разработки модульных кроссплатформенных приложений. Развивается и поддерживается Eclipse Foundation. Наиболее известные приложения на основе Eclipse Platform — различные «Eclipse IDE» для разработки ПО на множестве языков." + "\n" + "https://www.eclipse.org/downloads/")
    
    
    elif message.text.lower() == "@ intellij idea @" :
        bot.send_message(message.chat.id , "IntelliJ IDEA — интегрированная среда разработки программного обеспечения для многих языков программирования, в частности Java, JavaScript, Python, разработанная компанией JetBrains." + "\n" + "https://www.jetbrains.com/ru-ru/idea/download/#section=windows")
    
    
    elif message.text.lower() == "@ clion @" :
        bot.send_message(message.chat.id , "CLion — интегрированная среда разработки для языков программирования Си и C++, разрабатываемая компанией JetBrains. Состояние CLion — бесплатная пробная версия на 30 дней. Подходит для операционных систем «Windows», «macOS», и «Linux». Начиная с версии 2017.1 в CLion появилась поддержка новых стандартов C++14 и C++17." + "\n" + "https://www.jetbrains.com/ru-ru/clion/download/#section=windows")
    
    
    elif message.text.lower() == "@ visual studio @" :
        bot.send_message(message.chat.id , "Visual Studio — это стартовая площадка для написания, отладки и сборки кода, а также последующей публикации приложений. Интегрированная среда разработки (IDE) представляет собой многофункциональную программу, которую можно использовать для различных аспектов разработки программного обеспечения. Помимо стандартного редактора и отладчика, которые существуют в большинстве сред IDE, Visual Studio включает в себя компиляторы, средства автозавершения кода, графические конструкторы и многие другие функции для упрощения процесса разработки." + "\n" + "https://visualstudio.microsoft.com/ru/downloads/")

    
    elif message.text.lower() == "@ komodo ide @" :
        bot.send_message(message.chat.id , "Komodo — выпускаемая канадской компанией ActiveState программа для разработки программного обеспечения на динамических языках программирования. В 2007 разделилась на два продукта: коммерческую среду разработки программного обеспечения Komodo IDE и свободный текстовый редактор Komodo Edit." + "\n" + "https://www.activestate.com/products/komodo-ide/download-ide/") 
    
    
    
    elif message.text.lower() == "meme pack":
        st1 = open ('memepackd_webp.zip' , 'rb')
        bot.send_document(message.chat.id , st1)


    elif message.text.lower() == "stalker pack" :
        st2 = open ('vdamki_webp.zip' , 'rb')
        bot.send_document(message.chat.id , st2)
   

    elif message.text.lower() == "путин pack" :
       st3 = open ('putins_webp.zip' , 'rb')
       bot.send_document(message.chat.id , st3)


    elif message.text.lower() == "fuck rkn pack" :
        st4 = open ('fuck_rkn_eezee_webp.zip' , 'rb')
        bot.send_document(message.chat.id , st4)


    elif message.text.lower() == "tom pack" :
        st5 = open ('fumerdrogue_webp.zip' ,'rb')
        bot.send_document(message.chat.id , st5)


    elif message.text.lower() == "pyspeedtest" :
        bot.send_message(message.chat.id , "PySpeedtest - это утилита для тестирования скоротси интернет соединения" + "\n" + "https://sourceforge.net/projects/pyspeedtest/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link4)


    elif message.text.lower() == "pydownloader" :
        bot.send_message(message.chat.id , "PyDownloader - это  программа для скачивания видео с YouTube  в выбранном качетсве" + "\n" + "https://sourceforge.net/projects/pydownloader-from-youtube/")
        bot.send_message(message.chat.id , "Исходный код : " , reply_markup = link5)


    elif message.text.lower() == "pygeometrycalc" :
        bot.send_message(message.chat.id , "PyGeometryCalc - это геометрический калькулятор позволяющий вычислять площадь и периметр различных фигур" + "\n" + "https://sourceforge.net/projects/pygeometrycalc/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link6)
   


    elif message.text.lower() == "pyhwmonitor" : 
        bot.send_message(message.chat.id , "PyHWMonitor - утилита для просмотра конфигурции пк и информации об усстановленной ОС" + "\n" + "https://sourceforge.net/projects/pyhwminotor/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link7)

    

    elif message.text.lower() == "pytranslate" :
        bot.send_message(message.chat.id , "PyTranslate - офлайн переводчик с поддержкой русског , английского , французского , немецкого , испанского , итальянского языков" + "\n" + "Также переводчик умеет переводить содержимое .txt  файлов" + "\n" + "https://sourceforge.net/projects/pytranslate/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link8)

    

    elif message.text.lower() == "pywikisearch" :
        bot.send_message (message.chat.id , "PyWikiSearch - программа для поиска информации на  Wikipedia" + "\n" + "https://sourceforge.net/projects/pywikisearch/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link9)


    elif message.text.lower() == "pyreminder" :
        bot.send_message(message.chat.id , "PyReminder  поможет Вам напомнить , то что Вам нужно , через указанные промежутки времени" + "\n" + "https://sourceforge.net/projects/pyreminder/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link10)
   
   
   
    elif message.text.lower() == "pyqrmaker" :
        bot.send_message(message.chat.id , "PyQRMaker - программа для создания QR  кодов из ссылок или текста" + "\n" + "https://sourceforge.net/projects/pyqrmaker/")
        bot.send_message(message.chat.id , "Исходный код :" , reply_markup = link11)
   
   
   
   
   
   
   
   
    elif message.text.lower() == "каталог программ":
        bot.send_message(message.chat.id, "Выберите категорию :" , reply_markup = progm1)


    elif message.text.lower() =="описание":
        bot.send_message (message.chat.id, "Мой создатель не дал мне описания",reply_markup = keyboard1)
        bot.send_photo (message.chat.id,f)
        bot.send_message (message.chat.id, "Напишите и выскажите ему всё своё недовольство по этому поводу" + "\n"+"@soska_vlg",reply_markup = keyboard1)


    elif message.text.lower() == "| техническая поддержка |" :
        bot.send_message(message.chat.id , "Техническая поддержка Telebot :" + "\n" + "@mypythonsupport_bot", reply_markup = mainkey)



    elif message.text.lower() == "исходный код на github":
        bot.send_message(message.chat.id , "Вот ссылка :" , reply_markup = link3)



    elif message.text.lower() == "по и api с помощью которых был написан бот":
        bot.send_message (message.chat.id ,"Вот список :",reply_markup = keyboard2)


    elif message.text.lower() == "1.язык программирования python":
        bot.send_message (message.chat.id , "Вот ссылка для скачивания :" + "\n" + "https://www.python.org/downloads/ " , reply_markup = keyboard2)


    elif message.text.lower() == "2.библиотека pytelegrambotapi":
        bot.send_message (message.chat.id , "Вот ссылка для скачивания и документация :" + "\n" "https://pypi.org/project/pyTelegramBotAPI/ " , reply_markup = keyboard2)



    elif message.text.lower() == "<<--- назад к категориям":
        bot.send_message(message.chat.id, "Возврат к категориям : " , reply_markup = progm1)


    elif message.text.lower() == "<<--- назад к категориям (стр № 2)":
        bot.send_message(message.chat.id, "Возврат к категориям (стр № 2): ", reply_markup=progm11)


    elif message.text.lower() == "<<--- назад в гланое меню":
        bot.send_message(message.chat.id, "Возврат в главное меню : " , reply_markup = mainkey)



    elif message.text.lower() == "следующая страница --->>":
        bot.send_message(message.chat.id , "Страница № 2 :" , reply_markup = progm11 )


    elif message.text.lower() == "следующaя страницa --->>" :
        bot.send_message(message.chat.id , "Страница № 2 :" , reply_markup = progm12 )


    elif message.text.lower() == "<<--- назад к странице № 1" :
        bot.send_message(message.chat.id , "Возврат к странице № 1 :" , reply_markup = progm1)



    elif message.text.lower() == "основные функции" :
        bot.send_message(message.chat.id , "Вот список функций :" , reply_markup= keyboard1)




    elif message.text.lower () == "3.среда разработки pycharm":
        bot.send_message(message.chat.id, "Вот ссылка для скачивания :" + "\n"  + "https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows " , reply_markup = keyboard2)


    elif message.text.lower() == "4.клиент telegram для windows":
        bot.send_message (message.chat.id , "Вот ссылка для скачивания :" + "\n" + " https://tlgrm.ru/ " , reply_markup = keyboard2)


    elif message.text.lower() == "ссылки и контакты":
        bot.send_message(message.chat.id, "Вот список : ", reply_markup=keyboard3)



    elif message.text.lower() == "группа в vk":
        bot.send_message(message.chat.id, "Вот ссылка :" + "\n",reply_markup = link1)


    elif message.text.lower() == "канал в telegram":
        bot.send_message(message.chat.id, "Вот ссылка :" + "\n", reply_markup = link2)




    elif message.text.lower() =="@ аудио и видео плееры @":
        bot.send_message(message.chat.id,"Какая из программ Вас интересует ?" ,reply_markup = progm2 )



    elif message.text.lower() =="@ работа с мультимедиа @":
        bot.send_message(message.chat.id,"Какая из программ Вас интересует ?" ,reply_markup = progm3 )


    elif message.text.lower() == "@ геймерам @":
        bot.send_message(message.chat.id, "Какая из программ Вас интересует ?", reply_markup=progm4)


    elif message.text.lower() == "@ мессенджеры @":
        bot.send_message(message.chat.id, "Какая из программ Вас интересует ?", reply_markup=progm5)


    elif message.text.lower() == "@ создание игр и 3d @" :
        bot.send_message(message.chat.id ,"Какая из программ Вас инетерсует ?" , reply_markup = progm6)


    elif message.text.lower() == "@ интернет браузеры @":
        bot.send_message(message.chat.id , "Какая из программ Вас инетерсует ?" , reply_markup = progm7 )


    elif message.text.lower() == "@ системное по и драйвера @" :
        bot.send_message(message.chat.id, "Какая из программ Вас инетерсует ?", reply_markup=progm8)



    elif message.text.lower() == "@ torrent клиенты @" :
        bot.send_message(message.chat.id, "Какая из программ Вас инетерсует ?", reply_markup= progm9)


    elif message.text.lower () == "@ утилиты @" :
        bot.send_message(message.chat.id, "Какая из программ Вас инетерсует ?", reply_markup = progm10)


    elif message.text.lower () == "@ офисные приложения и pdf @" :
        bot.send_message(message.chat.id , "Какая из программ Вас инетерсует ?" , reply_markup = progm13 )


    elif message.text.lower () == "@ разработчикам @" :
        bot.send_message(message.chat.id , "Какая из программ Вас инетерсует ?" , reply_markup = progm14 )
    

    elif message.text.lower() == "наборы стикеров" :
        bot.send_message(message.chat.id , "Какой набор стикеров Вы хотите получить ?" , reply_markup = stick1 )
    

    elif message.text.lower() == "самописные программы" :
        bot.send_message(message.chat.id , "Какая из программ Вас инетерсует ?" , reply_markup = progm15 )



    elif message.text.lower() == "узнать погоду":
        bot.send_message(message.chat.id , "Введите город в котором хотите узнать погоду")
        bot.register_next_step_handler(message , weather)

    
    
    
    elif message.text.lower () == "поиск по wikipedia" :
        bot.send_message (message.chat.id , "Введите то , что хотите найти")
        bot.register_next_step_handler(message , wiki)



    
    elif message.text.lower () == "перевод текста" :
        bot.send_message(message.chat.id , "Пока что бот умеет переводить только с русского на английский ")
        bot.send_message (message.chat.id , "Введите то , что  хотите перевести" )
        bot.register_next_step_handler(message , tran)

    

    elif message.text.lower() == "<<--показать еще программы-->>" :
        bot.send_message(message.chat.id , "Вот еще программы :"  , reply_markup = progm16)




    else:
        bot.send_message(message.chat.id , "Ошибочка вышла :(  , попробуйте ещё раз " , reply_markup = mainkey)


def weather(message) :
    try:
        bot.send_message(message.chat.id,"Секундочку......  " , reply_markup = keyboard1)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        weather = observation.weather
        temp_dict_celsius = weather.temperature('celsius')
        t = temp_dict_celsius['temp']
        t = int(t)
        wind_dict = weather.wnd
        s = wind_dict ['speed']
        wind_dict = weather.wnd
        d = wind_dict ['deg']
            
        if  0 <= d <= 44:
            v = "северный"
            
        elif 45 <= d <= 89 :
            v = "северо - восточный"
            
        elif 90 <= d <= 134 :
            v = "восточный"
            
        elif 135 <= d <= 179 :
            v = "юго - восточный"
            
        elif 180 <= d <= 224 :
            v = "южный"
            
        elif 225 <= d <= 269 :
            v = "юго - западный"
            
        elif 270 <= d <= 314 :
            v = "западный"
            
        elif 315 <= d <= 360 :
            v = "северо западный"
        w = open('owm.jpg', 'rb')    
        weather.status
        translator = Translator(to_lang="Russian")
        trans = translator.translate(weather.status.lower())
        bot.send_message(message.chat.id, "Сейчас в городе  " + message.text + "\n" + "Температура воздуха :  " + str(t) + " °С " + " и " + str(trans) + "\n" + "Скрость  и направление ветра :  " + str(s) + " м/с , "  + v)
        bot.send_message(message.chat.id , "По данным Open Weather" , reply_markup = keyboard1)
        bot.send_photo(message.chat.id ,w)
    except(NotFoundError):
        bot.send_message(message.chat.id , "Город не найден")
    
def wiki(message) :
    try:
        bot.send_message(message.chat.id , "Выполняю поиск....")
        w = wikipedia.summary (str(message.text) , redirect=True)
        page = wikipedia.page(str(message.text))
        ur = page.url
        bot.send_message(message.chat.id , "Вот что удалось найти :" + "\n" + "\n" + str(w))
        time.sleep (4)
        bot.send_message(message.chat.id , "Вот ссылка на страницу в Wikipedia :" + "\n" +str (ur))
    except(PageError):
        bot.send_message(message.chat.id , "По вашему запросу ничего не найдено" , reply_markup = keyboard1)




def tran (message):
    translator = Translator(to_lang= 'en' , from_lang = 'ru')
    trans = translator.translate(str(message.text))
    bot.send_message (message.chat.id , "Результат перевода : " + "\n" + "\n"  + str(trans))
    
        

bot.polling(none_stop=True)
