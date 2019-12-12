#!python
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


# Vamos fazer validações. Lembrando que o Len calcula o tamanho de uma lista.. Lembrando que conseguimos acessar os parametros pelo sys.argv
#

if __name__ == '__main__':
    # Se for TRUE, argumento for menor que 2, no caso 0(area_circulo_v11), 1(valor). Vai aparecer isso...
    if len(sys.argv) < 2:
        print("É Necessario informar o raio do circulo.")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
    else:  # Se for False, Precisa colocar um esle, para não executar os de baixo , nunca é executado os dois.
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo', area)
