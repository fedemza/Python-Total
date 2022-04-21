from pathlib import Path

base = Path.home()
guia = Path(base, 'Europa', 'España',Path('Barcelona', 'Sagrada_Familia.txt'))
guia2 = guia.with_name('La_pedrera.txt')
print(base)
print(guia)
print(guia2)
print(guia.parent)
print(guia.parent.parent)