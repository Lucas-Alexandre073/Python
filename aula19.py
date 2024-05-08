#Operadores in e not 
#Strings sao interaveis 
#  0 1 2 3 4 5 
#  O t a v i o 
# -6-5-4-3-2-1
Nome =input('Digite o seu nome: ') 
print(Nome[2])
print( 10 * '-')
print(Nome[-4])
print( 10 * '-')
print('a' in Nome)
print( 10 * '-')
print('g' in Nome)
print( 10 * '-')
print('cas' in Nome)
print( 10 * '-')
print('usl' in Nome)
print( 10 * '-')
print('u' not in Nome)
print( 10 * '-')
print('z' not in Nome)
print( 10 * '-')

Encontrar = input('Digite o que deseja encontrar: ')

if Encontrar in Nome:
    print(f'{Encontrar} esta em {Nome}')
else:
    print(f'{Encontrar} nao esta em {Nome} ')

