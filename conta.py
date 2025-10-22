# Importa módulo para registrar data e hora das transações

from datetime import datetime


class ContaBancaria:
    # Representa uma conta bancária vinculada a um cliente.
    # Gerencia saldo, extrato e operações como depósito e saque, com regras de limite.
    
    # Constantes de classe: definem limites padrão para saques
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500

    def __init__(self, numero, cliente):
        # Inicializa a conta com número, cliente associado, saldo zerado,
        # extrato vazio e contador de saques em 0
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def _registrar_movimentacao(self, tipo, valor):
        # Método interno para registrar uma movimentação no extrato
        # Armazena data/hora e descrição da operação
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append(f"[{data_hora}] {tipo}: R$ {valor:.2f}")

    def depositar(self, valor):
        # Realiza depósito se o valor for positivo
        if valor > 0:
            self.saldo += valor
            self._registrar_movimentacao("Depósito", valor)
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Valor inválido.")

    def sacar(self, valor):
        # Realiza saque com validações:
        # - saldo suficiente
        # - valor dentro do limite permitido
        # - número de saques não excedido
        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print("❌ Operação falhou! Valor excede o valor limite diário por saque.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("❌ Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self._registrar_movimentacao("Saque", valor)
            self.numero_saques += 1
            print("✅ Saque realizado com sucesso!")
        else:
            print("❌ Valor inválido.")

    def mostrar_extrato(self):
        # Exibe o extrato da conta com todas as movimentações registradas
        print("\n================ EXTRATO ================")
        print(f"Cliente: {self.cliente.nome} {self.cliente.sobrenome} | CPF: {self.cliente.cpf} | Conta: {self.numero}")
        print("------------------------------------------")
        print("\n".join(self.extrato) if self.extrato else "Nenhuma movimentação.")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
