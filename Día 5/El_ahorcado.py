from random import choice

palabras = ['iofi','trufa', 'piedra','auto','gato','montaña','mendoza','cordoba']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_secreta = choice(palabras)
    letras_unicas = len(set(palabra_secreta))

    return palabra_secreta, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input('Elige una letra: ')
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print(' No has elegido una letra correcta')
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print('La palabra era ' + palabra )
    return True

def ganar(palabra_decubierta):
    mostrar_nuevo_tablero(palabra_decubierta)
    print('Felicitaciones, has encontrado la palabra')
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*'*20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas) )
    print(f'Vidas:   {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado