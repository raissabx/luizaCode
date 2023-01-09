# Somar todos os valores da lista usando reduce()
from functools import reduce

lista = [100, 248.90, 88, 124.90]
soma = reduce(lambda x, y: x+y, lista)
print(soma)
