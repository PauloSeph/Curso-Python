#!python
from math import pi

# if se modulo é uma condição true or false, se for igual == main ele vai executar as ações a baixo que estão indentadas a ela, com espaços.
# ou sejá, a condição funciona para ./area_circulo_v7.py no terminal, ai vai puxar essa condição, de outra froma não.
# (import area_circulo_v7 não vai executar mais.)

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    print('Area do circulo', pi * float(raio) ** 2)
