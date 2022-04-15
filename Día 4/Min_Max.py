menor = min(35,48,58,96,54,25,10)
mayor = max(35,48,58,96,54,25,10)

print(menor)
print(mayor)

lista = [35,48,58,96,54,25,99]
print(max(lista))

nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres)) #Trae el que esta primero en orden alfabetico

nombre = 'Carlos'
print(min(nombre)) #primero busca en las mayusculas y despues en las minusculas

nombre = 'carlos'
print(min(nombre))

dic = {'c1':10, 'c2':9, 'b1':11, 'c3':15 }
print(min(dic))
print(min(dic.values()))
