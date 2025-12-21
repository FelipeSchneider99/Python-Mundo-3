def ficha(nome, gols):
    """
    Programa que mostra o nome do jogador e a quantidade de gols
    :param nome: Nome do jogador
    :param gols: Quantidade de gols
    :return: A ficha do jogador
    """
    linha_div = '-'*50
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        qnt_gols = int(gols)
    else:
        qnt_gols = 0
    dados_jogador = f'O jogador {nome} fez {qnt_gols} gol(s) no campeonato.'
    ficha_comp = (f"{linha_div}"
                  f"\n{dados_jogador}")
    return ficha_comp


#PROGRAMA PRINCIPAL
print('-'*50)
jogador = ficha((input('Digite o nome do jogador: ')),
                 (input('Quantidade de gols: ')))
print(jogador)

