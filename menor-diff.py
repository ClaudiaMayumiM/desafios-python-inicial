# Calcular a diferença mínima entre quaisquer dois elementos 
# Imprimir todos os pares de elementos com essa diferença em ordem crescente 

# EX:
# (2, 4) (4, 6)


""" 
1 - ordenar a lista por ordem crescente 
2 - armazenar o valor da menor diferença em uma variável 
3 - identificar os pares de números que possuem essa diferença entre si 
4 - imprimir na tela 
"""

import numpy as np

numeros = [6, 2, 4, 10, 20, 22, 30, 44, 46, 100, 78]

numeros.sort()

print(numeros)

num = np.array(numeros)

menor_diff = np.diff(num)

menor = min(menor_diff)


for i in range(0, len(numeros)):

  if numeros[i] == numeros[i-1] + menor:
    print(numeros[i-1], numeros[i])

