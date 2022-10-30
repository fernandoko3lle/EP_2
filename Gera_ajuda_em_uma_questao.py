import random 

def gera_ajuda(questao):
    repetidas = []
    l_questoes =[]
    correta = questao['correta']
    dic_questoes = questao['opcoes']
    del dic_questoes[correta]
    for r in dic_questoes.values():
        l_questoes.append(r)
    contagem = random.choice(range(2))
    contagem = contagem+1
    for a in range(contagem):
      print(random.choice(l_questoes))
        

        


            

        
        
        
        




gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "C"
})