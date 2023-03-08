from Conta import Conta

class Banco():
    def __init__(self, contas = []):
        self._contas = contas

    def adiciona_conta(self, conta):
        self._contas.append(conta)

    def pega_conta(self, posicao):
        return self._contas[posicao]

    def pega_total_de_contas(self):
        return len(self._contas)