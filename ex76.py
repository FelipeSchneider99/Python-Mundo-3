compras = ('Água mineral', 0.99, 'Vibrador Golfinho', 19.90, 'Whey Bar', 6, 'Protetor Solar NIVEA', 67.10)
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)

for produto in range(0, len(compras), 2):
    print(f'{compras[produto]:.<42}R$ {compras[produto+1]:5.2f}')

print('-'*50)