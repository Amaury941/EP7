import warnings
warnings.filterwarnings("ignore")

### importações

from functions import * 

### dependências: "dataset.csv", "tStudent.csv"

dados = pd.read_csv('datasets/dataset.csv')

### área de testes

Pulse1,Pulse2=[],[]

for n in range(len(dados['Age'])):
	if dados['Ran'][n] == 1:
		Pulse1.append(dados['Pulse1'][n])
		Pulse2.append(dados['Pulse2'][n])


difference = ( calculate_difference(Pulse1,Pulse2) )
α = 0.1

''' 
hipóteses:
	H_0 : μ_1 - μ_2 <= 0 <--- a diferença da primeira a mostra e da segunda amostra é 0 ou menor que 0
	μ_a : μ_1 - μ_2 > 0  <--- a diferença da primeira e da segunda é maior de 0
'''

## nível de significância 
print ("Nível de significância =",α)

## diferença
print ("diferenças",difference)

## sum of differences
print ("soma das diferenças =", calculate_sigma_differences( difference  ) )

## d¯¯¯ média da diferença
print ("média das diferenças =", calculate_mean ( difference ))

## desvio padrão das diferença
print ("desvio padrão das diferenças =", calculate_standard_deviation_diferences ( difference ) )

## grau de liberdade
print ("grau de liberdade =",calculate_gl(difference)[:calculate_gl(difference).index(".")])

## calculando região de rejeição
print ("região de rejeição em t >",region_rejection(difference)) 

## tcalc
print ("t =",t_calc(difference))

## H_0 é verdadeira ?
print (return_t_calc(difference,α))

# plotando o gráfico
plot_graphic (Pulse1,Pulse2,arr1Index='Pulso pré-exercício',arr2Index='pulso pós-exercício')


# o pulso aumenta em ao menos 10%

# hipótese nula: o pulso não aumenta (média primeira - média segunda >= 0)
# hipótese: o pulso aumenta( a média da primeira - a média da segunda > 0)