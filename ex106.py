from time import sleep

def help_sys():
    """
    Simula um sistema de ajuda interativo (PyHelp).

    O programa fica em loop, solicitando ao usuário o nome de uma
    função ou biblioteca Python. Então exibe a docstring desse comando usando a função help() interna.
    O loop encerra quando o usuário digita 'fim'.
    """
    while True:
        print('~' * 30)
        print('SISTEMA DE AJUDA PyHELP'.center(30))
        print('~' * 30)
        opc = input('Função ou Biblioteca > ').strip().lower()
        sleep(0.5)
        if opc == 'fim':
            print('~'*30)
            print('ATÉ LOGO!'.center(30))
            print('~'*30)
            break
        else:
            print('~'*40)
            print(f'Acessando o manual do comando {opc}'.center(40))
            print('~'*40)
            sleep(0.5)
            help(opc)
help_sys()
