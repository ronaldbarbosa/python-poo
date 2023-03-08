from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False

# Pode-se reescrever o método da classe mãe como um novo método, como abaixo:   
#    def get_bonificacao(self):
#        return self._salario * 0.15

# Ou aproveitar a implementação da classe mãe com um novo resultado:
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.0