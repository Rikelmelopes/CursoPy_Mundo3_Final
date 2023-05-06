'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

n1 = (int(input('Digite o primeiro numero: ')),
int(input('Digite o segundo numero: ')),
int(input('Digite o terceiro numero: ')),
int(input('Digite o quarto numero: ')))  
print(f'Os numeros digitados foram: {n1}')
print(f'O numero 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}ª posição') 
else:
    print('O valor 3 não foi digitado')
print('os valores pares digitados foram' , end= ' ')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
    