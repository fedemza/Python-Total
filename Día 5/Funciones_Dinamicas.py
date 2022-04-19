def chequear_3_cifras(lista):
    '''Chequea si hay  numeros de 3 cifras en  una lista y los devuelve
    en una lista'''
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([10,18,1985])
print(resultado)
resultado2 = chequear_3_cifras([585999,584,8492,635])
print(resultado2)