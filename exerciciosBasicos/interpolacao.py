# pode passar duas variaveis na mesma linha

nome, idade = 'Ana', 30

#Old Version
print('nome: %s Idade: %d %d %d' % (nome, idade, True, False)) 


#Dando mesmo resultado, versão 3.6 ou menor.
print('nome: {0} Idade: {1}'.format(nome, idade))


#versão 3.7 a cima.
print(f'nome: {nome} idade: {idade} {2 ** 8 + 1}')



#template

from string import Template

Alface = 'verde'
preco = 20

recebe = Template('nome: $n Idade: $p')
print(recebe.substitute(n=Alface, p=preco))


s = Template('nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))