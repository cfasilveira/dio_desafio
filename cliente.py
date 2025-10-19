import csv
from datetime import datetime
from pathlib import Path

ARQUIVO_CLIENTES = Path("clientes.csv")

class Cliente:
    CAMPOS = [
        "cpf", "nome", "sobrenome", "rua", "numero", "bairro", "cidade", "uf",
        "cep", "genero", "data_nascimento", "data_cadastro", "conta"
    ]

    def __init__(self, cpf, nome, sobrenome, rua, numero, bairro, cidade, uf, cep, genero, data_nascimento, conta):
        if not (cpf.isdigit() and len(cpf) == 11):
            raise ValueError("❌ CPF inválido! Deve conter 11 dígitos numéricos.")
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf.upper()
        self.cep = cep
        self.genero = genero

        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("❌ Data de nascimento inválida. Use o formato dd/mm/YYYY.")
        self.data_nascimento = data_nascimento

        self.data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.conta = conta

    def salvar(self):
        clientes = []
        if ARQUIVO_CLIENTES.exists():
            with open(ARQUIVO_CLIENTES, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                clientes = list(reader)

            # checar duplicidade de CPF e conta
            for c in clientes:
                if c["cpf"] == self.cpf:
                    raise ValueError(f"❌ Já existe um cliente cadastrado com o CPF {self.cpf}.")
                if c["conta"] == self.conta:
                    raise ValueError(f"❌ Já existe uma conta cadastrada com o número {self.conta}.")

        novo = {
            "cpf": self.cpf,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
            "genero": self.genero,
            "data_nascimento": self.data_nascimento,
            "data_cadastro": self.data_cadastro,
            "conta": self.conta
        }

        with open(ARQUIVO_CLIENTES, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(novo)

        print(f"✅ Cliente {self.nome} {self.sobrenome} cadastrado com sucesso! Conta {self.conta} criada.")

    @staticmethod
    def listar():
        if not ARQUIVO_CLIENTES.exists():
            print("Nenhum cliente cadastrado.")
            return

        with open(ARQUIVO_CLIENTES, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            print("\n=== Lista de Clientes ===")
            print(f"{'CPF':<12} {'Nome':<15} {'Sobrenome':<15} {'Conta':<10} {'Cidade':<12} {'UF':<3} {'Cadastro':<20}")
            print("-" * 90)
            for row in reader:
                print(f"{row['cpf']:<12} {row['nome']:<15} {row['sobrenome']:<15} "
                      f"{row.get('conta','-'):<10} {row['cidade']:<12} {row['uf']:<3} {row['data_cadastro']:<20}")
