'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
'''

numeros = [[], []]  # Lista única para armazenar os números separados em pares e ímpares

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        numeros[0].append(numero)  # Adiciona número par à primeira lista
    else:
        numeros[1].append(numero)  # Adiciona número ímpar à segunda lista

numeros[0].sort()
numeros[1].sort()

print("Valores pares em ordem crescente:", numeros[0])
print("Valores ímpares em ordem crescente:", numeros[1])
