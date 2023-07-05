'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''
def cadastrar_pessoa():
    pessoa = {}
    pessoa["nome"] = input("Digite o nome da pessoa: ")
    pessoa["sexo"] = input("Digite o sexo da pessoa (M/F): ")
    pessoa["idade"] = int(input("Digite a idade da pessoa: "))
    return pessoa

pessoas = []
soma_idade = 0

numero_pessoas = int(input("Digite o número de pessoas que deseja cadastrar: "))

for i in range(numero_pessoas):
    print(f"\nCadastro da pessoa {i+1}:")
    pessoa = cadastrar_pessoa()
    pessoas.append(pessoa)
    soma_idade += pessoa["idade"]

media_idade = soma_idade / numero_pessoas

mulheres = []
acima_media = []

for pessoa in pessoas:
    if pessoa["sexo"].upper() == "F":
        mulheres.append(pessoa)
    if pessoa["idade"] > media_idade:
        acima_media.append(pessoa)

print("\n--- Resultados ---")
print("A) Quantidade de pessoas cadastradas:", numero_pessoas)
print("B) Média de idade:", media_idade)
print("C) Lista de mulheres:")
for mulher in mulheres:
    print("   ", mulher["nome"])
print("D) Lista de pessoas com idade acima da média:")
for pessoa in acima_media:
    print("   ", pessoa["nome"])
