# Aplicar a função de descontos usando o map()

lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)

#listaDesconto = list(map(lambda x: x * (1 - 0.1), lista))
listaDesconto = list(map(lambda x: desconto(x), lista))

print(listaDesconto)