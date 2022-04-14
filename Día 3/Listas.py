mi_lista = ['a','b','c',5]
mi_lista2 = ['d', 'e','f']
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[1])
print(mi_lista[1:3])
print(mi_lista[1:])
print(mi_lista+mi_lista2)

mi_lista2[0] = 'alfa' #en las lista puedo reemplazar elementos. En los strings no
print(mi_lista2)

mi_lista.append('g')
print(mi_lista)

eliminado = mi_lista.pop(1) #si lodejamos vacio elimina el ultimo elemento. Sino elimina el elemento del indice que se paso por argumentos
print(mi_lista)
print(eliminado)

lista3 = ['g','a','k','d','o','f']
lista3.sort() #ordena la lista. El metodo sort no devuelve nada(por lo tanto no lo podemos almacenar en una variable). Modifica la lista original
print(lista3)
lista3.reverse() # Da vuelta el orden
print(lista3)


