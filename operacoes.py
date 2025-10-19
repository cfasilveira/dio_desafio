def menu_admin():
    return input("""
=== MENU ADMINISTRAÇÃO ===
[1] Cadastrar cliente (já cria conta)
[2] Listar clientes
[3] Voltar ao menu principal
=> """)

def menu_cliente():
    return input("""
=== MENU CLIENTE ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """)
