#!python
from math import pi

# Aqui o (input)usuario vai informa o valor do raio(que é uma variável)
# lembrando que pi já tem um valor natural.
# raio(que é uma string) foi convertido para float.
# Raio aqui será o valor que será passado pelo usuario no caso
raio = input('Informe o raio: ')
print('Area do circulo', pi * float(raio) ** 2)

