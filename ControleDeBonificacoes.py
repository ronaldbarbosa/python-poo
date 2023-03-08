from Funcionario import Funcionario

class ControleDeBonificacoes():
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self,	obj):
        # Verifica se o obj tem o método
        # if(hasattr(obj, "get_bonificacao")):

        # Verifica se o objete é instância da classe
        if(isinstance(obj, Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(f"A instância de {obj.__class__.__name__} não implementa o método get_bonificacao()")

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes
