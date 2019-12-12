#!python
from math import pi

# apartir do sys consigo pegar o argumento que foi passado.
import sys


def circulo(raio):
    return pi * float(raio) ** 2

# 1. Vamos subistituir o input para propria linha de comando.
# Com o sys.argv, O Argv é a lista onde vai conter todos os argumentos passados para o seu script, no caso argv[indice] ou sejá primeiro argumento.
# No caso o 0 é o primeiro indice, e o [1] indice dois, que é o valor que será passado [1], o que queremos.
# Colocando assim no terminal ./area_circulo_v11 (valor do raio)


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo', area)

