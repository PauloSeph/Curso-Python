#!python
def fibonacci(quantidade, sequencia=(0, 1)):

    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


# pode passar valores, para começar no caso o segundo parametro.
if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequencia
    for fib in fibonacci(20):
        print(fib)
