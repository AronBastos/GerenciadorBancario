class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito de R${valor} realizado com sucesso.')
        else:
            print('Valor de deposito invalido. O valor deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Valor de saque invalido. O valor deve ser maior que zero.')

    def consultar_saldo(self):
        print(f'Saldo da conta {self.numero_conta}: R${self.saldo:.2f}')


# Exemplo de uso do sistema:
conta1 = ContaBancaria('12345', 1000.0)
conta2 = ContaBancaria('67890')

conta1.consultar_saldo()  # Deve mostrar o saldo inicial de R$ 1000.00
conta2.consultar_saldo()  # Deve mostrar o saldo inicial de R$ 0.00

conta1.depositar(500.0)   # Deve adicionar R$ 500.00 ao saldo da conta1
conta2.depositar(200.0)   # Deve adicionar R$ 200.00 ao saldo da conta2

conta1.sacar(200.0)       # Deve subtrair R$ 200.00 do saldo da conta1
conta2.sacar(100.0)       # Deve subtrair R$ 100.00 do saldo da conta2

conta1.consultar_saldo()  # Deve mostrar o saldo atual de R$ 1300.00
conta2.consultar_saldo()  # Deve mostrar o saldo atual de R$ 100.00
