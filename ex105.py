def notas(*nums, situacao=False):
    """
    Programa que recebe varias notas de alunos e retorna um dicionario com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
    :param nums: notas dos alunos
    :param situacao: True/False, indica se deve adicionar a situacao
    :return: dicionario com a analise da turma
    """
    nota = dict()
    if not nums:
        return {'total': 0, 'maior': 0, 'menor': 0, 'media': 0, 'situacao': ''}

    nota['total'] = len(nums)
    nota['maior'] = max(nums)
    nota['menor'] = min(nums)
    nota['media'] = round(sum(nums) / len(nums), 2)

    if situacao:
        if nota['media'] >= 7:
            nota['situacao'] = 'BOA'
        elif nota['media'] >= 5:
            nota['situacao'] = 'RAZOAVEL'
        else:
            nota['situacao'] = 'RUIM'
    return nota


resp = notas(3.5, 2.56, 6.5, 7, 4)
print(resp)
help(notas)