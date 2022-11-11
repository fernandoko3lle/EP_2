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
def valida_questoes(questoes):
    lista_validada = []
    for i in questoes:
        val = valida_questao(i)
        lista_validada.append(val)
    return lista_validada


print(valida_questoes([{'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?', 'nivel': 'moleza', 'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'}, 'correta': 'A'}, {'titulo': 'Einstein foi Nobel de física em qual ano?', 'nivel': 'dificil', 'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'}, 'correta': 'D'}, {'titulo': 'Qual a capital do Brasil?', 'nivel': 'facil', 'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'}, 'correta': 'A'}, {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?', 'nivel': 'medio', 'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'}, 'correta': 'C'}, {'titulo': 'Qual destas não é uma linguagem de programação?', 'nivel': 'facil', 'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'}, 'correta': 'A'}]))



