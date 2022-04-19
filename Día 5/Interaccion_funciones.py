from random import *
 # Lista inicial
palitos = ['-','--','---','----']

 # mezclar palitos
def mezclar(lista):
    shuffle(palitos)
    return lista

 # pedirle intento
def probar_suerte():
     intento = ''
     while intento not in ['1','2','3','4']:
         intento = input('Elige un numero del 1 al 4: ')
     return int(intento)

 # comprobar intento
def chequear_intento(lista,intento):
     if lista[intento - 1] == '-':
         print(' A lavar los platos')
     else:
         print('Esta vez te has salavado')

     print(f'Te ha tocado {lista[intento - 1]}')


# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados,seleccion)

def lanzar_dados():
    dado1 = [1, 2, 3, 4, 5, 6]
    dado2 = [1, 2, 3, 4, 5, 6]

    resultado1 = choice(dado1)
    resultado2 = choice(dado2)

    return (resultado1,resultado2)

def evaluar_jugada(n1,n2):
    if (n1 + n2 <=6):
        return (f'La suma de los resultados que son {n1} y {n2} es menor o igual a 6')
    else:
        return (f'La suma de los resultados que son {n1} y {n2} es mayor a 6')


# n1, n2 = lanzar_dados()
# print (evaluar_jugada(n1,n2))

def reducir_lista(lista_numeros):
    nueva_lista = []
    for n in lista_numeros:
        if n  not in nueva_lista:
            nueva_lista.append(n)
    nueva_lista.sort()
    nueva_lista.pop()
    return nueva_lista

def promedio(lista_numeros):
    suma = sum(lista_numeros)
    promedio = suma/len(lista_numeros)
    return promedio

lista_reducida  = reducir_lista([5,5,10,15,15])
print(promedio(lista_reducida))

lista_numeros = [1,2,15,7,2,8]


def lanzar_moneda():
    resultado = choice(["Cara", "Cruz"])
    return resultado


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista

resultado_moneda = lanzar_moneda()

print(probar_suerte(resultado_moneda,lista_numeros))