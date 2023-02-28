from datetime import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.trasacoes = []

    def imprime(self):
        print("Data e hora de abertura da conta: {}".format(self.data_abertura))
        print("Transações: ")
        for transacao in self.trasacoes:
            print("-", transacao)