# IMPORTAÇÕES
import random

# LIB QUEST
quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

#VARIAVEIS GLOBAIS
sort = []

# NIVEIS   
niveis = {
    0: "facil",
    1: "médio",
    2: "dicícil",
}

# FUNÇÕES 
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
def questao_para_texto(dic_questao, id):
  return ''' ----------------------------------------
QUESTAO {0}

{1}

ALTERNATIVAS:
A: {2}
B: {3}
C: {4}
D: {5}
'''.format(id,dic_questao['titulo'],dic_questao['opcoes']['A'],dic_questao['opcoes']['B'], dic_questao['opcoes']['C'], dic_questao['opcoes']['D'])
def gera_ajuda(questao):
    l_respostas_erradas = []
    dica = []
    correta = questao['correta']
    dic_questoes = questao['opcoes']
    for r in dic_questoes.values():
        if r != dic_questoes[correta]:
            l_respostas_erradas.append(r)
    contagem = random.choice(range(2))
    contagem = contagem+1
    for a in range(contagem):
        dica.append(random.choice(l_respostas_erradas))
    if len(dica) == 2:
        if dica[0] == dica[1]:
            del dica[1]
    if len(dica) == 2:        
        x = 'DICA:\nOpções certamente erradas: {0} | {1}'.format(dica[0], dica[1])
    else:
        x = 'DICA:\nOpções certamente erradas: {0}'.format(dica[0])

    return x 
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

# CONTADORES 
id = 1
n = 0 
ajuda = 3
pula = 2

# VALIDANDO LISTA DE QUESTÕES  
valida = valida_questoes(quest)
    #deve retornar uma lista com dicionarios vazios. 
lista_dic_emp = ['{}, ' * (len(quest) - 1) + '{}']


# TRANSFORMANDO LISTA DE QUESTÕES EM UM DICIONARIO COM SEPARAÇÃO POR NIVEL 
dic_questoes = transforma_base(quest)



# INTRODUÇÃO
nome = input('''Bem vindo ao Fortuna DesSoft,
Digite seu nome para começar: ''')
print('''
Olá {0}, pronto para ser o mais novo milinonário?
No Fortuna você terá que responder perguntas de multiplas escolha podendo ganhar até 1 milhão de reais!!!!
Cada resposta correta aumentará seu premio!!!

CUIDADO basta uma resposta incorreta para perder tudo.

Durante o jogo você terá direito de pular 2 perguntas e solicitar 3 ajudas para os universitários.
Para pular ou pedir ajuda digite: 'pula' ou 'ajuda'
Você pode parar a qualquer momento do jogo, para isso digite: 'parar' 

BOA SORTE, QUE A FORTUNA ESTEJA COM VOCE
'''.format(nome))

# SORTEANDO UMA QUESTÃO

for nivel, lista_pergunta in dic_questoes.items():
    i = 0 
    while i < 9:
        Pergunta = sorteia_questao_inedida(dic_questoes,niveis[n//3], sort)
        pergunta_texto = questao_para_texto(Pergunta, id)
        print(niveis[n//3])
        n += 1
        i += 1
        print(pergunta_texto)
        resposta = str(input('DIGITE SUA RESPOSTA: '))
        












