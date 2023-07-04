'''
Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:  
                                                                                                  
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves
'''

pessoas = []  # Lista para armazenar as informações das pessoas

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":
        break
    
    peso = float(input("Digite o peso da pessoa: "))
    
    pessoa = (nome, peso)  # Tupla contendo o nome e o peso da pessoa
    pessoas.append(pessoa)  # Adiciona a pessoa à lista de pessoas

# A) Quantidade de pessoas cadastradas
quantidade_pessoas = len(pessoas)
print("Quantidade de pessoas cadastradas: ", quantidade_pessoas)

# B) Listagem das pessoas mais pesadas
pessoas.sort(key=lambda x: x[1], reverse=True)  # Ordena a lista pelo peso (maior para o menor)
maiores_pesos = [p[0] for p in pessoas if p[1] == pessoas[0][1]]  # Lista de nomes das pessoas com o maior peso

print("Pessoas mais pesadas:")
for nome in maiores_pesos:
    print(nome)

# C) Listagem das pessoas mais leves
pessoas.sort(key=lambda x: x[1])  # Ordena a lista pelo peso (menor para o maior)
menores_pesos = [p[0] for p in pessoas if p[1] == pessoas[0][1]]  # Lista de nomes das pessoas com o menor peso

print("Pessoas mais leves:")
for nome in menores_pesos:
    print(nome)
