from Conta import Conta

class ContaCorrente(Conta):
    _tipo = "Conta Corrente"
    def atualiza(self, taxa):
        self._saldo	+= self._saldo * taxa
        self._saldo += self._saldo * 0.2

    def deposita(self, valor):
        self._saldo += valor - 0.10