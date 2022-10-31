import random
def sorteia_questao(dic_questoes, nivel):
    return random.choice(dic_questoes[nivel])
def sorteia_questao_inedida(dic_questoes, nivel, sort): 
    c = 0 
    for q, r in dic_questoes.items():
        if q == nivel:
            if r[c] not in sort:
                q_sort = sorteia_questao(dic_questoes, nivel)
                sort.append(q_sort)
            c += 1
    return q_sort

