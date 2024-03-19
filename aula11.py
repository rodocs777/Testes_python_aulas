# 1. (n + n) >> primeiros a serem executados
# 2. ** >> depois a mais forte é a potenciacao ou exponenciacao
# 3. * /  // %  >> multiplicacao, divisao, divisao inteira e modulo
# 4. + - >> mais ou menos
conta_1 = 1 + 1 ** 5 + 5 #1024
print(conta_1)


# correcao para ser 1024
conta_1 = (1 + 1) ** (5 + 5) #1024
print(conta_1)


conta_1 = (1 + 1) ** (5 + 5) #1024
conta_1 = 'qualquer coisa'
print(conta_1)


conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) #1024
print(conta_1)
