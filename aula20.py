"""
Interpolacao basica de strings
s - string
d e i - int
f - float
x e X - hexadecimal
"""

nome = 'Lucas'
preco = 1000.954632
variavel = '%s, o preco total foi de  R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimaol de %d e %04X' % (1523, 1523))