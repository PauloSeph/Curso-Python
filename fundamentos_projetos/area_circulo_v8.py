#!python
from math import pi

""" Definindo uma função => circulo, puxando a variavel raio entre parenteses do circulo(raio)
 e colocando a variavel a baixo dela.
"""


def circulo(raio):
    print('Area do circulo', pi * float(raio) ** 2)


""" já que foi definido a função, então colocamos aqui, circulo(raio)
lembrando que a condição vai funcionar normalmente.
"""
if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)

# com o comando import area_circulo_v8 as (apelido) consegue por um apelido no arquivo.
# e conseguindo calcular s08.circulo(22.3)