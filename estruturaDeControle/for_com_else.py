PALAVRAS_PROIBIDAS = ('futebol', 'feligiao', 'politica')

textos = [
    'João gosta de futebol e poltica',
    'A praia foi divertida',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
 
print(texto)