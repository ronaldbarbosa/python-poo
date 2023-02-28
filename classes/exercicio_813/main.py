from Cliente import Cliente
from Conta import Conta

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
conta1 = Conta("123-4", cliente1, 0.0)
conta2 = Conta("432-1", cliente2, 1000.0)

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
conta1.historico.imprime()
print("\n=============================================================\n")
print("{} - cliente desde: ".format(cliente2.nome), end="")
print("{}/{}/{}".format(conta2.data_abertura.dia, conta2.data_abertura.mes, conta2.data_abertura.ano))
conta2.historico.imprime()

