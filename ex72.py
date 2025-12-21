num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num_usuario = int(input('Digite um numero entre 0 e 20: '))
    if num_usuario < 0 or num_usuario > 20:
        print('Tente novamente.', end=' ')
        continue
    else:
        print(f'Voce digitou o numero {num[num_usuario]}')
        break
