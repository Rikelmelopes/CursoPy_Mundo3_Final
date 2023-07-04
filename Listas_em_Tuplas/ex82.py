'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das 
três listas geradas

'''

numeros = []  
pares = []  
impares = []  

while True:
    numero = int(input("Digite um número (ou digite 0 para parar): "))

    if numero == 0:
        break

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista completa de números digitados:")
print(numeros)

print("Lista de números pares:")
print(pares)

print("Lista de números ímpares:")
print(impares)
