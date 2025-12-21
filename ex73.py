serie_a = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 'Vasco', 'Bragantino',
               'Grêmio', 'Ceará', 'Corinthians', 'Atlético Mineiro', 'Internacional', 'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')

while True:
    print('[1] Classificados para Libertadores'
          f'\n[2] Zona de Rebaixamento'
          f'\n[3] Times em Ordem Alfabética'
          f'\n[4] Em qual posição está o Grêmio'
          f'\n[5] Sair do Programa')
    escolha_usuario = int(input('Opção: '))
    if escolha_usuario == 1:
        print('=-' * 20)
        print('G-4 da série A')
        print('=-' * 20)
        for times in serie_a[:4]:
            print(times)
        print('=-' * 20)
    elif escolha_usuario == 2:
        print('=-' * 20)
        print('Zona de Rebaixamento')
        print('=-' * 20)
        for times in serie_a[-4:]:
            print(times)
        print('=-' * 20)
    elif escolha_usuario == 3:
        print('=-' * 20)
        print('Times da série A em Ordem Alfabética')
        print('=-' * 20)
        for times in (sorted(serie_a)):
            print(times)
        print('=-' * 20)
    elif escolha_usuario == 4:
        print('=-' * 20)
        print('Em qual posição se encontra o Grêmio')
        print('=-' * 20)
        print(f'O Grêmio se encontra na {serie_a.index('Grêmio') + 1}ª posição da tabela')
        print('=-' * 20)
    elif escolha_usuario == 5:
        print('=-' * 20)
        print('Finalizando o programa...')
        print('=-' * 20)
        break
    else:
        print('Opção inválida')
