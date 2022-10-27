def valida_questao(Questão): 
    Validação = {}
    for chave in ('titulo', 'nivel', 'opcoes', 'correta'):
        if chave not in Questão:
            Validação[chave] = 'nao_encontrado'
    if len(Questão.keys()) != 4:
        Validação['outro'] = 'numero_chaves_invalido'
    if 'titulo' in Questão: 
        if Questão['titulo'].strip() == '':
            Validação['titulo'] = 'vazio'
    if 'nivel' in Questão:
        if Questão['nivel'] not in ('facil', 'medio', 'dificil'):
            Validação['nivel'] = 'valor_errado'
    if 'opcoes' in Questão:
        if len(Questão['opcoes'].keys()) == 4:
            for opçao, resposta in Questão['opcoes'].items():
                if opçao in('A', 'B', 'C', 'D'):
                        if resposta.strip() == '':
                            if 'opcoes' not in Validação:
                                Validação['opcoes'] = {}
                                Validação['opcoes'][opçao] = 'vazia'
                            else:
                                Validação['opcoes'][opçao] = 'vazia'
                else:
                    Validação['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else: 
            Validação['opcoes'] = 'tamanho_invalido'
    if 'correta' not in Validação:
        if Questão['correta'] not in ('A', 'B', 'C', 'D'):
            Validação['correta'] = 'valor_errado'
    return Validação

print(valida_questao({
  'titulo': 'Qual o resultado da operação 57 + 32?',
  'nivel': 'moleza',
  'opcoes': {'A': '  ', 'B': '85', 'C': '89', 'D': '\t'}
}))



             

        
                            
                            
                            

