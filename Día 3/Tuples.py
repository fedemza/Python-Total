tuple = (1,2,3,4) #Tambien se puede hacer sin los parentesis pero lo mas comun es con los parentesis
print(type(tuple))
print(tuple[1])
print(tuple[-2])
#Los tuples no soportan asignacion de items

tuple2 = (1,2,(3,5),4)
print(tuple2[2])
print(tuple2[2][0])

list = list(tuple2) # convierto el tuple a lista
print(type(list))
print(list)

t = (1, 2, 1)
x, y, z = t    # Tiene que se la misma cantidad de variables que valores. Tambien se puede hacer con listas y dicionarios
print(x, y, z)

print(len(t))
print(t.count(1)) # Las veces que aparece 1
print(t.index(2)) #posicion en la que esta 2