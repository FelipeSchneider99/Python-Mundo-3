from time import sleep

def contador(ini, fi, pas):
    if pas == 0:
        pas = 1
    if ini >= fi and pas > 0:
        pas = pas * -1
    print('-' * 40)
    print(f'Contagem de {ini} até {fi} de {abs(pas)} em {abs(pas)}')
    if pas > 0:
        for ini in range(ini, fi + 1, pas):
            print(f'{ini}', end=' ')
            sleep(0.3)
        print()
    else:
        for ini in range(ini, fi - 1, pas):
            print(f'{ini}', end=' ')
            sleep(0.3)
        print()

contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
