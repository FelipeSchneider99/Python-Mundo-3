from datetime import datetime
clt = dict()
ano_atual = datetime.now().year

clt['nome'] = str(input('Nome: ')).strip().title()
clt['idade'] = ano_atual - int(input('Ano nascimento: '))
clt['ctps'] = int(input('CTPS(0 se não tem): '))
if clt['ctps'] != 0:
    clt['ano_contratacao'] = int(input('Ano de contratação: '))
    clt['salario'] = float(input('Salario: R$'))
    clt['aposentadoria'] = (clt['ano_contratacao'] + 35 - ano_atual) + clt['idade']

print('-=' * 30)
print(clt)
for k, v in clt.items():
    print(f'  - {k} tem o valor {v}')
