from Historico import Historico
from Data import Data

class Conta:
    # Método que inicializa o objeto
    # Esse não é o método construtor. O método __new__() é o construtor, e é chamado antes do __init__() pelo interpretador do python
    # O método __init__() recebe a instância (self) do método __new__() 

    # Atributo de classe
    _total_contas = 0

    # __slots__: usado para não permitir que usuários das classes adicionem atributos às suas instâncias
    # Mas o seu principal propósito é fazer o interpretador alocar espaço apenas para os atributos definidos
    # __slots__ = [_numero, _titular, _saldo, _limite]

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = cliente
        self._saldo = saldo
        self.limite = limite
        self.historico = Historico()
        self.data_abertura = Data()
        Conta._total_contas += 1
    
    # Equivalente a getter
    @property
    def pega_saldo(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor
        self.historico.trasacoes.append("Depósito: {}".format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico.trasacoes.append("Saque: {}".format(valor))
            return True

    def extrato(self):
        print("Numero da conta: {}".format(self.numero))
        print("Titular: {} {}".format(self.titular.nome, self.titular.sobrenome))
        print("CPF: {}".format(self.titular.cpf))
        print("Saldo: {}".format(self._saldo))
        self.historico.trasacoes.append("Extrato: saldo de {}".format(self._saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.trasacoes.append("Transferência de {} para a conta {}".format(valor, destino.numero))
            return True
    
    # Métodos de classe servem para definir um método que opera na classe, e não em instâncias
    # cls = objeto do tipo class
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    # Métodos estaticos são usados quando não há a necessidade de receber a referência de um objeto especial (classe ou instância), funcionando com uma função comum
    # Métodos estáticos são imutáveis
    # @staticmethod
    # def get_total_contas():
    #    return Conta._total_contas