pessoa = dict()
banco = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ').upper().strip()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    banco.append(pessoa.copy())
    while True:
        resposta = str(input('Deseja adicionar outra pessoa?[S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resposta == 'N':
        break
# for pessoa in banco:
#     if isinstance(pessoa,dict):
#         soma += pessoa.get('idade', 0)
media = soma / len(banco)
print(banco)
#A - Quantas pessoas foram cadastradas
print(f'{len(banco)} pessoas cadastradas')
#B - A media de idade do grupo
print(f'B) A média de idade é de {media:5.2f} anos.')
#C - Uma lista com todas as mulheres
print(f'C) As mulheres cadastradas foram ', end= ' ')
for p in banco:
    if p['sexo'] == 'F':
        print(f'{p["nome"]},', end=' ')
print()
#D - Uma lista com todas as pessoas com idade acima da média
print(f'D) Lista de pessoas que estão acima da média:')
print()
for p in banco:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< ENCERRADO >>')
