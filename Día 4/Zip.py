nombres = ['Ana', 'Hugo', 'Valeria']
edades = [25, 32, 28,35]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades)) #zip llega hasta el largo de la lista mas corta

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')
