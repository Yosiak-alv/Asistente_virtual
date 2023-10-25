from utils.cases import *

command_mapping = {
    'reproduce': play_music,

    'hora de hoy': get_time,

    'fecha de hoy': get_date,

    'busca': search_wikipedia,

    'clima en': get_weather,
    
    'como estas': greet,

    'estas en una relacion': handle_relationship,

    'dime un chiste': tell_joke,

    'salir': exit
}


def text_response():
    while True:
        print('\033[H\033[J',end='')  # Clear the screen
        print(" ******** Seleccione una Opcion: ********")
        print("1. reproduce <nombre_de_video>")
        print("2. hora de hoy")
        print("3. fecha de hoy")
        print("4. busca <nombre_de_persona>")
        print("5. clima en <nombre_de_ciudad>")
        print("6. estas en una relacion")
        print("7. como estas")
        print("8. dime un chiste")
        print("9. salir")

        prompt = input('escriba la opcion como se muestra (ej : reproduce waka waka): ')
        # Buscar el comando en el diccionario y ejecutar la función correspondiente
        for command, function in command_mapping.items():
            if command in prompt: 
                function(prompt.replace(command,'').strip())
                break
        else:
            handle_unknown()