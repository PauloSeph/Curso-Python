#!python
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


# pode passar valores, para começar no caso o segundo parametro.
if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20, (4, 5)):
        print(fib)