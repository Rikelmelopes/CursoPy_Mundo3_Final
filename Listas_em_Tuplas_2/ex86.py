'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre 
a matriz na tela, com a formatação correta
'''

# Criar uma matriz vazia de dimensão 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preencher a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))

# Imprimir a matriz formatada na tela
print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")  # Imprime o elemento seguido de um espaço
    print()  # Pula para a próxima linha

