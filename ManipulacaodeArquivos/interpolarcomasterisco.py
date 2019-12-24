"nome {} idade {}".format("Gui", 4)


# Pode usar o asterisco * para interpolar uma tupla para dentro da string.
"nome {} idade {}".format(*("Gui", 4))


# Poderia usar assim também:
valores = ("gui", 4)
"nome {} idade {}".format(valores[0], valores[1])


# Deixando mais simples usando o asterisco *
valores = ("gui", 4)
"nome {} idade {}".format(*valores)


# Da mesma forma da para fazer com lista
valoresLista = ['Gui', 4]
"nome {} idade{}".format(*valoresLista)
