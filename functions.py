import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# calcula a média entre dois arrays

def calculate_mean (arr,mean=0):
	for item in arr:
		mean += item
	return round (mean/len(arr),3)

# calcula a diferença entre dois arrays

def calculate_difference (arr1, arr2, arr3 = []):
	for item in range(len(arr1)):
		arr3.append(arr1[item]-arr2[item])
	return arr3

# calcula a soma de todas as diferenças

def calculate_sigma_differences(arrd, result=0):
 	for n in arrd:
 		result += (n)
 	return result

# calcula o desvio padrão das diferenças

def calculate_standard_deviation_diferences(arrd,standardDeviation = 0):

 	for item in arrd:
 		standardDeviation += (item - calculate_mean(arrd))**2
 	return ( ( ( standardDeviation ) / (len(arrd)-1) )** 0.5 )

# calcula o grau de liberdade (de acordo com as necessidades da tabela tStudent)

def calculate_gl(arrd): 
	aux = len(arrd) - 1
	try: 
		str(aux).index(".")
		return (str(aux))
	except:
		return (str(aux)+'.1')

# calcula o valor da região de rejeição 

def region_rejection(difference):
	tStudent = pd.read_csv('datasets/tStudent.csv')

	for item in range(len(tStudent)):
		aux = tStudent['xxx'][item] 
		if (str(aux) == ( calculate_gl(difference)[:calculate_gl(difference).index("."):] ) ):
			return ( tStudent [('0%s'%calculate_gl(difference)[calculate_gl(difference).index("."):])] [item] )

# calcula a estatística do teste padronidada

def t_calc(arrd,ud=0):
	return (
		(calculate_mean ( arrd ) - ud)
		/ 
		(  calculate_standard_deviation_diferences ( arrd ) 
			/ 
			(len(arrd))**0.5   
		)
	)

# retorna se rejetou ou não a hipótese nula

def return_t_calc( arrd,α,ud=0):

	if ( region_rejection(arrd) < t_calc(arrd,ud)):
		return "Rejeitou H0\nPortanto,há evidência suficiente para sustentar a afirmação"
	return "Falhou em rejeitar H0\nPortanto,não há evidência suficiente para sustentar a afirmação"

# plota o gráfico #

def MaxOrMin_array(arr,value=0,type=True):
	if type:
		for n in arr:
			if n > value: 
				value = n
		return value

	value = MaxOrMin_array(arr,value=0,type=True)

	for n in arr:
		if n < value: 
			value = n
	return value
	
def MaxiOrMini(v1,v2,type=True):
	if type:
		if v1 > v2:
			return v1
		return v2
	if v1 < v2:
		return v1
	return v2

def plot_graphic (arr1,arr2,arr1Index='arr1',arr2Index='arr2'):
	sns.distplot(arr1, hist=False, rug=False,label=arr1Index)
	sns.distplot(arr2, hist=False, rug=False,label=arr2Index)

	plt.xlim([
		MaxiOrMini(MaxOrMin_array(arr1,type=False),MaxOrMin_array(arr2,type=False),type=False)-1,
		MaxiOrMini(MaxOrMin_array(arr1),MaxOrMin_array(arr2))+1,
		])

	plt.xlabel('frequência de pulso por minuto')
	plt.ylabel('probabilidades')
	plt.title('Mudança no pulso pré e pós exercício')
	plt.legend()
	plt.savefig("imagem.png")

	print ([
		MaxiOrMini(MaxOrMin_array(arr1,type=False),MaxOrMin_array(arr2,type=False),type=False)-1,
		MaxiOrMini(MaxOrMin_array(arr1),MaxOrMin_array(arr2))+1,
		])
