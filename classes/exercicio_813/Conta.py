from Historico import Historico
from Data import Data

class Conta:
    # Método que inicializa o objeto
    # Esse não é o método construtor. O método __new__() é o construtor, e é chamado antes do __init__() pelo interpretador do python
    # O método __init__() recebe a instância (self) do método __new__() 
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.data_abertura = Data()
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.trasacoes.append("Depósito: {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.trasacoes.append("Saque: {}".format(valor))
            return True

    def extrato(self):
        print("Numero da conta: {}".format(self.numero))
        print("Titular: {} {}".format(self.titular.nome, self.titular.sobrenome))
        print("CPF: {}".format(self.titular.cpf))
        print("Saldo: {}".format(self.saldo))
        self.historico.trasacoes.append("Extrato: saldo de {}".format(self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.trasacoes.append("Transferência de {} para a conta {}".format(valor, destino.numero))
            return True