#Retornar os valores maiores que 100.

lista = [100, 248.90, 88, 124.90]

lista100 = list(filter(lambda x: (x > 100), lista))

print(lista100)
