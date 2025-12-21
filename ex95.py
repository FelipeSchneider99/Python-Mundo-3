time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ').strip().title()
    partidas = int(input('Quantas partidas: '))
    total = 0
    gols.clear()
    for i in range(partidas):
        jogador['gols'] = int(input(f'Quantidade de gols na partida {i+1}: '))
        gols.append(jogador['gols'])
        total += jogador['gols']
    jogador['gols'] = gols[:]
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resposta in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
#---output
print('=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for dado in v.values():
        print(f'{str(dado):<15}', end=' ')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para encerrar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, gols in enumerate(time[busca]["gols"]):
            print(f' - Na partida {i+1} fez {gols} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')