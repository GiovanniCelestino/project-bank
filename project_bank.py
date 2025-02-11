#Bank Account management system



class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0, cpf=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = 0  # Inicializa _saldo
        self.saldo = saldo
        self.cpf = cpf
        self._historico_transacao = []
       

    def histórico_transacao(self):
        print('\nTRANSAÇÕES')
        for transacao in self._historico_transacao:
            print(transacao)
        print('')

    def depositar(self, valor):
        if valor < 0:
            print('valor de saque não pode ser menor que zero')
            
        
        else: 
            self._saldo += valor
            self._historico_transacao.append(f'Deposito de R${valor}')

    def sacar(self, valor):
        if valor <= self._saldo:

            if valor < 0:
                print('valor de saque não pode ser menor que zero')

            else:
              self._saldo -=valor
              print(f'Saque de {valor} realizado com sucesso!')
              self._historico_transacao.append(f'Saque de R${valor}')
        
  
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
    def __init__(self, numero_conta, titular, saldo=0, cpf=0, cheque_especial=500):
        super().__init__(numero_conta, titular, saldo, cpf)
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
    def __init__(self, numero_conta, titular, saldo=0, cpf=0, taxa_rendimento = 0.005):
        super().__init__(numero_conta, titular, saldo, cpf)
        self.taxa_rendimento = taxa_rendimento #0.5% ao mês, por exemplo

    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.taxa_rendimento
        print(f'Rendimento aplicado! Novo saldo: R${self._saldo:.2f}')
        


class Cliente:
    def __init__(self, nome, cpf):
      self.nome = nome
      self.conta = []
      self._cpf = []
      self.cpf = cpf

    def adicionar_conta(self, conta):
        self.conta.append(conta)

    def exibir_cliente(self):
        print(f'\nDados do Cliente: {self.nome}')
        for dados in self.conta:
            print(f'Tipo de Conta: {dados.__class__.__name__}\nNúmero da conta: {dados.numero_conta}\nCPF: {dados.cpf}')
            print()

""" 
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if valor in self._cpf:
            print(f'CPF {valor} já existe')
        else:
            self._cpf.append(valor)
"""






conta1 = ContaCorrente(123456, "Giovanni", 120, 460821)
conta2 = ContaPoupanca(123457, "Giovanni", 300, 460821)
conta3 = ContaBancaria(145871, "Giovanni", 1000, 460821)


cliente1 = Cliente('Giovanni', 460821)
cliente2 = Cliente('Carlos', 460821)

cliente1.adicionar_conta(conta1)
cliente1.adicionar_conta(conta2)
cliente1.exibir_cliente()




conta3.exibir_saldo()
conta3.sacar(1000)
conta3.exibir_saldo()
conta3.depositar(-1000)
conta3.depositar(300)
conta3.sacar(100)
conta3.sacar(80)
conta3.depositar(20)

conta3.histórico_transacao()


"""
# Cria uma conta corrente e testa o saque com cheque especial
conta_corrente = ContaCorrente(123456, "Giovanni", saldo=100)
conta_corrente.sacar(300)
conta_corrente.exibir_saldo()  # Saldo: R$0.00 | Cheque Especial: R$300.00

# Cria uma conta poupança e aplica rendimento
conta_poupanca = ContaPoupanca(123457, "Giovanni", saldo=1000)
conta_poupanca.aplicar_rendimento()  # Rendimento aplicado! Novo saldo: R$1005.00"""