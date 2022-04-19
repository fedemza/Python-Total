def suma(**kwargs): # para pasar diccionarios
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total


print(suma(x=3, y=5, z=2))

def prueba(num1,num2,*args,**kwargs): # si pasamos arguementos y *args y **kwargs hay que ponerlos en ese orden

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')
    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [100,200,300,400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}
prueba(15,50,*args,**kwargs)