'''
Crie um programa que vai ler vários números e colocar em uma lista.                 
Depois disso, mostre:   
                                                                                                                                            
A) Quantos números foram digitados.                                                                                                                   
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = []  # lista vazia para armazenar os valores

while True:
    valor = int(input("Digite um número (ou digite 0 para parar): "))

    if valor == 0:
        break

    valores.append(valor)

# A) Quantidade de números digitados
quantidade = len(valores)
print(f"A quantidade de números digitados foi: {quantidade}")

# B) Lista de valores em ordem decrescente
valores.sort(reverse=True)
print("Lista de valores em ordem decrescente:")
for valor in valores:
    print(valor)

# C) Verificar se o valor 5 está na lista
if 5 in valores:
    print("O valor 5 foi digitado e está na lista.")
else:
    print("O valor 5 não foi digitado ou não está na lista.")
