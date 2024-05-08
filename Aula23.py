"""
Introducao ao try/except
try--> tentar executar o codigo 
except--> ocorreu um erro a executas
"""
numero_str = input('vou dobrar o numero que voce digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} e {numero_float * 2}')
except:
    print('Isso nao e um numero')

#if numero_str.isdigit():
   # numero_float = float(numero_str)
    #print(f'O dobro de {numero_str} e {numero_float * 2}')
#else:
 #   print('Isso nao e um numero')