# a = 'A'
# b = 'B'
# c = 1.1
# string = 'a={} b={} c={:.2f}'
# formato = string.format(a, b, c)

# print(formato)


# a = 'A'
# b = 'B'
# c = 1.1
# string = 'a={0} b={1} c={2:.2f}'
# formato = string.format(a, b, c)
# print(formato)


a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, 
    nome2=b, 
    nome3=c)
print(formato)


# O que o código abaixo exibe?

# nome = "Luiz"
# idade = 23
# formato = '{1} tem {0} anos'
# print(formato.format(nome, idade))


# nome = "Luiz"
# idade = 23
# formato = f'{nome} tem {idade:.2f} anos'