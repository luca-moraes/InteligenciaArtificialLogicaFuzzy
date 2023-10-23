#pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import os 

folder = './imagens/'

#os.makedirs(output_directory, exist_ok=True)

#Variaveis de Entrada (Antecedent)

estresse = ctrl.Antecedent(np.arange(0, 11, 1), 'estresse')
altura = ctrl.Antecedent(np.arange(120, 201, 1), 'altura')
atividadeFisica = ctrl.Antecedent(np.arange(0, 11, 1), 'atividadeFisica')
quantidadeSono = ctrl.Antecedent(np.arange(2, 9, 1), 'quantidadeSono')
ingestaoAcucar_Carboidrato = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoAcucar')
ingestaoGordura = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoGordura')
ingestaoFrutas_Legumes_Verduras = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoFrutas')
ingestaoProteinas = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoProteinas')
ingestaoAgua_Chas = ctrl.Antecedent(np.arange(0, 11, 1), 'ingestaoAgua')

#Variaveis de saída (Consequent)

obesidade = ctrl.Consequent(np.arange(0, 101, 1), 'obesidade')

# automf -> Atribuição de categorias automaticamente

# estresse.automf(names=['baixo','normal','alto'])
# altura.automf(names=['baixo','normal','alto'])
# atividadeFisica.automf(names=['pouca','media','muita'])
# quantidadeSono.automf(names=['pouca','media','muita'])
# ingestaoAcucar_Carboidrato.automf(names=['pouca','media','muita'])
# ingestaoGordura.automf(names=['pouca','media','muita'])
# ingestaoFrutas_Legumes_Verduras.automf(names=['pouca','media','muita'])
# ingestaoProteinas.automf(names=['pouca','media','muita'])
# ingestaoAgua_Chas.automf(names=['pouca','media','muita'])

# obesidade.automf(names=['pouca','normal','alta'])

# atribuicao sem o automf, usando gaussiana no lugar

estresse['baixo'] = fuzz.gaussmf(estresse.universe,2,1)
estresse['normal'] = fuzz.gaussmf(estresse.universe,5,1)
estresse['alto'] = fuzz.gaussmf(estresse.universe,9,1)

altura['baixo'] = fuzz.gaussmf(altura.universe,130,8)
altura['normal'] = fuzz.gaussmf(altura.universe,160,4)
altura['alto'] = fuzz.gaussmf(altura.universe,180,4)

atividadeFisica['pouca'] = fuzz.gaussmf(atividadeFisica.universe,2,1)
atividadeFisica['media'] = fuzz.gaussmf(atividadeFisica.universe,5,1)
atividadeFisica['muita'] = fuzz.gaussmf(atividadeFisica.universe,9,1)

quantidadeSono['pouca'] = fuzz.gaussmf(quantidadeSono.universe,3,.6)
quantidadeSono['media'] = fuzz.gaussmf(quantidadeSono.universe,5,.4)
quantidadeSono['muita'] = fuzz.gaussmf(quantidadeSono.universe,7,.4)

ingestaoAcucar_Carboidrato['pouca'] = fuzz.gaussmf(ingestaoAcucar_Carboidrato.universe,2,1)
ingestaoAcucar_Carboidrato['media'] = fuzz.gaussmf(ingestaoAcucar_Carboidrato.universe,5,1)
ingestaoAcucar_Carboidrato['muita'] = fuzz.gaussmf(ingestaoAcucar_Carboidrato.universe,9,1)

ingestaoGordura['pouca'] = fuzz.gaussmf(ingestaoGordura.universe,2,1)
ingestaoGordura['media'] = fuzz.gaussmf(ingestaoGordura.universe,5,1)
ingestaoGordura['muita'] = fuzz.gaussmf(ingestaoGordura.universe,9,1)

ingestaoFrutas_Legumes_Verduras['pouca'] = fuzz.gaussmf(ingestaoFrutas_Legumes_Verduras.universe,2,1)
ingestaoFrutas_Legumes_Verduras['media'] = fuzz.gaussmf(ingestaoFrutas_Legumes_Verduras.universe,5,1)
ingestaoFrutas_Legumes_Verduras['muita'] = fuzz.gaussmf(ingestaoFrutas_Legumes_Verduras.universe,9,1)

ingestaoProteinas['pouca'] = fuzz.gaussmf(ingestaoProteinas.universe,2,1)
ingestaoProteinas['media'] = fuzz.gaussmf(ingestaoProteinas.universe,5,.6)
ingestaoProteinas['muita'] = fuzz.gaussmf(ingestaoProteinas.universe,9,1)

ingestaoAgua_Chas['pouca'] = fuzz.gaussmf(ingestaoAgua_Chas.universe,2,1)
ingestaoAgua_Chas['media'] = fuzz.gaussmf(ingestaoAgua_Chas.universe,5,1)
ingestaoAgua_Chas['muita'] = fuzz.gaussmf(ingestaoAgua_Chas.universe,9,1)

obesidade['pouca'] = fuzz.gaussmf(obesidade.universe,30,8)
obesidade['normal'] = fuzz.gaussmf(obesidade.universe,55,4)
obesidade['alta'] = fuzz.gaussmf(obesidade.universe,90,10)

#Visualizando as variáveis

estresse.view()
plt.savefig(os.path.join(folder, 'estresse_automatico.png'))

altura.view()
plt.savefig(os.path.join(folder, 'altura_automatico.png'))

atividadeFisica.view()
plt.savefig(os.path.join(folder, 'atividade_fisica_automatico.png'))

quantidadeSono.view()
plt.savefig(os.path.join(folder, 'quantidade_sono_automatico.png'))

ingestaoAcucar_Carboidrato.view()
plt.savefig(os.path.join(folder, 'ingestao_acucar_automatico.png'))

ingestaoFrutas_Legumes_Verduras.view()
plt.savefig(os.path.join(folder, 'ingestao_frutas_automatico.png'))

ingestaoGordura.view()
plt.savefig(os.path.join(folder, 'ingestao_gordura_automatico.png'))

ingestaoProteinas.view()
plt.savefig(os.path.join(folder, 'ingestao_proteinas_automatico.png'))

ingestaoAgua_Chas.view()
plt.savefig(os.path.join(folder, 'ingestao_agua_automatico.png'))

obesidade.view()
plt.savefig(os.path.join(folder, 'obesidade_automatico.png'))

plt.clf()

#Criando as regras

regra1 = ctrl.Rule(estresse['baixo'] & altura['baixo'] 
                   & atividadeFisica['muita'] 
                   & quantidadeSono['muita'] 
                   & ingestaoAcucar_Carboidrato['pouca'] 
                   & ingestaoGordura['pouca'] 
                   & ingestaoFrutas_Legumes_Verduras['muita'] 
                   & ingestaoProteinas['muita'] 
                   & ingestaoAgua_Chas['muita']
                   ,obesidade['pouca'])

regra2 = ctrl.Rule(estresse['normal'] & altura['baixo'] 
                   & atividadeFisica['media'] 
                   & quantidadeSono['media'] 
                   & ingestaoAcucar_Carboidrato['media'] 
                   & ingestaoGordura['media'] 
                   & ingestaoFrutas_Legumes_Verduras['media'] 
                   & ingestaoProteinas['media'] 
                   & ingestaoAgua_Chas['media']
                   ,obesidade['normal'])

regra3 = ctrl.Rule(estresse['alto'] & altura['baixo'] 
                   & atividadeFisica['pouca'] 
                   & quantidadeSono['pouca'] 
                   & ingestaoAcucar_Carboidrato['muita'] 
                   & ingestaoGordura['muita'] 
                   & ingestaoFrutas_Legumes_Verduras['pouca'] 
                   & ingestaoProteinas['pouca'] 
                   & ingestaoAgua_Chas['pouca']
                   ,obesidade['alta'])

regra4 = ctrl.Rule(estresse['baixo'] & altura['normal'] 
                   & atividadeFisica['muita'] 
                   & quantidadeSono['muita'] 
                   & ingestaoAcucar_Carboidrato['pouca'] 
                   & ingestaoGordura['pouca'] 
                   & ingestaoFrutas_Legumes_Verduras['muita'] 
                   & ingestaoProteinas['muita'] 
                   & ingestaoAgua_Chas['muita']
                   ,obesidade['pouca'])

regra5 = ctrl.Rule(estresse['normal'] & altura['normal'] 
                   & atividadeFisica['media'] 
                   & quantidadeSono['media'] 
                   & ingestaoAcucar_Carboidrato['media'] 
                   & ingestaoGordura['media'] 
                   & ingestaoFrutas_Legumes_Verduras['media'] 
                   & ingestaoProteinas['media'] 
                   & ingestaoAgua_Chas['media']
                   ,obesidade['normal'])

regra6 = ctrl.Rule(estresse['alto'] & altura['normal'] 
                   & atividadeFisica['pouca'] 
                   & quantidadeSono['pouca'] 
                   & ingestaoAcucar_Carboidrato['muita'] 
                   & ingestaoGordura['muita'] 
                   & ingestaoFrutas_Legumes_Verduras['pouca'] 
                   & ingestaoProteinas['pouca'] 
                   & ingestaoAgua_Chas['pouca']
                   ,obesidade['alta'])

regra7 = ctrl.Rule(estresse['baixo'] & altura['alto'] 
                   & atividadeFisica['muita'] 
                   & quantidadeSono['muita'] 
                   & ingestaoAcucar_Carboidrato['pouca'] 
                   & ingestaoGordura['pouca'] 
                   & ingestaoFrutas_Legumes_Verduras['muita'] 
                   & ingestaoProteinas['muita'] 
                   & ingestaoAgua_Chas['muita']
                   ,obesidade['pouca'])

regra8 = ctrl.Rule(estresse['normal'] & altura['alto'] 
                   & atividadeFisica['media'] 
                   & quantidadeSono['media'] 
                   & ingestaoAcucar_Carboidrato['media'] 
                   & ingestaoGordura['media'] 
                   & ingestaoFrutas_Legumes_Verduras['media'] 
                   & ingestaoProteinas['media'] 
                   & ingestaoAgua_Chas['media']
                   ,obesidade['normal'])

regra9 = ctrl.Rule(estresse['alto'] & altura['alto'] 
                   & atividadeFisica['pouca'] 
                   & quantidadeSono['pouca'] 
                   & ingestaoAcucar_Carboidrato['muita'] 
                   & ingestaoGordura['muita'] 
                   & ingestaoFrutas_Legumes_Verduras['pouca'] 
                   & ingestaoProteinas['pouca'] 
                   & ingestaoAgua_Chas['pouca']
                   ,obesidade['alta'])


controlador = ctrl.ControlSystem([regra1,regra2,regra3,regra4,regra5,regra6,regra7,regra8,regra9])

#Simulando

CalculoObesidade = ctrl.ControlSystemSimulation(controlador)

#Input

alt = int(input('Digite sua altura (120 - 200 cm): '))
qtdSono = int(input('Qntd. de sono (2 - 8 horas): '))
est = int(input('Digite seu nivel de estresse (escala de 0 - 10): '))
atvFisica = int(input('Qntd. de atividade Fisica (escala de 0 - 10): '))
ingAcucar = int(input('Qnts. de consumo de acucar e carboidratos (escala de 0 - 10): '))
ingGord = int(input('Qnts. de consumo de gordura (escala de 0 - 10): '))
ingFrutas = int(input('Qnts. de consumo de frutas, legumes e verduras (escala de 0 - 10): '))
ingProt = int(input('Qnts. de consumo de proteinas (escala de 0 - 10): '))
ingAgua = int(input('Qnts. de consumo de agua e chas (escala de 0 - 10): '))

CalculoObesidade.input['estresse'] = est
CalculoObesidade.input['altura'] = alt
CalculoObesidade.input['atividadeFisica'] = atvFisica
CalculoObesidade.input['quantidadeSono'] = qtdSono
CalculoObesidade.input['ingestaoAcucar'] = ingAcucar
CalculoObesidade.input['ingestaoGordura'] = ingGord
CalculoObesidade.input['ingestaoFrutas'] = ingFrutas
CalculoObesidade.input['ingestaoProteinas'] = ingProt
CalculoObesidade.input['ingestaoAgua'] = ingAgua

CalculoObesidade.compute()

valorObesidade = CalculoObesidade.output['obesidade']

print("\nValores de entrada: ")

print("\nEstresse: %d \nAltura: %d" %(est, alt))
print("Atividade Fisica: %d \nQntd. de sono: %d" %(atvFisica, qtdSono))
print("Qnts. de consumo de acucar e carboidratos: %d" %(ingAcucar))
print("Qnts. de consumo de gordura: %d" %(ingGord))
print("Qnts. de consumo de frutas, legumes e verduras: %d" %(ingFrutas))
print("Qnts. de consumo de proteinas: %d" %(ingProt))
print("Qnts. de consumo de agua e chas: %d" %(ingAgua))

print("\nValor de saída: ")
print("Obesidade: %d" %(valorObesidade))

print("\nEscala de obesidade: \n0 - 50: Obesidade baixa \n50 - 70: Obesidade média \n70 - 100: Obesidade alta \n")

print("Classificação: ")

if valorObesidade < 50:
    print("Classificado como pouco obeso")
elif valorObesidade >= 50 and valorObesidade < 70:
    print("Classificado como obesidade média")
else:
    print("Classificado como muito obeso")

#Salvando as imagens

estresse.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'estresse_regras.png'))

altura.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'altura_regras.png'))

atividadeFisica.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'atividade_fisica_regras.png'))

quantidadeSono.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'quantidade_sono_regras.png'))

ingestaoAcucar_Carboidrato.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'ingestao_acucar_regras.png'))

ingestaoGordura.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'ingestao_gordura_regras.png'))

ingestaoFrutas_Legumes_Verduras.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'ingestao_frutas_regras.png'))

ingestaoProteinas.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'ingestao_proteinas_regras.png'))

ingestaoAgua_Chas.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'ingestao_agua_regras.png'))

obesidade.view(sim=CalculoObesidade)
plt.savefig(os.path.join(folder, 'obesidade_regras.png'))

#exibir no terminal

# plt.show()