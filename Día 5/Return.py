def multiplicar(num1,num2):
    return num1*num2

resultado = multiplicar(5,10)
print(resultado)



palabra = 'Python'
def invertir_palabra(palabra):
    '''Invierte la palabra y la pine en mayusculas'''
    palabra = palabra[::-1].upper()
    return palabra
print(invertir_palabra('python'))