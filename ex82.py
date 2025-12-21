lista = []
lista2 = []
lista3 = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista2.append(valor)
    if valor % 2 == 1:
        lista3.append(valor)

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break

print(f'A lista completa é {lista}')
print(f'Os numeros pares da lista: {lista2}')
print(f'Os numeros impares da lista: {lista3}')