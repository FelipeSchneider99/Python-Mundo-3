def areaTerreno():
    print('-' * 20)
    print('Controle de Terrenos')
    print('-' * 20)
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    area = a * b
    print(f'A área de um terreno de {a}x{b} é de {area:.1f}m².')

areaTerreno()