# if / elif / else
# se / se não se / se não
entrada = input('Você quer "entrar ou "sair"? ')

if entrada == 'entrar':                 # o if pode viver sozinho
    print('Você entrou no sistema')     # tem que ter o espacamento

    print(1234)
elif entrada =='sair':
    print('Você saiu do sistema')
else:                                   # o else pode viver sem o elif
    print('Você não digitou nem entrar e nem sair')


print('FORA DOS BLOCOS')                # suprindo a primeira condicao, ele executa esta segunda