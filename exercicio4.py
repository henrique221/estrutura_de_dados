"""Exercicio 3 

Dizemos que um número natural n é palíndromo se:
1º algarismo de n é igual ao seu último algarismo,
2º algarismo de n é igual ao penúltimo algarismo e assim
sucessivamente.
Exemplo: 567765 e 32423 são palíndromos
567675 não é palíndromo.
Faça uma função que receba um número inteiro e positivo n e
verifica se é palíndromo, caso o número seja palíndromo é
retornado 1 e 0 caso contrário.

INTEGRANTES:

Henrique Borges da Silva - 1700054
Fabio Aurelio Nogueira - 1700603
Gabriel Bueno Maia - 1601606
"""

def recebeNumero(N):
    tamanhoNumero = len(str(N))
    resultado = 0
    
    for cadaNumero in range(tamanhoNumero):
        
        resto = N % 10
        multPorDez = N // 10
        N = multPorDez
        resultado = (resultado * 10)+resto
        
        #print('N = ',N, 'multiplicacao = ',multPorDez, 'resto = ',resto, 'resultado = ',resultado)

    return resultado

def filtraPalindromo(N, Ninv):
    if N == Ninv:
        return 1
    return 0

def Main():
    
    N = int(input("Digite o numero inteiro : "))
    Ninv = recebeNumero(N)
    #print(Ninv)
    print(filtraPalindromo(N, Ninv))


Main()