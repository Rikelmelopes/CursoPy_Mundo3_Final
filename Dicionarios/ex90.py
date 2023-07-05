'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela
'''

alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    media = float(input("Digite a média do aluno: "))
    
    situacao = 'Aprovado' if media >= 7.0 else 'Reprovado'
    
    alunos[nome] = {'Média': media, 'Situação': situacao}

print("\n=== Situação dos Alunos ===")
for nome, info in alunos.items():
    print(f"Aluno: {nome}")
    print(f"Média: {info['Média']}")
    print(f"Situação: {info['Situação']}")
    print("==========================")
