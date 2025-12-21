from random import randint
from time import sleep

jogos_mega = []
lista_palpites = []
jogos = int(input('Quantos jogos serão gerados? '))

for i in range(jogos):
    for j in range(6):
        numero_gerado = randint(1, 60)
        while numero_gerado in lista_palpites:
            numero_gerado = randint(1, 60)
        if numero_gerado not in lista_palpites:
            lista_palpites.append(numero_gerado)
    lista_palpites.sort()
    jogos_mega.append(lista_palpites[:])
    lista_palpites.clear()

print('-=' * 20)
print(f'{"JOGOS DA MEGASENA":^40}')
print('-=' * 20)
for cont in range(jogos):
    print(f'Jogo {cont + 1}: {jogos_mega[cont]}')
    sleep(0.7)
