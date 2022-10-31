import random 
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
    
print(gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "C"
}))