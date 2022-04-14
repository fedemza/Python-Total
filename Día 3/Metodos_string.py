texto = 'Este es el texto de Federico'

resultado = texto.upper()
resultado1 = texto.lower()
resultado2 = texto[2].upper()
resultado3 = texto.split()
resultado4 = texto.split('t')
resultado5 = ' '.join(['aprender', 'python', 'es', 'genial']) # lo que va antes del punto es lo que vamos a usar para unir la lista
resultado6 = texto.find('l')
resultado7 = texto.find('g') # La diferencia entre find e index es que cuando find no encuentra devuelve -1 e index devuelve error
resultado8 = texto.replace('e','x')
resultado9 = texto.replace('Federico','todos')


print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)