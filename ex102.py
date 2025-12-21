def factorial (num, show=False):
    """
    Calcula o Fatorial de um número
    :param num: O numero a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um numero num.
    """
    fact = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        fact *= c
    print(fact)
    return fact


#PROGRAMA PRINCIPAL
factorial(5)
factorial(4, show=True)
