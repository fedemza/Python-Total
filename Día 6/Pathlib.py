from pathlib import Path, PureWindowsPath
archivo = Path('C:/Users/fedev/OneDrive/Escritorio/Python/Día 6/Prueba.txt')

ruta_windows = PureWindowsPath(archivo)
print(ruta_windows)

# print(archivo.read_text())
# print(archivo.name)
# print(archivo.suffix)
# print(archivo.stem)

if not archivo.exists():
    print('El archivo no existe')
else:
    print('El archivo si existe')