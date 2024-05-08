#Operadores lógicos 
#and or not
#and - Todas as condições precisam ser verdadeiras 
#Se qualquer valor for considerado falso, a expressão será validada naquele valor 
#São considerados falsy
# 0 0.0'' false 
#Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '12346'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrada')

else:
    print('Sair')

#Avaliação de curto circuito
print( True and False and True)