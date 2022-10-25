def transforma_base(lista):
    dic_nivel = {}
    for Q in lista:
        for chave, valor in Q.items():
            if chave == 'nivel':
                if valor in dic_nivel:
                    dic_nivel[valor].append(Q)
                else:
                    dic_nivel[valor] = [Q]
    return dic_nivel 