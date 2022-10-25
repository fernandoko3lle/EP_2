def valida_questao(dic_entrada): 
    dic_saida = {}
    if ('titulo', 'nivel', 'opcoes', 'correta') in dic_saida.keys():
        if len(dic_saida.keys()) == 4:
            if 'titulo' != '' and 'titulo' != ' ':
                if 'nivel' in ('facil', 'medio', 'dificil'):
                    if len('opções'.values()) == 4:
                        if ('A', 'B', 'C', 'D') in 'opções'.keys():
                            
                            

