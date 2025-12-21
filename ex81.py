lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Voce digitou {len(lista)} valores')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 se encontra na lista')
else:
    print('O valor 5 não se encontra na lista')