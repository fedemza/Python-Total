nombre = input('Nombre: ')
ventas = float(input('Ventas: '))
comision = round(ventas*0.13,2)

print(f'Ok {nombre}, este mes ganaste ${comision} en comisiones')