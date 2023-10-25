import datetime
import pywhatkit
import wikipedia
import pyjokes
import pyttsx3
import locale

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate' , 145)
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang("es")
locale.setlocale(locale.LC_TIME, 'es_ES')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def play_music(song):
    print('Ok, voy a reproducir ' + song + ' en youtube')
    talk('Ok, voy a reproducir ' + song + ' en youtube')
    pywhatkit.playonyt(song)

def get_time(params=None):
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('La hora es ' + time)
    talk('La hora es ' + time)

def get_date(params=None):
    fecha = datetime.date.today().strftime("%Y-%m-%d")
    print('Hoy estamos: ' + fecha)
    talk('Hoy estamos: ' + fecha)

def search_wikipedia(query):
    info = wikipedia.summary(query, 1)
    print(info)
    talk(info)

def get_weather(city):
    pywhatkit.search(city + " clima")
    talk('Ok, esto es lo que encontré en la web acerca del clima en ' + city)

def handle_relationship(params=None):
    print('No, tengo una relación seria con el procesador')
    talk('No, tengo una relación seria con el procesador')

def tell_joke(params=None):
    result = pyjokes.get_joke(language='es', category='neutral')
    print(result)
    talk(result)

def greet(params=None):
    print('Estoy bien gracias')
    talk('Estoy bien gracias')

def handle_unknown(params=None):
    print('No comprendo, repítelo por favor')
    talk('No comprendo, repítelo por favor')

def exit(params=None):
    print('Hasta luego')
    talk('Hasta luego')
    quit()