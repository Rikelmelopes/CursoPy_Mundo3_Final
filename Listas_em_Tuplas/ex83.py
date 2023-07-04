'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se 
a expressão passada está com os parênteses abertos e fechados na ordem correta
'''

expressao = input("Digite uma expressão com parênteses: ")

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) == 0:
            pilha.append(caractere)
            break
        else:
            pilha.pop()

if len(pilha) == 0:
    print("Expressão válida. Os parênteses estão na ordem correta.")
else:
    print("Expressão inválida. Os parênteses não estão na ordem correta.")
