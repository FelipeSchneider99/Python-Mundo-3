boletim = []
while True:
    nome = (str(input('Nome: ')).strip().capitalize())
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = ((nota1 + nota2) / 2)
    boletim.append([nome, [nota1, nota2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja cadastrar as notas curriculares de outro aluno?[S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('-='*30)
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*26)
for pos, cont in enumerate(boletim):
    print(f'{pos:<4} {cont[0]:<10} {cont[2]:>8.1f}')
while True:
    print('-'*30)
    aluno_notas = int(input('Mostrar as notas de qual aluno?(999 para interromper o programa) '))
    if aluno_notas == 999:
        break
    if aluno_notas <= len(boletim) - 1:
        print(f'Notas de {boletim[aluno_notas][0]} são {boletim[aluno_notas][1]}')



