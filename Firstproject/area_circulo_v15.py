#!python

from math import pi
import sys
import errno


ERRO = '\033[94m'
NORMAL = '\033[0m'


def help():
    print("É Necessario informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(ERRO, 'O Raio deve ser um valor númerico', NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo', area)

#    caso as linhas ou colunas nao fique alinhado o comando nao funciona.
