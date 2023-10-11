#pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)

#estresse = ctrl.Antecedent(np.arange(0, 11, 1), 'estresse')
#altura = ctrl.Antecedent(np.arange(0, 201, 1), 'altura')
atividadeFisica = ctrl.Antecedent(np.arange(0, 11, 1), 'atividadeFisica')
#quantidadeSono = ctrl.Antecedent(np.arange(0, 11, 1), 'quantidadeSono')
ingestaoAcucar = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoAcucar')
#ingestaoGordura = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoGordura')
#ingestaoCarboidrato = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoCarboidrato')
#ingestaoFrutas = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoFrutas')
#ingestaoCha = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoCha')
#ingestaoLegumes = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoLegumes')
#ingestaoVerduras = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoVerduras')
#ingestaoProteinas = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoProteinas')
#ingestaoAgua = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoAgua')

#Variaveis de saída (Consequent)

obesidade = ctrl.Consequent(np.arange(0, 121, 1), 'obesidade')

# automf -> Atribuição de categorias automaticamente

#altura.automf(name=['baixo','normal','alto'])
atividadeFisica.automf(names=['pouca','media','muita'])
ingestaoAcucar.automf(names=['pouca','media','muita'])
#ingestaoProteinas.automf(name=['pouca','media','muita'])
#ingestaoAgua.automf(name=['pouca','media','muita'])

# atribuicao sem o automf

#obesidade['baixa'] = fuzz.gaussmf(obesidade.universe,0,.5)
#obesidade['media'] = fuzz.gaussmf(obesidade.universe,70,5)
#obesidade['alta'] = fuzz.gaussmf(obesidade.universe,120,5)

obesidade.automf(names=['baixa','media','alta'])

#Visualizando as variáveis

#altura.view()
atividadeFisica.view()
ingestaoAcucar.view()
obesidade.view()

#Criando as regras

regra1 = ctrl.Rule(ingestaoAcucar['pouca'] & atividadeFisica['pouca'],obesidade['media'])
regra2 = ctrl.Rule(ingestaoAcucar['media'] & atividadeFisica['media'],obesidade['media'])
regra3 = ctrl.Rule(ingestaoAcucar['muita'] & atividadeFisica['muita'],obesidade['media'])
regra4 = ctrl.Rule(ingestaoAcucar['pouca'] & atividadeFisica['muita'],obesidade['baixa'])
regra5 = ctrl.Rule(ingestaoAcucar['muita'] & atividadeFisica['pouca'],obesidade['alta'])

controlador = ctrl.ControlSystem([regra1,regra2,regra3,regra4,regra5])

#Simulando

CalculoGorjeta = ctrl.ControlSystemSimulation(controlador)

#Input

atvFisica = int(input('Qntd. de atividade Fisica: '))
ingAcucar = int(input('Qnts. de consumo de acucar: '))

CalculoGorjeta.input['atividadeFisica'] = atvFisica
CalculoGorjeta.input['ingestaoAcucar'] = ingAcucar
CalculoGorjeta.compute()

valorGorjeta = CalculoGorjeta.output['obesidade']

print("\nQualidade %d \nServiço %d \nGorjeta de %5.2f" %(atvFisica, ingAcucar,valorGorjeta))

ingestaoAcucar.view(sim=CalculoGorjeta)
atividadeFisica.view(sim=CalculoGorjeta)
obesidade.view(sim=CalculoGorjeta)

plt.show()