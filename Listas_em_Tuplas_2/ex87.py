'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.    
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha
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

# Calcular a soma dos valores pares
soma_pares = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            soma_pares += elemento

# Calcular a soma dos valores da terceira coluna
soma_terceira_coluna = 0
for linha in matriz:
    soma_terceira_coluna += linha[2]

# Encontrar o maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

# Imprimir os resultados
print(f"Soma dos valores pares: {soma_pares}")
print(f"Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"Maior valor da segunda linha: {maior_segunda_linha}")
