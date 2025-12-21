def voto(ano_nasc):
    """
        Função para verificar a situação de voto de uma pessoa com base no ano de nascimento.
        Retorna uma string com a idade e a situação.
    """
    import datetime
    idade = datetime.datetime.now().year - ano_nasc
    if idade < 16:
        return f'Com {idade} anos. VOTO NEGADO!'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos. VOTO OPCIONAL'
    else:
        return f'Com {idade} anos. VOTO OBRIGATORIO'


#PROGRAMA PRINCIPAL
nascimento = (int(input('Em que ano você nasceu? ')))
print(voto(nascimento))