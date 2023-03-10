from Conta import Conta

class ContaInvestimento(Conta):
    _tipo = "Conta Investimento" 
    def atualiza(self, taxa):
        self._saldo	+= self._saldo * taxa *	5