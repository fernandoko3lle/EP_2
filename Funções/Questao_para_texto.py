def questao_para_texto(dic_questao, id):
  return ''' ----------------------------------------
QUESTAO {0}

{1}

RESPOSTAS:
A: {2}
B: {3}
C: {4}
D: {5}

'''.format(id,dic_questao['titulo'],dic_questao['opcoes']['A'],dic_questao['opcoes']['B'], dic_questao['opcoes']['C'], dic_questao['opcoes']['D'])