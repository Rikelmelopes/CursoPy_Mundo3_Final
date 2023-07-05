'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
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

aproveitamento_jogador = cadastrar_aproveitamento()

print("\n--- Aproveitamento do Jogador ---")
print("Nome do jogador:", aproveitamento_jogador["nome"])
print("Partidas jogadas:", len(aproveitamento_jogador["gols"]))
print("Gols por partida:", aproveitamento_jogador["gols"])
print("Total de gols:", aproveitamento_jogador["total_gols"])
