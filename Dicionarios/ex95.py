'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
aproveitamento de cada jogador.
'''

def cadastrar_aproveitamento():
    jogador = {}
    jogador["nome"] = input("Digite o nome do jogador: ")
    num_partidas = int(input("Digite o número de partidas jogadas: "))
    gols = []

    for i in range(num_partidas):
        gol_partida = int(input(f"Digite a quantidade de gols feitos na partida {i+1}: "))
        gols.append(gol_partida)

    jogador["gols"] = gols
    jogador["total_gols"] = sum(gols)
    
    return jogador

def exibir_aproveitamento(jogador):
    print("\n--- Detalhes do Aproveitamento ---")
    print("Nome do jogador:", jogador["nome"])
    print("Partidas jogadas:", len(jogador["gols"]))
    print("Gols por partida:", jogador["gols"])
    print("Total de gols:", jogador["total_gols"])

jogadores = []
numero_jogadores = int(input("Digite o número de jogadores que deseja cadastrar: "))

for i in range(numero_jogadores):
    print(f"\nCadastro do jogador {i+1}:")
    jogador = cadastrar_aproveitamento()
    jogadores.append(jogador)

print("\n--- Aproveitamento dos Jogadores ---")
for jogador in jogadores:
    exibir_aproveitamento(jogador)
