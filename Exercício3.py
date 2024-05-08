primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')


if primeiro_valor > segundo_valor:
    print("Primeiro valor é maior que o segundo valor!")

elif segundo_valor > primeiro_valor:
    print('Segundo valor é maior que o primeiro valor!')

elif primeiro_valor == segundo_valor:
    print('Os valores são iguais!')

else:
    print('Use números, por favor :)')

