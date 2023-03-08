from Conta import Conta

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        super().atualiza(taxa)
        self._saldo += self._saldo * 0.3