palavras = ('batata', 'gato', 'tomada', 'violao', 'porta', 'armario', 'carro', 'jabuticaba')

for palavra in palavras:
    vogais = []
    print(f'Na palavra {palavra.upper()} temos as vogais =', end = ' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU' and letra.upper() not in vogais:
            vogais.append(letra.upper())
    print(vogais, end = ' ')

    print()