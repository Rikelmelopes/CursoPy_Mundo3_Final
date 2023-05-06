'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

cont = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez'
        'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete',
        'Dezoito','Dezenove','Vinte')

while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('tente novamente. ', end='')
print(f'Voce digitou o numero {cont[numero]}')