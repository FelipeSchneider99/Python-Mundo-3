valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Voce digitou os valores {valores}')

menor = min(valores)
maior = max(valores)

print(f'O menor valor foi {menor} nas posições ', end ='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'[{i}]...', end=' ')
print()
print(f'O maior valor foi {maior} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'[{i}]...', end=' ')
print()
