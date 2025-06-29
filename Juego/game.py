import random

def game():
    #Diccionario para las opciones del jugador
    opciones = {1: "✊", 2: "🖐️", 3: "✌️"}  # Diccionario de opciones
    nombre_opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    
    #Menú Bienvenida
    print('Bienvenido a ✊ 🖐️ ✌️')
    print('Selecciona cual quieres usar:\n1. ✊ Piedra\n2. 🖐️ Papel\n3. ✌️ Tijera')
    
    #Manejo de eleccion de Jugador
    while True:
        try:
            eleccion = int(input("Elige tu opción (1 - 3): "))
            if eleccion not in opciones:
                print("Ingresa una opción valida")
                continue
        except ValueError:
            print("Ingresa un numero valido")
            continue

        #Jugada computadora 
        computadora = random.randint(1, 3)

        #Mensaje para mostrar elecciones de Jugador y la computadora
        print(f"\nTú elegiste: {nombre_opciones[eleccion]} {opciones[eleccion]}")
        print(f"\nLa computadora eligió: {nombre_opciones[computadora]} {opciones[computadora]}")

        #Manejo de quien gana
        if eleccion == computadora:
            print("\nEs un empate\n")
        elif (eleccion == 1 and computadora == 3) or (eleccion == 2 and computadora == 1) or (eleccion == 3 and computadora == 2):
            print("\nGanaste, Felicidades 🥳\n")
        else:
            print("\nHaz perdido Crack!\n")

        #Para dejar de jugar
        again = input("Quieres volver a jugar (Si - No):").lower

        if again != "si":
            print("Gracias por jugar, hasta pronto :D")
            break

game()