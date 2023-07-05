'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
'''

from datetime import date

def cadastrar_pessoa():
    pessoa = {}
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["ano_nascimento"] = int(input("Digite o ano de nascimento: "))
    pessoa["ctps"] = int(input("Digite o número da carteira de trabalho (CTPS): "))

    if pessoa["ctps"] != 0:
        pessoa["ano_contratacao"] = int(input("Digite o ano de contratação: "))
        pessoa["salario"] = float(input("Digite o salário: "))

    return pessoa

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def calcular_anos_aposentadoria(ano_contratacao):
    idade_aposentadoria = 65
    anos_aposentadoria = idade_aposentadoria - (date.today().year - ano_contratacao)
    return anos_aposentadoria

pessoas = []

numero_pessoas = int(input("Digite o número de pessoas que deseja cadastrar: "))

for i in range(numero_pessoas):
    print(f"\nCadastro da pessoa {i+1}:")
    pessoa = cadastrar_pessoa()
    pessoa["idade"] = calcular_idade(pessoa["ano_nascimento"])
    if pessoa["ctps"] != 0:
        pessoa["anos_aposentadoria"] = calcular_anos_aposentadoria(pessoa["ano_contratacao"])
    pessoas.append(pessoa)

print("\n--- Lista de Pessoas Cadastradas ---")
for pessoa in pessoas:
    print("\nNome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("CTPS:", pessoa["ctps"])
    if pessoa["ctps"] != 0:
        print("Ano de Contratação:", pessoa["ano_contratacao"])
        print("Salário:", pessoa["salario"])
        print("Anos até a Aposentadoria:", pessoa["anos_aposentadoria"])
