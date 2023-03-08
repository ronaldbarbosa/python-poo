from Conta import Conta

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        super().atualiza(taxa) 
        self._saldo += self._saldo * 0.2

    def deposita(self, valor):
        self._saldo += valor - 0.10