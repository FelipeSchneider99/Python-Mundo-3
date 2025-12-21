lista = []
lista_pares = []

for i in range(4):
    num = int(input('Digite um número: '))
    lista.append(num)

lista_tupla = tuple(lista)
for i in lista_tupla:
    if i % 2 == 0:
        lista_pares.append(i)
pares_tupla = tuple(lista_pares)

print(f'Você digitou os valores {lista_tupla}')
print(f'O valor 9 apareceu {lista_tupla.count(9)} vezes')
if 3 in lista_tupla:
    print(f'O número 3 se encontra na posição {lista_tupla.index(3)}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
    print(f'Os valores pares digitados foram:', end=' ')
for i in pares_tupla:
    print(i, end=' ')
