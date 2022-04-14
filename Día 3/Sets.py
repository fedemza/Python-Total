#Los sets solo admiten elementos únicos. No se le pueden poner elementos repetidos
#Los elementos del set no tienen índices
#Dentro de los sets no se pueden incluir listas y diccionarios. Si admiten tuplas
set = set([1,2,3,4,5])
print(type(set))
print(set)

set2 = {7, 8, 9, 10, 11}
print(type(set2))
print(set2)
print(len(set2))
print(7 in set2)

set3 = {7, 8, 9, (10, 11), 7, 8, 7, 7}
print(set3) #Si hay elementos repetidos en el set Python los elimina

s1 = {1, 2 ,3}
s2 = {3, 4 ,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
print(s1)
s1.remove(3)
s1.discard(9) # Igual que el .remove() solo que si el elemento no existe no me va a dar error
print(s1)
s2.pop() # elimina un elemento aleatorio.
print(s2)
s2.clear() # Vacia nuestro set
print(s2)