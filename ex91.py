from random import randint
from time import sleep
from operator import itemgetter
jogadores = list()
pessoa = dict()
ranking = list()
for contador in range(1, 5):
    pessoa['nome'] = str(input('Nome do Jogador: ')).title()
    print('Rolando o dado...')
    sleep(1)
    pessoa['num_dados'] = randint(1, 6)
    jogadores.append(pessoa.copy())
ranking = sorted(jogadores, key=itemgetter('num_dados'), reverse=True)
#lista 'ranking'
#key=itemgetter('num_dados'): diz para ordenar usando o valor da chave 'num_dados'
#reverse=True: ordena do maior para o menor
print('-='*20)
for jogador in jogadores:
    print(f'O {jogador['nome']} tirou {jogador['num_dados']} no dado.', end = ' ')
    print()
print('-=' * 20)
print('Ranking dos jogadores')
for i, jogador in enumerate(ranking):
# enumerate() nos dá o índice (para a posição) e o valor (o dicionário do jogador)
    print(f'{i+1}º Lugar: {jogador["nome"]} com {jogador["num_dados"]}')


