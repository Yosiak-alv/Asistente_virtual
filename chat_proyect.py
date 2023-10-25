from utils.voice_response import voice_response
from utils.text_response import text_response

if __name__ == '__main__' :
    while True:
        print(" ******** Asistente Virtual: ********")
        print("1. Comandos por Voz ")
        print("2. Comandos por linea de Comandos ")
        print("3. Salir ")

        choice = input("Digite su Opcion: ")

        if choice == "1":
           print('\033[H\033[J',end='')  # Clear the screen
           voice_response()
        elif choice == "2":
            print('\033[H\033[J',end='')  # Clear the screen
            text_response()
        elif choice == "3":
            print('\033[H\033[J',end='')  # Clear the screen
            quit()
        else:
            print('\033[H\033[J',end='')  # Clear the screen
            print("Opcion Invalida!")