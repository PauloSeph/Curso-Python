
print('    teste abc    ')

# tira os espaços da borda da string, nas laterais.
print('   teste abc '.strip())

# aqui vai remover os 0 mas vai deixar os espaços em branco
print('000000 teste abc 000000'.strip('0'))

# podendo chamar o strip de forma encadeada para tira os espaços.
print('000000 teste abc 000000'.strip('0').strip())
