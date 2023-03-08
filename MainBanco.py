from Banco import Banco
from Conta import Conta
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from AtualizadorDeContas import AtualizadorDeContas
from Cliente import Cliente

banco = Banco()
atualizador_de_contas = AtualizadorDeContas(0.02)

c = Cliente("Ronald", "Barbosa", "999999999991")
ccp = Cliente("Maria", "Rodrigues", "98765432111")
ccc = Cliente("Laura", "Rodrigues", "00000000000")

cn = Conta("123-4", c, 1000)
cp = ContaPoupanca("235-6", ccp, 1000)
cc = ContaCorrente("639-0", ccc, 1000)

banco.adiciona_conta(cn)
banco.adiciona_conta(cp)
banco.adiciona_conta(cc)

for conta in banco._contas:
    atualizador_de_contas.roda(conta)