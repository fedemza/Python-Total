import os
from pathlib import Path
archivo = Path('C:/Users/fedev/OneDrive/Escritorio/Python/Día 6/Prueba.txt')
mi_archvio = open(archivo)
print(mi_archvio.read())


ruta = os.getcwd() # para saber en que ruta estamos
ruta_actual = 'C:\\Users\\fedev\\OneDrive\\Escritorio\\Python\Día 6\\.Prueba.txt'
elemento1 = os.path.basename(ruta_actual)
elemento2 = os.path.dirname(ruta_actual)
elemento3 = os.path.split(ruta_actual) # recibo ambos elementos en una tupla
# print(elemento1)
# print(elemento2)
# print(elemento3)

nueva_ruta = os.chdir('C:\\Users\\fedev\\OneDrive\\Escritorio\\Python\\Teoria') #para cambiar de directorio
archivo = open('prueba.txt','r')

# print(ruta)
# print(archivo.read())

# nueva_ruta2 = os.mkdir('C:\\Users\\fedev\\OneDrive\\Escritorio\\Python\\Teoria\\Otra') # Crear un nuevo directorio
# os.rmdir('C:\\Users\\fedev\\OneDrive\\Escritorio\\Python\\Teoria\\Otra') # Eliminar carpetas

