'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta 
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
valores = []  

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))

    posicao = 0
    while posicao < len(valores) and valor > valores[posicao]:
        posicao += 1

    valores.insert(posicao, valor)

print("Valores digitados em ordem crescente:")
for valor in valores:
    print(valor)
