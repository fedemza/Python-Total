mi_texto = 'Esta es una prueba'
resultado = mi_texto[-4] # pueden ser positivos o negativos los indices. El primero es siempre 0
indice = mi_texto.index('e',8,16) # Se pueden buscar letras o o substring. 2do y 3er argumentos opcionales desde donde hasta donde
indicer = mi_texto.rindex('u') # igual que el index pero busca al reves. De derecha a izquierda

print(resultado)
print(indice)
print(indicer)