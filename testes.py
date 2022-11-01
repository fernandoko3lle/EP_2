import random
def sorteia_questao(quest, nivel):
    lista_possiveis = []
    for i in quest:
        if i['nivel'] == nivel:
            lista_possiveis.append(i)
    return random.choice(lista_possiveis)

print(sorteia_questao([{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'medio',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'}], 'medio'))