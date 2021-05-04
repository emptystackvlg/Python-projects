
from pyowm.owm import OWM
from pyowm.commons.exceptions import NotFoundError
owm = OWM('cae9eaad6d7d0f30ada409a70e1756b9')


    mgr = owm.weather_manager()
    observation = mgr.weather_at_place("Волгоград")  # the observation object is a box containing a weather object
    weather = observation.weather
    temp_dict_celsius = weather.temperature('celsius')
    t = temp_dict_celsius ['temp']
    wind_dict = weather.wnd
    d = wind_dict ['deg']
    print (d)

except(NotFoundError):
    print ("Не найдено")

