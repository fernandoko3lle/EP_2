# IMPORTAÇÕES
import random
from termcolor import *
 
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

          {'titulo': 'Quais dessas marcas não são alemães?',
          'nivel': 'facil',
          'opcoes': {'A': 'Porsche', 'B': 'Mercedes Benz', 'C': 'Audi', 'D': 'Ferrari'},
          'correta': 'D'},
          
          {'titulo': 'Albert Einstein foi:',
          'nivel': 'facil',
          'opcoes': {'A': 'Físico', 'B': 'Cientista', 'C': 'Advogado', 'D': 'Médico'},
          'correta': 'A'},
          
          {'titulo': 'Qual o maior osso do corpo humano?',
          'nivel': 'facil',
          'opcoes': {'A': 'Fêmur', 'B': 'Tíbia', 'C': 'Bacia', 'D': 'Úmero'},
          'correta': 'A'},
          
          {'titulo': 'Qual o maior orgão do corpo humano?',
          'nivel': 'facil',
          'opcoes': {'A': 'Coração', 'B': 'Rins', 'C': 'Pulmões', 'D': 'Pele'},
          'correta': 'D'},

          {'titulo': 'Quantas copas do mundo a seleção Brasileira ganhou?',
          'nivel': 'facil',
          'opcoes': {'A': '4', 'B': '5', 'C': '6', 'D': '3'},
          'correta': 'B'},
          
          {'titulo': 'Qual o nome do mascote da copa de 2014',
          'nivel': 'facil',
          'opcoes': {'A': 'Zakumi', 'B': 'Fuleco', 'C': 'Zabivaka', 'D': "La'ebb"},
          'correta': 'B'},
          
          {'titulo': 'Quanto é 24 + 12 + 13 - 20',
          'nivel': 'facil',
          'opcoes': {'A': '25', 'B': 'Nenhuma dessas', 'C': '29', 'D': '31'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

          {'titulo': 'Quem é o maior vencedor de Grand Slam?',
            'nivel': 'medio',
            'opcoes': {'A': 'Roger Federer', 'B': 'NovaK Djokovic', 'C': 'Rafael Nadal', 'D': 'Gustavo Kuerten'},
            'correta': 'C'},

            {'titulo': 'Quantas pessoas morreram na segunda guerra mundia?',
            'nivel': 'medio',
            'opcoes': {'A': '40 milhoes de pessoas', 'B': '20 milhoes de pessoas', 'C': '50 milhoes de pessoas', 'D': '80 milhoes de pessoas'},
            'correta': 'A'},

            {'titulo': 'Qual ano foi fundado o Corinthinas Paulista?',
            'nivel': 'medio',
            'opcoes': {'A': '1912', 'B': '1910', 'C': '1923', 'D': '1915'},
            'correta': 'B'},

            {'titulo': 'Qual a população do estado de São Paulo?',
            'nivel': 'medio',
            'opcoes': {'A': '38 milhões', 'B': '40 milhões', 'C': '44 milhões', 'D': '35 milhões'},
            'correta': 'C'},

            {'titulo': 'Qual a idade média de um gato?',
            'nivel': 'medio',
            'opcoes': {'A': '15 a 20 anos', 'B': '12 a 18 anos', 'C': '10 a 12 anos', 'D': '8 a 10 anos'},
            'correta': 'B'},

            {'titulo': 'Quantos gols Maradona fez ao longo de sua carreira?',
            'nivel': 'medio',
            'opcoes': {'A': '548 gols', 'B': '628 gols', 'C': '456 gols', 'D': '497 gols'},
            'correta': 'A'},
        
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

          {'titulo': 'O freio ABS nos carros mais modernos possui a função de:',
            'nivel': 'dificil',
            'opcoes': {'A': 'Travar as 4 rodas do carro', 'B': 'Travar apenas as rodas traseiras', 'C': 'Não travar as rodas', 'D': 'Não travar as rodas dinateiras'},
            'correta': 'C'},     

            {'titulo': 'Qual é a cidade mais visitada do mundo?',
            'nivel': 'dificil',
            'opcoes': {'A': 'Paris', 'B': 'Pequim', 'C': 'Nova York', 'D': 'Hong Kong'},
            'correta': 'D'},

            {'titulo': 'Quantos anos de governo teve Getulio Vargas?',
            'nivel': 'dificil',
            'opcoes': {'A': '12 anos', 'B': '10 anos', 'C': '15 anos', 'D': '8 anos'},
            'correta': 'C'},

            {'titulo': 'Qual oceano banha a Australia',
            'nivel': 'dificil',
            'opcoes': {'A': 'Pacífico e Índico', 'B': 'Atlântico', 'C': 'Índico', 'D': 'Pacífico'},
            'correta': 'A'},

            {'titulo': 'Qual foi o ultimo ano de Felipe Massa na Formula 1',
            'nivel': 'dificil',
            'opcoes': {'A': '2017', 'B': '2016', 'C': '2015', 'D': '2018'},
            'correta': 'B'},

            {'titulo': 'Qual a altura da cesta de basquete da NBA?',
            'nivel': 'dificil',
            'opcoes': {'A': '3m e 5cm', 'B': '3m e 8cm', 'C': '3m e 3cm', 'D': '3m e 10cm'},
            'correta': 'A'},

            {'titulo': 'Quantos banheiros tem no Maracanã?',
            'nivel': 'dificil',
            'opcoes': {'A': '228', 'B': '234', 'C': '225', 'D': '231'},
            'correta': 'D'},

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
sai_sem_nada = 0

# NIVEIS
niveis = {
    0: 'facil',
    1: 'medio',
    2: 'dificil'
}

#Premio
Premio = 0
dic_premio = {
    1: 1000,
    2: 5000,
    3: 10000,
    4: 30000,
    5: 50000,
    6: 100000,
    7: 300000,
    8: 500000,
    9: 1000000,
}        


# FUNÇÕES 
def sorteia_questao(dic_questoes, nivel):
    return random.choice(dic_questoes[nivel])
def sorteia_questao_inedida(dic_questoes, nivel, sort): 
    q_sort = sorteia_questao(dic_questoes, nivel)
    while q_sort in sort:
        q_sort = sorteia_questao(dic_questoes, nivel)
    sort.append(q_sort)
    return q_sort
def questao_para_texto(dic_questao, id):
  return '''

----------------------------------------
QUESTAO {0}

{1}

RESPOSTAS:
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
def lista_dic_vaz(n):
    j = 0
    lista_dic_emp = []
    while j < n:
        lista_dic_emp.append({})
        j += 1
    return lista_dic_emp

# CONTADORES 
id = 0
ajuda = 2
pula = 3
c_p = 1

# True / False
para = False
perdeu = False
joga = True

# VALIDANDO LISTA DE QUESTÕES  
valida = valida_questoes(quest)
nova_lista = lista_dic_vaz(len(quest))


# TRANSFORMANDO LISTA DE QUESTÕES EM UM DICIONARIO COM SEPARAÇÃO POR NIVEL 
dic_questoes = transforma_base(quest)


# INTRODUÇÃO
cprint('\nOlá! Você está na fortuna DesSoft e terá a oportunidade de enriquecer!', 'magenta',attrs=['bold'])
nome = input('\nQual seu nome? ')
cprint('''\nOk {0}, você tem direito a pular 3 vezes e 2 ajudas!'''.format(nome.upper()),attrs=['bold'])
cprint('''As opções de respostas são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!
''', 'cyan',attrs=['bold'])
comeco = input('Aperte ENTER para continuar...')

# JOGO
print('\nO jogo já vai começar! Lá vem a primeira questão!')
while comeco != '':
    comeco = input('Aperte ENTER para continuar...')
if valida == nova_lista:
    i = 0 
    erro = False
    while joga == True:
        while i < 9:
            if para == False:
                if erro == False:
                    if i == 0:
                        cprint('\nVamos começar com questões do nível FACIL!')
                    if i == 3:
                        cprint('\nHEY! Você passou para o nível MEDIO!',attrs=['bold'])
                    if i == 6:
                        cprint('\nHEY! Você passou para o nível DIFICIL!', attrs=['bold'])
                    comeco = input('Aperte ENTER para continuar...')
                    while comeco != '':
                        comeco = input('Aperte ENTER para continuar...')
                    id += 1
                    Pergunta = sorteia_questao_inedida(dic_questoes,niveis[i//3], sort)
                    correta = Pergunta['correta']
                    pergunta_texto = questao_para_texto(Pergunta, id)
                    print(pergunta_texto)
                erro = False
                resposta = str(input('Qual sua resposta?! '))
                if resposta == 'ajuda':
                    if ajuda > 0:
                        ajuda -= 1
                        print('Ok, lá vem ajuda! Você tem {0} ajudas restantes!\n'.format(ajuda))
                        comeco = input('Aperte ENTER para continuar...')
                        while comeco != '':
                            comeco = input('Aperte ENTER para continuar...')
                        cprint(gera_ajuda(Pergunta),'green', attrs=['bold'])
                        resposta = str(input('Qual sua resposta?!'))
                        while resposta == 'ajuda':
                            cprint('Não deu! Você já pediu ajuda nesta questão!', 'red', attrs=['bold'])
                            resposta = str(input('Digite sua nova resposta: '))   
                    else:
                        cprint('Não deu! Você não tem mais direito a ajuda!', 'red', attrs=['bold'])
                        erro = True
                        id += 1
                        continue
                if resposta == 'pula':
                    if pula > 0:
                        pula -= 1
                        if pula == 0:
                            print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
                        else:
                            print('Ok, pulando! Você ainda tem {0} pulos!'.format(pula))
                        comeco = input('Aperte ENTER para continuar...')
                        while comeco != '':
                            comeco = input('Aperte ENTER para continuar...')
                        Pergunta = sorteia_questao_inedida(dic_questoes,niveis[i//3], sort)
                        correta = Pergunta['correta']
                        pergunta_texto = questao_para_texto(Pergunta, id)
                        print(pergunta_texto)
                        erro = True
                        continue
                    else:
                        cprint('Não deu! Você não tem mais direito a pulos!','red', attrs=['bold'])
                        erro = True
                        id += 1
                        continue
                if resposta == 'parar':
                    r = input('\nDeseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {0}.00! '.format(Premio))
                    if r == 'S':
                        para = True
                        continue
                    while r != 'S' and r != 'N':
                        cprint('Opção inválida!', 'red', attrs=['bold'])
                        r = input('\nDeseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {0}.00! '.format(Premio))
                    if r == 'N':
                        i -= 1
                        id -= 1
                        erro = True
                if resposta == correta:
                    Premio = dic_premio[c_p]
                    cprint('Você acertou! Seu prêmio atual é de R$ {}.00'.format(Premio), 'green',attrs=['bold'])
                    i += 1
                    c_p += 1
                if resposta != correta and resposta in ('A', 'B', 'C', 'D'):
                    cprint('Que pena! Você errou e vai sair sem nada :(', 'yellow',attrs=['bold'])
                    i += 9999
                    sai_sem_nada = 1
                if resposta not in ('A', 'B', 'C', 'D', 'ajuda', 'pula', 'parar'):
                    cprint('Opção invalida!', 'red', attrs=['bold'])
                    cprint('''As opções de respostas são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!
    ''', 'cyan', attrs=['bold'])
                    erro = True
                    continue
            else:
                break
        if sai_sem_nada <= 0:
            if Premio >= 1000000:
                cprint('\nPARABÉNS, você zerou o jogo e ganhou um milhão de reais!', 'green', attrs = ['bold'])
            elif Premio > 0 and Premio != 1000000:
                cprint('PARABÉNS, você ganhou {0}!'.format(Premio), 'green')
            elif Premio == 0:
                cprint('\nPoxa! Desistiu sem nada =(')
        joga_de_novo = str(input('Quer jogar novamente(S/N)?'))
        if joga_de_novo in ('S','s'):
            joga = True
            i = 0 
            pula = 3
            ajuda = 2
            id = 0
            c_p = 1
            para = False
            sai_sem_nada = 0  
        if joga_de_novo in ('N','n'):
            joga = False 
else:
    print('Erro na lista de questoes')
    print(valida)

cprint('Jogo encerrado', 'red', attrs=['bold'])

#Versão final