#Bank Account management system




class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -=valor

    def exibir_saldo(self):
        print(f'Valor total em saldo é de: {self.saldo:.2f}')
        


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo=0, cheque_especial=500):
        super().__init__(numero_conta, titular, saldo)
        self._cheque_especial = cheque_especial
        self._limite_original = cheque_especial #Guarda o limite total
        

    def sacar_(self, valor):
        limite_total = self.saldo + self._cheque_especial
        if valor <= limite_total:
            if valor > self.saldo:
                # Se o valor for maior que o saldo, usar o cheque especial
                valor_cheque = valor - self.saldo
                self.saldo = 0
                self._cheque_especial -= valor_cheque

            else:
                self.saldo -= valor

        else:
            print("Saldo e cheque especial insuficiente!")

    def exibir_saldo(self):
        print(f'Saldo: R${self.saldo:.2f} | Cheque Especial: R${self._cheque_especial:.2f}')


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo=0, taxa_rendimento = 0.005):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_rendimento = taxa_rendimento #0.5% ao mês, por exemplo

    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.taxa_rendimento
        print(f'Rendimento aplicado! Novo saldo: R${self.saldo:.2f}')
        



conta1 = ContaCorrente(123456, "Giovanni", 120)
conta2 = ContaPoupanca(123457, "Giovanni", 300)
