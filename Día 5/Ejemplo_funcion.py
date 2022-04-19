precios_cafe = [('capuchino',1.50),('expresso',2.20),('moka',1.90)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El cafe mas caro es el {cafe} con un precio de {precio} dólares')