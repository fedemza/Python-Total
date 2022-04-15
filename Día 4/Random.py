from random import *  #importa todos los metodos de esa libreria

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5),1) #Tira un valor decimal aleatorio dentro del rango
print(aleatorio)

aleatorio = random() # Decimal entre 0 y 1
print(aleatorio)

colores = ['Azul', 'Rojo', 'Verde', 'Violeta']
aleatorio = choice(colores) # elige un elemento aleatorio de la lista
print(aleatorio)

numeros = list(range(5,55,5))
shuffle(numeros) #Mezcla los elementos de la lista
print(numeros)