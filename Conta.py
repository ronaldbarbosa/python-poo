from Historico import Historico
from Data import Data

class Conta:
    # Método que inicializa o objeto
    # Esse não é o método construtor. O método __new__() é o construtor, e é chamado antes do __init__() pelo interpretador do python
    # O método __init__() recebe a instância (self) do método __new__() 

    # Atributo de classe
    _total_contas = 0
    _identificador = 1

    # __slots__: usado para não permitir que usuários das classes adicionem atributos às suas instâncias
    # Mas o seu principal propósito é fazer o interpretador alocar espaço apenas para os atributos definidos
    __slots__ = ["_numero", "_titular", "_saldo", "_limite", "_historico", "_data_abertura"]

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print("Inicializando uma conta")
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._data_abertura = Data()
        Conta._total_contas += 1
        Conta._identificador += 1
    
    # Equivalente a getter
    @property
    def pega_saldo(self):
        return self._saldo

    @property
    def data_abertura(self):
        return self._data_abertura

    def deposita(self, valor):
        self._saldo += valor
        self._historico.trasacoes.append("Depósito: {}".format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.trasacoes.append("Saque: {}".format(valor))
            return True

    def extrato(self):
        print("Numero da conta: {}".format(self._numero))
        print("Titular: {} {}".format(self._titular.nome, self._titular.sobrenome))
        print("CPF: {}".format(self._titular.cpf))
        print("Saldo: {}".format(self._saldo))
        self._historico.trasacoes.append("Extrato: saldo de {}".format(self._saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self._historico.trasacoes.append("Transferência de {} para a conta {}".format(valor, destino._numero))
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