# 💳 Sistema Bancário em Python

Projeto desenvolvido como desafio prático, simulando um **sistema bancário** com cadastro de clientes, criação de contas e operações financeiras básicas.

## 🚀 Funcionalidades

- Cadastro de clientes com endereço completo (incluindo bairro).  
- Criação automática de conta vinculada ao cliente.  
- Operações bancárias: **depósito, saque e extrato**.  
- Listagem de clientes em formato de tabela.  
- Validação de CPF e número de conta para evitar duplicidade.  

## 🛠️ Tecnologias

- **Python 3**  
- Manipulação de arquivos **CSV** para persistência de dados.  
- Estruturação em **módulos** para melhor organização.  

## 📂 Estrutura do Projeto

```
desafio/
│── admin.py        # Funções administrativas (cadastro, listagem)
│── cliente.py      # Classe Cliente (POO)
│── conta.py        # Classe ContaBancaria (POO)
│── operacoes.py    # Menus e interações
│── main.py         # Ponto de entrada do sistema
│── clientes.csv    # Base de dados simples (armazenamento)
│── __init__.py
```

## 🧩 Conceitos Utilizados

### Programação Orientada a Objetos (POO)
- **Classe Cliente**: encapsula dados pessoais e endereço.  
- **Classe ContaBancaria**: gerencia saldo, extrato e operações.  
- Uso de **métodos** para depósito, saque e extrato.  
- **Encapsulamento** e **validação** de dados (CPF, data de nascimento, limites de saque).  

### Modularização
- Código dividido em **módulos** (`cliente.py`, `conta.py`, `admin.py`, etc.), facilitando manutenção e reutilização.  
- `main.py` atua apenas como **orquestrador**, chamando funções e classes dos módulos.  
- Separação clara entre **camada de dados** (CSV), **regras de negócio** (POO) e **interface de linha de comando** (menus).  

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/dio_desafio.git
   cd dio_desafio
   ```

2. Execute o programa:
   ```bash
   python3 main.py
   ```

3. Use os menus para cadastrar clientes, criar contas e realizar operações.

===================================================================================================================================================================================================

# 💳 Banking System in Python

This project was developed as a practical challenge, simulating a **banking system** with customer registration, account creation, and basic financial operations.

## 🚀 Features

- Customer registration with full address (including neighborhood).  
- Automatic account creation linked to the customer.  
- Banking operations: **deposit, withdraw, and statement**.  
- Customer listing in a formatted table.  
- CPF and account number validation to avoid duplicates.  

## 🛠️ Technologies

- **Python 3**  
- **CSV file handling** for simple data persistence.  
- **Modular code structure** for better organization.  

## 📂 Project Structure

```
desafio/
│── admin.py        # Administrative functions (register, list)
│── cliente.py      # Customer class (OOP)
│── conta.py        # BankAccount class (OOP)
│── operacoes.py    # Menus and user interaction
│── main.py         # Application entry point
│── clientes.csv    # Simple database (storage)
│── __init__.py
```

## 🧩 Key Concepts

### Object-Oriented Programming (OOP)
- **Customer class**: encapsulates personal and address data.  
- **BankAccount class**: manages balance, statement, and operations.  
- Use of **methods** for deposit, withdraw, and statement.  
- **Encapsulation** and **data validation** (CPF, birth date, withdrawal limits).  

### Modularization
- Code split into **modules** (`cliente.py`, `conta.py`, `admin.py`, etc.) for maintainability and reuse.  
- `main.py` acts as the **orchestrator**, calling functions and classes from modules.  
- Clear separation between **data layer** (CSV), **business logic** (OOP), and **CLI interface** (menus).  

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dio_desafio.git
   cd dio_desafio
   ```

2. Run the program:
   ```bash
   python3 main.py
   ```

3. Use the menus to register customers, create accounts, and perform operations.

---
