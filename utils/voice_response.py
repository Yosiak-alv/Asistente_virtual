import speech_recognition as sr
from utils.cases import *

listener = sr.Recognizer()

def command_voice():
    try:
        with sr.Microphone() as source:
            print("Dime una pregunta...")
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice, language='es-ES')
            command = command.lower()
            return command
    except Exception as e:
        print(e)
        return ''
    
command_mapping = {
    'reproduce': play_music,
    
    'hora de hoy': get_time,

    'fecha de hoy': get_date,

    'busca': search_wikipedia,

    'clima en': get_weather,
    
    'como estas': greet,
    'cómo estás': greet,
    
    'estas en una relacion': handle_relationship,
    'estás en una relación': handle_relationship,

    'dime un chiste': tell_joke,

    'salir': exit
}

def voice_response():
    while True:
        print('\033[H\033[J',end='')  # Clear the screen
        print(" ******** Di Cualquera de estas opciones: (ej: reproduce waka waka) ********")
        print("1. reproduce <nombre_de_video>")
        print("2. hora de hoy")
        print("3. fecha de hoy")
        print("4. busca <nombre_de_persona>")
        print("5. clima en <nombre_de_ciudad>")
        print("6. estas en una relacion")
        print("7. como estas")
        print("8. dime un chiste")
        print("9. salir")
        commands = command_voice()
        print(commands)
        # Buscar el comando en el diccionario y ejecutar la función correspondiente
        for command, function in command_mapping.items():
            if command in commands: 
                function(commands.replace(command,'').strip())
                break
        else:
            handle_unknown()