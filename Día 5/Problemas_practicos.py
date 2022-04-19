# 1- Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.

def devolver_distintos(a,b,c):
    suma = a+b+c


    lista = [a,b,c]
    lista.sort()

    if suma > 15:
       return lista[2]
    elif suma < 10:
        return lista[0]
    else:
        return lista[1]

print(devolver_distintos(2,1,6))

# 2- Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido"
# , debería devolver ['d','e','i','n','o','r','t']

def ordenar_letras(string):
    lista = []
    for letra in string:
        lista.append(letra)

    lista = set(lista)
    lista = list(lista)
    lista.sort()
    return lista

print(ordenar_letras('entretenido'))


# 3-  Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def doble_cero(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False
print(doble_cero(5,6,1,0,0,9,3,5))
print(doble_cero(6,0,5,1,0,3,0,1))
print(doble_cero(6,0,5,1,0,3,0,0))

# 4- Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números
# primos hay en el rango que va desde cero hasta ese número
# incluido, y va a devolverla cantidad de números primos que
# encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos

def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero  < 2 :
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return(len(primos))

print(contar_primos(50))




