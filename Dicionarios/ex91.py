'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um 
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no 
dado
'''

import random

jogadores = {}
num_jogadores = 4

for i in range(1, num_jogadores + 1):
    jogador = input(f"Digite o nome do jogador {i}: ")
    resultado = random.randint(1, 6)
    jogadores[jogador] = resultado

print("\n=== Resultados ===")
for jogador, resultado in jogadores.items():
    print(f"{jogador}: {resultado}")

jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("\n=== Resultados Ordenados ===")
for jogador, resultado in jogadores_ordenados:
    print(f"{jogador}: {resultado}")
