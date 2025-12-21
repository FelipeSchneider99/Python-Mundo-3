lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resposta = '    '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper()
    if resposta == 'N':
        break


print('-='* 30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de: {menor}Kg. Peso de ', end= '')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')