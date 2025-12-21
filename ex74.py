from random import randint
lista = []
# numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for i in range (5):
    numero = randint(1, 100)
    lista.append(numero)
numeros_tupla = tuple(lista)
print(f'Números gerados: {numeros_tupla}')
print(f'O menor número gerado na tupla foi {min(numeros_tupla)}')
print(f'O maior número gerado na tupla foi {max(numeros_tupla)}')