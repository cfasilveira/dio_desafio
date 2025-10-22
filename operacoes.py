# Exibe o menu de administração e retorna a opção escolhida pelo usuário.
# Usado para acessar funções como cadastro e listagem de clientes.
def menu_admin():
    return input("""
=== MENU ADMINISTRAÇÃO ===
[1] Cadastrar cliente (já cria conta)
[2] Listar clientes
[3] Relatório geral do banco
[4] Voltar ao menu principal
=> """)

# Exibe o menu de operações disponíveis para o cliente.
# Permite realizar depósito, saque, consultar extrato ou sair.
def menu_cliente():
    return input("""
=== MENU CLIENTE ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """)
