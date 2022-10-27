def valida_questao(dic_entrada): 
    dic_saida = {}
    for chave in ('titulo', 'nivel', 'opcoes', 'correta'):
        if chave not in dic_entrada:
            dic_saida[chave] = 'nao_encontrado'
    if len(dic_entrada.keys()) != 4:
        dic_saida['outro'] = 'numero_chaves_invalido'
    if 'titulo' in dic_entrada: 
        if dic_entrada['titulo'].strip() == '':
            dic_saida['titulo'] = 'vazio'
    if 'nivel' in dic_entrada:
        if dic_entrada['nivel'] not in ('facil', 'medio', 'dificil'):
            dic_saida['nivel'] = 'valor_errado'
    if 'opcoes' in dic_entrada:
        if len(dic_entrada['opcoes'].keys()) == 4:
            for opçao, resposta in dic_entrada['opcoes'].items():
                if opçao in('A', 'B', 'C', 'D'):
                        if resposta.strip() == '':
                            if 'opcoes' not in dic_saida:
                                dic_saida['opcoes'] = {}
                                dic_saida['opcoes'][opçao] = 'vazia'
                            else:
                                dic_saida['opcoes'][opçao] = 'vazia'
                else:
                    dic_saida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else: 
            dic_saida['opcoes'] = 'tamanho_invalido'
    if 'correta' not in dic_saida:
        if dic_entrada['correta'] not in ('A', 'B', 'C', 'D'):
            dic_saida['correta'] = 'valor_errado'
    return dic_saida



             

        
                            
                            
                            

