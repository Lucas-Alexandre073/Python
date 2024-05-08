class Main:
    pass

print('Testando o programa')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Lucas", "11980837153")

conta = Conta(c1.get_nome,6565,0)

conta.deposita(100)
conta.saque(50)
conta.extrato()