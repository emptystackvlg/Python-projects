from googletrans import Translator
translator = Translator()
ex = translator.translate('привет как поживаешь я разработчик' , dest = 'English')
print(ex.text)