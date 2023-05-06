'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Vasco.
'''

times = ('Botafogo','Fortaleza','Palmeiras','Internacional','Fluminense','Cruzeiro','Gremio','São Paulo',
        'Vasco da Gama','Atletigo-MG','Santos','Bragantino','Flamengo','Atletico-PR','Goiás','Corinthinhas',
        'Cuiaba','Coritiba','Bahia','America-MG')

print('=======TABELA DO BRASILEIRÃO========')
print('')
print(20*'======')
print(times)
print(20*'======')
print('')
print(f'Os 4 primeiros times da tabela são: {times[0:4]}')
print('')
print(20*'======')
print('')
print(f'Os 4 Ultimos times da tabela são: {times[16:20]}')
print('')
print(20*'======')
print('')
print('Tabela em ordem alfabetica')
print('')
times2 = tuple(sorted(times))
print(times2)
print('')
print(20*'======')
print('')
print(f'Vasco da gama se encontra na {times.index("Vasco da Gama")}º colocação')
print('')
print(20*'======')
