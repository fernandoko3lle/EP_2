def valida_questao(dic_entrada): 
    dic_saida = {}
    for chave, valor in dic_entrada.items():
        if chave not in('titulo', 'nivel', 'opcoes', 'correta'):
            dic_saida[chave] = 'nao_encontrado'
        if len(dic_entrada.keys()) != 4:
            dic_saida['outro'] = 'numero_chaves_invalido'
        if dic_entrada['titulo'] == '' or dic_entrada['titulo'] == ' ':
            dic_saida['titulo'] = 'vazio'
        if dic_entrada['nivel'] not in('facil', 'medio', 'dificil'):
            dic_saida['nivel'] = 'valor_errado'
        if len(dic_entrada['opçoes'].keys()) == 4:
            for opçao in 'opçoes'.keys():
                if opçao not in('A', 'B', 'C', 'D'):
                    dic_saida['opçoes'] = 'chave_invalida_ou_nao_encontrada'
                    if opçao == '' or opçao == ' ':
                        'opçoes'[opçao] = 'vazia'  
        else: 
            dic_saida['opcoes'] = 'tamanho_invalido'
        if 'correta' not in('A', 'B', 'C', 'D'):
            dic_saida['correta'] = 'valor_errado'
            


        

        
        


             

        
                            
                            
                            

