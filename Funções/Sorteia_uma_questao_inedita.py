import random
def sorteia_questao(dic_questoes, nivel):
    return random.choice(dic_questoes[nivel])
def sorteia_questao_inedida(dic_questoes, nivel, sort): 
    q_sort = sorteia_questao(dic_questoes, nivel)
    while q_sort in sort:
        q_sort = sorteia_questao(dic_questoes, nivel)
    sort.append(q_sort)
    return q_sort

