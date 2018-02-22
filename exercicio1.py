#Exercicio 1 de estrutura de dados

""" Escreva um programa para encontrar todos números primos
existentes entre N1 e N2 (inclusive), em que N1 e N2 são números
naturais lidos. Para resolver o problema utilize a função do exercício
(03 feito em sala)."""

def identifica_numero_primo(N2):

	lista_numeros = list(range(2, N2+1)) #lista de numeros inteiros
	
	for each_number in range(2, N2): #loop para cada numero entre 2 e N2
		if each_number in lista_numeros: #se numero estiver na lista de numeros inteiros
			for numeros in range(each_number ** 2, N2 + 1, each_number): #loop multiplicando os numeros da lista por 2 e criando um range 
				if numeros in lista_numeros:
					lista_numeros.remove(numeros)

	return lista_numeros


def Main():
	N2 = int(input("Qual o valor do N2 ? \n"))
	print(identifica_numero_primo(N2))

Main()