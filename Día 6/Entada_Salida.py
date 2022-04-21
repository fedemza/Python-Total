mi_archivo = open('prueba.txt')

# print(mi_archivo.read())

# for linea in mi_archivo:
#     print('Aqui dice: ' + linea)


todas = mi_archivo.readlines()
print(todas)
una_linea = mi_archivo.readline()

print(una_linea.upper())

una_linea = mi_archivo.readline()

print(una_linea.rstrip())


una_linea = mi_archivo.readline()

print(una_linea)