'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
'''
listagem = ('Lapis',2.00,
            'Caneta',3.00,
            'Pochete',27.90)
print('*'*30)
print('')

print('Lista de preços')

print('')
print('*'*30)
print('')

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>5}')
print('')
print('*'*30)

