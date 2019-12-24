palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')


# list
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)


# tuple
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sabado')

for dia in dias_semana:
    print(f'Hoje é {dia}')


# conjunto(set)
for numero in {1, 2, 3, 4, 5}:
    print(numero)
