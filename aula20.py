primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')



if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior'
        f' que o {segundo_valor=}')
else:
    print('O segundo valor é maior que o primeiro valor')


if primeiro_valor == segundo_valor:
    print("sao iguais")