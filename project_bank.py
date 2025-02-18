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
    def __init__(self,numero_conta, nome, cpf):
      self.nome = nome
      self.numero_conta = numero_conta
      self.cpf = cpf
      self.cliente = []

 
    def listar_clientes(self):
        print(f'Nome Titular: {self.nome}\nCPF Titular: {self.cpf}\nNumero Conta Titular: {self.numero_conta}')
        print()
        

conta1 = ContaCorrente(123456, "Giovanni", 120, 460820)
conta2 = ContaPoupanca(123457, "Andre", 300, 460821)
conta3 = ContaBancaria(145871, "Andre", 1000, 460821)

#CRIAR UMA REGRA PARA QUE CONTAS DIFERENTES POSSAM SER VINCULADAS NO NOME DO MESMO CLIENTE.

clientes = []

def adicionar_cliente(conta):
    for cliente in clientes:
        if cliente.cpf == conta.cpf:
            print('Cliente já existe dentro da base')
            return
    novo_cliente = Cliente(conta.numero_conta, conta.titular, conta.cpf)
    clientes.append(novo_cliente)
    novo_cliente.listar_clientes()
    


adicionar_cliente(conta3)
adicionar_cliente(conta1)


conta3.exibir_saldo()
conta3.sacar(1000)
conta3.exibir_saldo()
conta3.depositar(-1000)
conta3.depositar(300)
conta3.exibir_saldo()
conta3.sacar(100)
conta3.sacar(80)
conta3.depositar(20)

conta3.histórico_transacao()
