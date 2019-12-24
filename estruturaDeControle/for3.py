# Dicionario

produto = {'nome': 'Caneta Azul', 'preco': 17.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for chave in produto.keys():
    print(chave)


for valor in produto.values():
    print(valor)


for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)