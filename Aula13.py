#if / elif / else
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'Entrar':
    print('Você entrou no sistema')

elif entrada == 'Sair':
    print('Você saiu do sistema')

elif entrada == 'sair':
    print('Você sair no sistema!')

elif entrada == 'entrar':
    print('Você entrou o sistema!')

else:
    print('Você não digitou entrar e nem sair.')