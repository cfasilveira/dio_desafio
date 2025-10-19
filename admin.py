from cliente import Cliente
from conta import ContaBancaria

contas = {}  # chave = cpf, valor = ContaBancaria

def cadastrar_cliente():
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
        cliente = Cliente(cpf, nome, sobrenome, rua, numero, bairro, cidade, uf, cep, genero, data_nascimento, conta_numero)
        cliente.salvar()
        conta = ContaBancaria(conta_numero, cliente)
        contas[cpf] = conta
    except ValueError as e:
        print(e)

def listar_clientes():
    Cliente.listar()
