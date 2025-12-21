def leia_int(msg):
    """
    Programa de validação que aceita apenas valores numericos inteiros
    :param msg: "input" do usuario
    :return: retorna o valor do usuario
    """
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return num

#PROGRAMA PRINCIPAL
num_valido = leia_int('Digite um número: ')
print(f'Voce acabou de digitar o numero {num_valido}')
