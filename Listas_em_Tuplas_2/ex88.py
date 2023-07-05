'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão 
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
'''

import random

quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

jogos = []
for _ in range(quantidade_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(sorted(jogo))

print("\nAqui estão os seus palpites:")
for jogo in jogos:
    print(jogo)
