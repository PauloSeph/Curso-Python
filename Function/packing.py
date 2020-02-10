def somas(*numeros):
    print(numeros)
    soma = 0
    for na in numeros:
        soma += na
    return soma


if __name__ == '__main__':
    print(somas(3, 4))


def soma_3(a, b, c):
    return a + b + c


# Unpacking
tupla_nums = (1, 2, 3)
print(soma_3(*tupla_nums))
