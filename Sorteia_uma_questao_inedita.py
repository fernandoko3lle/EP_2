import random
def sorteia_questao(dic_questoes, nivel):
    return random.choice(dic_questoes[nivel])
def sorteia_questao_inedida(dic_questoes, nivel, sort): 
    c = 0 
    for q, r in dic_questoes.items():
        if q == nivel:
            if r[c] not in sort:
                q_sort = sorteia_questao(dic_questoes, nivel)
            else:
                sort.append(r[c]) 
            c += 1
    return q_sort
print(sorteia_questao_inedida( {
  "facil": [
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}, 'medio', [
  {
    "titulo": "Qual destes parques não se localiza em São Paulo?!",
    "nivel": "facil",
    "opcoes": {
      "A": "Ibirapuera",
      "B": "Parque do Carmo",
      "C": "Parque Villa Lobos",
      "D": "Morro da Urca"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual o resultado da operação 57 + 32?",
    "nivel": "facil",
    "opcoes": {
      "A": "-19",
      "B": "85",
      "C": "89",
      "D": "99"
    },
    "correta": "C"
  }
]))
