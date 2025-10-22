from operacoes import menu_admin, menu_cliente
from admin import cadastrar_cliente, listar_clientes, relatorio_geral
import csv
from cliente import ARQUIVO_CLIENTES, Cliente
from conta import ContaBancaria


def main():
    # Loop principal do sistema: exibe o menu inicial e direciona para administração ou cliente
    while True:
        escolha = input("""
=== MENU PRINCIPAL ===
[1] Administração
[2] Cliente
[0] Sair
=> """)

        # ---------------- MENU ADMIN ----------------
        if escolha == "1":
            # Loop do menu de administração: permite cadastrar e listar clientes
            while True:
                opcao = menu_admin()
                if opcao == "1":
                    cadastrar_cliente()
                elif opcao == "2":
                    listar_clientes()
                elif opcao == "3":
                    relatorio_geral()
                elif opcao == "4":
                    break
                else:
                    print("❌ Opção inválida.")

        # ---------------- MENU CLIENTE ----------------
        elif escolha == "2":
            # Solicita CPF para localizar cliente e conta
            cpf = input("Informe seu CPF: ")

            conta = None
            # Verifica se o arquivo de clientes existe e busca o cliente pelo CPF
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
                # Caso o CPF não seja encontrado
                print("❌ Nenhuma conta encontrada para este CPF.")
                continue

            # Menu de operações do cliente
            while True:
                opcao = menu_cliente()
                if opcao == "d":
                # Depósito com validação de entrada
                    try:
                        valor = float(input("Valor do depósito: "))
                        conta.depositar(valor)
                    except ValueError:
                        print("❌ Entrada inválida. Digite um número.")
                elif opcao == "s":
                # Saque com validação de entrada
                    try:
                        valor = float(input("Valor do saque: "))
                        conta.sacar(valor)
                    except ValueError:
                        print("❌ Entrada inválida. Digite um número.")
                elif opcao == "e":
                # Exibe extrato da conta
                    conta.mostrar_extrato()
                elif opcao == "q": # Sai do menu cliente
                    break
                else:
                    print("❌ Opção inválida.")

        # ---------------- SAIR ----------------
        elif escolha == "0":
            # Encerra o programa
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
