palavras = ('batata', 'gato', 'tomada', 'violao', 'porta', 'armario', 'carro', 'jabuticaba')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais = ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
    print()