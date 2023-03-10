from Cliente import Cliente
from Conta import Conta
from Funcionario import Funcionario
from Gerente import Gerente
from ControleDeBonificacoes import ControleDeBonificacoes
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from ContaInvestimento import ContaInvestimento

# conta = Conta()
# print(type(conta))

# Por ser uma liguagem dinâmica, Python permite modificar o objeto em tempo de execução
# Nesse caso, foi adicionado o atributo "titular" ao objeto
# Vale lembrar, que a modificação do ojbjeto em tempo de execução não garante que toda instância da classe vai ter o atributo
# conta.titular = "Ronald"
# print(conta.titular)

## Métodos mágicos:  métodos iniciados e terminados com dois underscores que são chamados pelo interpretador

cliente1 = Cliente("Ronald", "Barbosa", '123456789-10')
cliente2 = Cliente("Maria", "Rodrigrues", '987654321-01')
conta1 = ContaCorrente("123-4", cliente1, 0.0)
conta2 = ContaPoupanca("432-1", cliente2, 1000.0)

print("\n=============================================================\n")

conta1.extrato()
print("\n=============================================================\n")
conta2.extrato()

conta2.transfere_para(conta1, 500.0)
conta1.saca(200.0)
conta2.deposita(1000.0)
print("\n=============================================================\n")

print("{} - cliente desde: ".format(cliente1.nome), end="")
print("{}/{}/{}".format(conta1.data_abertura.dia, conta1.data_abertura.mes, conta1.data_abertura.ano))
conta1._historico.imprime()
print("\n=============================================================\n")
print("{} - cliente desde: ".format(cliente2.nome), end="")
print("{}/{}/{}".format(conta2.data_abertura.dia, conta2.data_abertura.mes, conta2.data_abertura.ano))
conta2._historico.imprime()

print("\n=============================================================\n")

print("Total de contas: {}".format(Conta.get_total_contas()))

print("\n=============================================================\n")
print("\n=============================================================\n")

funcionario = Gerente("Ronald", "11111111111", 2000.0, '321', 2)
gerente = Gerente("Amelia", '22222222222', 5000.0, '123', 15)
print(vars(funcionario))
print(funcionario.get_bonificacao())
print(vars(gerente))
print(gerente.get_bonificacao())

print("\n=============================================================\n")
controle = ControleDeBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)
print(f"Total: {controle.total_bonificacoes}")

cliente3 = Cliente("Rony", "Elson", "10101010101010")
controle.registra(cliente3)

print("\n=============================================================\n")

cliente_c = Cliente("Weverton", "Pereira", "99998989898")
c = ContaCorrente("645-3", cliente_c, 1000.0)
cliente_cp = Cliente("Jailson", "Barros", "2938475495")
cp = ContaPoupanca("987-2", cliente_cp, 1000.0)
cliente_cc = Cliente("Fernando", "Prass", "84375349869")
cc = ContaCorrente("754-5", cliente_cc, 1000.0)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c.pega_saldo)
print(cp.pega_saldo)
print(cc.pega_saldo)

print(cc)

print("\n=============================================================\n")

cliente_ci = Cliente('nome', 'sobrenome', 'cpf')
ci = ContaInvestimento('757', cliente_ci, 1000.0)
ci.deposita(1000.0)
ci.atualiza(0.01)
print(ci.pega_saldo)
print(ci)
print(cp)
print(cc)