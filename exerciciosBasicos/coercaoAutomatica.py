from decimal import Decimal, getcontext
print(10 / 3)
print(10 // 3)
print(type(10 / 3))

print(2 + True)
print(2 + False)


# numeros

# print(dir(int))
# print(dir(float))

print(5.0.is_integer())

# deixa positivo
print((-2).__abs__())

# Importando decimal e o getcontext

print(Decimal(1) / Decimal(7))
# Obtendo precisa de 4 casas decimais
getcontext().prec = 4
print(Decimal(1) / Decimal(7))

# Retorna o maior valor
print(Decimal.max(Decimal(1), Decimal(7)))

print(dir(Decimal))

print(1.1 + 2.2)

print(Decimal(1.1) + Decimal(2.2))
