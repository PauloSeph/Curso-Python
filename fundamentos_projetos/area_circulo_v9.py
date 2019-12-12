#!python
from math import pi

# def é a palavra reservada para definir uma função.
# Aqui estamos dando um retorno para função, para ser usada varias vezes, não so imprimindo.
def circulo(raio):
    return pi * float(raio) ** 2


# criando uma nova variável que vai puxar a função(area = circulo(raio)) que vai ser aplicada no console, ecaso queira puxar ela, ou circulo.
# o print vai continuar aparecendo, mas não sera somente um print. lembrando que está area = resultado do raio.
if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Area do circulo', area)

