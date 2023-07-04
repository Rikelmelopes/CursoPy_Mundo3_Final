'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente
'''

valores = []  # lista vazia para armazenar os valores

while True:
    valor = int(input("Digite um valor (ou digite 0 para sair): "))

    if valor == 0:
        break

    if valor not in valores:
        valores.append(valor)

valores.sort()  # ordenar os valores em ordem crescente

print("Valores únicos digitados (em ordem crescente):")
for valor in valores:
    print(valor)
