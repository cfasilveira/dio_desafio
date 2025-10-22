from cliente import Cliente # Importa a classe Cliente para cadastro e listagem
from conta import ContaBancaria # Importa a classe ContaBancaria para vincular conta ao cliente

contas = {} # Dicionário para armazenar contas criadas em tempo de execução (não persistido em arquivo)
            # chave = CPF do cliente, valor = objeto ContaBancaria

def cadastrar_cliente():
    # Coleta dados do cliente via input e realiza o cadastro
    print("\n=== Cadastro de Cliente + Conta ===")
    cpf = input("CPF (somente números): ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    rua = input("Rua/Av.: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF (ex: GO, SP): ")
    cep = input("CEP: ")
    genero = input("Gênero: ")
    data_nascimento = input("Data de nascimento (dd/mm/YYYY): ")
    conta_numero = input("Número da conta: ")

    try:
        # Cria Cliente e salva no arquivo CSV
        cliente = Cliente(cpf, nome, sobrenome, rua, numero, bairro, cidade, uf, cep, genero, data_nascimento, conta_numero)
        cliente.salvar()

        # Cria ContaBancaria vinculado ao cliente e armazena no dicionário local
        conta = ContaBancaria(conta_numero, cliente)
        contas[cpf] = conta
    except ValueError as e:
        # Exibe mensagens de erro de validação (CPF, data, duplicidade)
        print(e)

def listar_clientes():
    # Chama método estático da classe Cliente para exibir todos os clientes cadastrados
    Cliente.listar()
