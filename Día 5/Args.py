def suma(*args): # Con *args le puedo pasar numero indefinido de argumentos
   return sum(args)

print(suma(5,6,5,4))

def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma += n**2
    return suma

print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    return suma

print(suma_absolutos(-5,5,10,-5,-15))

def numeros_persona(nombre,*args):
    return f'{nombre}, la suma de tus numeros es {sum(args)}'

print(numeros_persona('Pedro',-5,5,10,-5,-15))