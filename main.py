from operacoes import menu_admin, menu_cliente
from admin import cadastrar_cliente, listar_clientes
import csv
from cliente import ARQUIVO_CLIENTES, Cliente
from conta import ContaBancaria


def main():
    while True:
        escolha = input("""
=== MENU PRINCIPAL ===
[1] Administração
[2] Cliente
[0] Sair
=> """)

        # ---------------- MENU ADMIN ----------------
        if escolha == "1":
            while True:
                opcao = menu_admin()
                if opcao == "1":
                    cadastrar_cliente()
                elif opcao == "2":
                    listar_clientes()
                elif opcao == "3":
                    break
                else:
                    print("❌ Opção inválida.")

        # ---------------- MENU CLIENTE ----------------
        elif escolha == "2":
            cpf = input("Informe seu CPF: ")

            conta = None
            if ARQUIVO_CLIENTES.exists():
                with open(ARQUIVO_CLIENTES, newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["cpf"] == cpf:
                            # Reconstruir objeto Cliente
                            cliente = Cliente(
                                row["cpf"], row["nome"], row["sobrenome"],
                                row["rua"], row["numero"], row["bairro"],
                                row["cidade"], row["uf"], row["cep"],
                                row["genero"], row["data_nascimento"],
                                row["conta"]
                            )
                            conta = ContaBancaria(row["conta"], cliente)
                            break

            if not conta:
                print("❌ Nenhuma conta encontrada para este CPF.")
                continue

            # Menu de operações do cliente
            while True:
                opcao = menu_cliente()
                if opcao == "d":
                    try:
                        valor = float(input("Valor do depósito: "))
                        conta.depositar(valor)
                    except ValueError:
                        print("❌ Entrada inválida. Digite um número.")
                elif opcao == "s":
                    try:
                        valor = float(input("Valor do saque: "))
                        conta.sacar(valor)
                    except ValueError:
                        print("❌ Entrada inválida. Digite um número.")
                elif opcao == "e":
                    conta.mostrar_extrato()
                elif opcao == "q":
                    break
                else:
                    print("❌ Opção inválida.")

        # ---------------- SAIR ----------------
        elif escolha == "0":
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
