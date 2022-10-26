def valida_questao(dic_entrada): 
    dic_saida = {}
    for chave in ('titulo', 'nivel', 'opcoes', 'correta'):
        if chave not in dic_entrada:
            dic_saida[chave] = 'nao_encontrado'
    if len(dic_entrada.keys()) != 4:
        dic_saida['outro'] = 'numero_chaves_invalido'
    if dic_entrada['titulo'].strip(' ') == '':
        dic_saida['titulo'] = 'vazio'
    if dic_entrada['nivel'] not in ('facil', 'medio', 'dificil'):
        dic_saida['nivel'] = 'valor_errado'
    if len(dic_entrada['opcoes'].keys()) == 4:
        for opçao in dic_entrada['opcoes'].keys():
            if opçao not in('A', 'B', 'C', 'D'):
                dic_saida['opçoes'] = 'chave_invalida_ou_nao_encontrada'
                if opçao == '' or opçao == ' ':
                    dic_entrada['opcoes'][opçao] = 'vazia'  
    else: 
        dic_saida['opcoes'] = 'tamanho_invalido'
    if 'correta' in dic_entrada and dic_entrada['correta'] not in ('A', 'B', 'C', 'D'):
        dic_saida['correta'] = 'valor_errado'
    return dic_saida


        

        
        


             

        
                            
                            
                            

