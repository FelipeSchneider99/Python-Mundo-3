valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        print('Valor adicionado com sucesso')
        valores.append(num)
    elif num in valores:
        print('Valor duplicado! Não vou adicionar')

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

valores.sort()
print(f'Voce digitou os valores {valores}')