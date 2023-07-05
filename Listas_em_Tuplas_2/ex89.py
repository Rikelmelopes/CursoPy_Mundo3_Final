'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre 
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
'''

boletim = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    aluno = [nome, nota1, nota2]
    boletim.append(aluno)

print("\nBoletim:")

for aluno in boletim:
    nome = aluno[0]
    media = sum(aluno[1:]) / 2
    print(f"\nAluno: {nome}")
    print(f"Média: {media}")

    while True:
        opcao = input("Deseja ver as notas desse aluno? (S/N): ")
        if opcao.upper() == "S":
            print(f"Nota 1: {aluno[1]}")
            print(f"Nota 2: {aluno[2]}")
            break
        elif opcao.upper() == "N":
            break
        else:
            print("Opção inválida. Digite 'S' para ver as notas ou 'N' para continuar.")

print("\nPrograma encerrado.")
