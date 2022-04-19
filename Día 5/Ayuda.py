dic = {'Clave1': 100, 'Clave2': 500}

a = dic.popitem() # si pongo el cursor sobre el método me dice que hace
print(a)
print( dic)

#practicas

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(texto.lstrip(",:%_#"))
print(texto)
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#").lstrip())
print(texto.lstrip(",:_#%"))
print('www.example.com'.lstrip('cmowz.'))

#añade naranja como 4to elemento de la lista
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

# Analiza si los setsforman conjuntos aislados,es decir, no tienen elementos en comun
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

