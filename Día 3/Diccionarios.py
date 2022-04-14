diccionario = {'c1':'valor1', 'c2':'valor2'} #las claves no pueden repetirse pero los valores si
print(type(diccionario))
print(diccionario)
diccionario['c3'] = 'valor3' #agrego una clave al diccionario
print(diccionario)
diccionario[4] = {'s1': 1, 's2': [1,2,'tres']} #agrego una clave al diccionario
print(diccionario)
diccionario['c3'] = 'nuevoValor' #sobreescribo
print(diccionario)
print(diccionario.keys())#para conocer todas las claves de un diccionario
print(diccionario.values())#para conocer todos las valores de un diccionario
print(diccionario.items())#para conocer todo lo de un diccionario

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'Juan','apellido':'Fuentes','peso':88, 'talla':1.76, 'mascotas':['Lali','Pongo']} #los valores tambien pueden ser listas o diccionarios
print(cliente['talla'])
print(cliente['mascotas'][1])

