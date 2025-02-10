#Bank Account management system



class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = 0  # Inicializa _saldo
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print('valor de saque não pode ser menor que zero')
        
        else: 
            self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:

            if valor < 0:
                print('valor de saque não pode ser menor que zero')

            else:
              self._saldo -=valor
              print(f'Saque de {valor} realizado com sucesso!')
        
  
        else:
            print('Saldo insuficiente')

    def exibir_saldo(self):
        print(f'Valor total em saldo é de: {self._saldo:.2f}')

    @property
    def saldo(self):
        return self._saldo

#Checar se saldo está zerado
    @saldo.setter
    def saldo(self, valor):
        if (valor < 0):
            novo_valor = self._saldo + valor
            if novo_valor < self._saldo:
                print(f'Valor indisponível em conta. Seu saldo atual é de: {self._saldo}')

            else:
                self._saldo = novo_valor

        else:
            self._saldo = valor
        


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
        print(f'Saldo: R${self._saldo:.2f} | Cheque Especial: R${self._cheque_especial:.2f}')


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo=0, taxa_rendimento = 0.005):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_rendimento = taxa_rendimento #0.5% ao mês, por exemplo

    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.taxa_rendimento
        print(f'Rendimento aplicado! Novo saldo: R${self._saldo:.2f}')
        



conta1 = ContaCorrente(123456, "Giovanni", 120)
conta2 = ContaPoupanca(123457, "Giovanni", 300)
conta3 = ContaBancaria(145871, "Giovanni", 1000)

conta3.exibir_saldo()
conta3.sacar(1000)
conta3.exibir_saldo()
conta3.depositar(-1000)



"""
# Cria uma conta corrente e testa o saque com cheque especial
conta_corrente = ContaCorrente(123456, "Giovanni", saldo=100)
conta_corrente.sacar(300)
conta_corrente.exibir_saldo()  # Saldo: R$0.00 | Cheque Especial: R$300.00

# Cria uma conta poupança e aplica rendimento
conta_poupanca = ContaPoupanca(123457, "Giovanni", saldo=1000)
conta_poupanca.aplicar_rendimento()  # Rendimento aplicado! Novo saldo: R$1005.00"""