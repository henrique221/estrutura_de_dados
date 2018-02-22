"""Exercicio 3 

Escreva um programa que receba um número inteiro N, esse
número não contém o digito 0 (zero), e devolve N invertido,
Exemplo: se N igual 123 a resposta será 321.

INTEGRANTES:

Henrique Borges da Silva - 1700054
Fabio Aurelio Nogueira - 1700603
Gabriel Bueno Maia - 1601606
"""

def devolveNumeroInvertido(N):
    tamanhoNumero = len(str(N))
    resultado = 0

    for cadaNumero in range(tamanhoNumero):
        
        resto = N % 10
        multPorDez = N // 10
        N = multPorDez
        resultado = (resultado * 10)+resto
        
        #print('N = ',N, 'multiplicacao = ',multPorDez, 'resto = ',resto, 'resultado = ',resultado)

    return resultado

def Main():
    
    N = int(input("Digite o numero inteiro : "))
    print(devolveNumeroInvertido(N))

Main()
    




