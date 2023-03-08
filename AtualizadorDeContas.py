class AtualizadorDeContas():
    def __init__(self, selic, saldo_total = 0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        print(f"Saldo da conta: {conta.pega_saldo}")
        conta.atualiza(self._selic)
        print(f"Saldo final: {conta.pega_saldo}")
