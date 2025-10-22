from datetime import datetime
from pathlib import Path
import csv

ARQUIVO_MOVIMENTACOES = Path("movimentacoes.csv")

class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 1000

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def _registrar_movimentacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append(f"[{data_hora}] {tipo}: R$ {valor:.2f}")

        # Registra em arquivo global
        with open(ARQUIVO_MOVIMENTACOES, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([data_hora, tipo, f"{valor:.2f}", self.cliente.cpf, self.numero])

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self._registrar_movimentacao("Depósito", valor)
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Valor inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print("❌ Valor excede o limite por saque.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("❌ Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.numero_saques += 1
            self._registrar_movimentacao("Saque", valor)
            print("✅ Saque realizado com sucesso!")
        else:
            print("❌ Valor inválido.")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print(f"Cliente: {self.cliente.nome} {self.cliente.sobrenome} | CPF: {self.cliente.cpf} | Conta: {self.numero}")
        print("------------------------------------------")
        print("\n".join(self.extrato) if self.extrato else "Nenhuma movimentação.")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
