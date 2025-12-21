
gols = list()
jogador = dict()
jogador['nome'] = input('Nome do Jogador: ').strip().capitalize()
partidas = int(input('Quantas partidas: '))
total = 0
for i in range(partidas):
    jogador['gols'] = int(input(f'Quantidade de gols na partida {i+1}: '))
    gols.append(jogador['gols'])
    total += jogador['gols']
jogador['gols'] = gols[:]
jogador['total'] = total
print('=' * 50)
print(jogador)
print('=' * 50)
for k, v in jogador.items():
    print(f'  - O campo {k} tem o valor {v}')
print('=' * 50)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for partida in range(0, partidas):
    print(f'=> Na partida {partida + 1}, fez {gols[partida]} gols.')
print('=' * 50)
print(f'Foi um total de {total} gols.')


