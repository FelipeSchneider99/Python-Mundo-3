from random import randint
from time import sleep

def sorteia():
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for num in range(5):
        lista.append(randint(1, 10))
        print(f'{lista[num]}', end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar():
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')



lista = list()
sorteia()
somaPar()

