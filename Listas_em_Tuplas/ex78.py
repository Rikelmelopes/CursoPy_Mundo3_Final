'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor 
valor digitado e as suas respectivas posições na lista
'''

valores = []  # lista vazia para armazenar os valores

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor a Posição {i}: ')))

# Encontrar o maior valor e sua posição
maior_valor = max(valores)
posicao_maior = valores.index(maior_valor)

# Encontrar o menor valor e sua posição
menor_valor = min(valores)
posicao_menor = valores.index(menor_valor)

# Mostrar os resultados
print(f"O maior valor digitado foi {maior_valor} na posição {posicao_maior+1}")
print(f"O menor valor digitado foi {menor_valor} na posição {posicao_menor+1}")
