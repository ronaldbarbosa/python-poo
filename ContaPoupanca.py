from Conta import Conta

class ContaPoupanca(Conta):
    _tipo = "Conta Poupança"
    def atualiza(self, taxa):
        self._saldo	+= self._saldo * taxa
        self._saldo += self._saldo * 0.3