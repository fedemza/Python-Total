from random import randint

nombre = input('Dime tu nombre: ')
print(f'{nombre} el programa tiene un numero 1 al 100, tienes 8 intentos para adivinarlo')

numero_programa = randint(1,100)

intentos = 1

while intentos < 9:
    numero_elegido = input(f'intento {intentos}, di tu numero: ')
    numero_elegido = int(numero_elegido)
    if numero_elegido < 1 or numero_elegido > 100:
        print('intento no valido')
        intentos += 1
    elif numero_elegido < numero_programa:
        print('Tu respuestas es incorrecta, tu numero es menor al numero secreto')
        intentos += 1
    elif numero_elegido > numero_programa:
        print('Tu respuestas es incorrecta, tu numero es mayor al numero secreto')
        intentos += 1
    elif numero_elegido == numero_programa:
        print(f'Ganaste en {intentos} intentos')
        break
        intentos += 1
if numero_elegido != numero_programa:
    print('Lo siento, se han agotado los intentos')


# SOLUCION DEL PROFE

# intentos = 0
# estimado = 0
# numero_secreto = randint(1,100)
# nombre = input("Dime tu nombre: ")
#
# print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes 8 intentos para adivinar")
#
# while intentos < 8:
#     estimado = int(input("Cuál es el número?: "))
#     intentos += 1
#
#     if estimado < numero_secreto:
#         print("Mi numero es mas alto")
#     elif estimado > numero_secreto:
#         print("Mi numero es mas bajo")
#     else:
#         print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
#         break
#
# if estimado != numero_secreto:
#     print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")