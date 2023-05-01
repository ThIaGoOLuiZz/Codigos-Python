from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f"Depositado R${valor}!")             #Vai chamar a função detalhes apos alterar o saldo

    def detalhes(self, msg=""):
        print(f"O seu saldo é de R${self.saldo:.2f} \n{msg}")


### Conta poupança

class ContaPoupanca(Conta):
     def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >=0:
            self.saldo -= valor
            self.detalhes(f"Sacado R${valor}!")

            return self.saldo
        
        print("Não foi possível concluir o saque!!\n")
        self.detalhes(f"saque no valor de R${valor} negado!!")

### Conta Corrente

class ContaConrrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >=limite_maximo:
            self.saldo -= valor
            self.detalhes(f"Sacado R${valor}!")

            return self.saldo
            
        print("Não foi possível concluir o saque!!\n")
        print(f"Seu limite é de {self.limite:.2f}")
        self.detalhes(f"saque no valor de R${valor} negado!!")


if __name__ == "__main__":        #So vai executar se o modulo for o __main__
    conta_Poupanca1 = ContaPoupanca(0000, 123456, 0)
    conta_Corrente1 = ContaConrrente(0000, 123456, 0, 100)

    conta_Poupanca1.sacar(1)
    conta_Poupanca1.depositar(10)
    conta_Poupanca1.sacar(5)
    print("\n")
    conta_Corrente1.sacar(1)
    conta_Corrente1.depositar(10)
    conta_Corrente1.sacar(1000)
