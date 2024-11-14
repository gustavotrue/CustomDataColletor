# Project name: Data Collector
# Author: Gustavo Torres
# Github: https://github.com/gustavotrue
# Linkedin: www.linkedin.com/in/gustavo-torres-91862a1b0
# Language Data: PT-BR

#----------------------------------------------------------------------------------#

# Import's

import re

class Pessoa:
    
    # Construtor para criar uma pessoa
    def __init__(self, nome, idade, d_nascimento, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.d_nascimento = d_nascimento
        self.cpf = cpf
        self.endereco = endereco

    # Exibe os dados da pessoa
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Data de Nascimento: {self.d_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereco}")
        print("-" * 30)

    # Atualiza o dado de um atributo específico com um menu de opções
    def atualizar_dado(self):
        while True:
            print("Escolha o atributo que deseja atualizar:")
            print("1 >>> Nome")
            print("2 >>> Idade")
            print("3 >>> Data de Nascimento")
            print("4 >>> CPF")
            print("5 >>> Endereço")
            print("6 >>> Voltar ao menu principal")
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                self.nome = coletar_nome()
                print("Nome atualizado com sucesso!")
            elif opcao == "2":
                self.idade = coletar_idade()
                print("Idade atualizada com sucesso!")
            elif opcao == "3":
                self.d_nascimento = coletar_data_nascimento()
                print("Data de nascimento atualizada com sucesso!")
            elif opcao == "4":
                self.cpf = coletar_cpf()
                print("CPF atualizado com sucesso!")
            elif opcao == "5":
                self.endereco = coletar_endereco()
                print("Endereço atualizado com sucesso!")
            elif opcao == "6":
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Lista para armazenar objetos do tipo Pessoa
pessoas = []

# Função para coletar o nome
def coletar_nome():
    while True:
        nome = input("Nome: ")
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print("Nome inválido, tente novamente. Somente letras são permitidas.")

# Função para coletar idade
def coletar_idade():
    while True:
        idade = input("Idade: ")
        if idade.isdigit():
            return int(idade)
        else:
            print("A idade deve conter apenas números.")

# Função para coletar data de nascimento
def coletar_data_nascimento():
    while True:
        d_nascimento = input("Digite a data de nascimento no formato ##/##/####: ")
        if re.fullmatch(r'\d{2}/\d{2}/\d{4}', d_nascimento):
            print("Data Válida")
            return d_nascimento
        else:
            print("Formato de data inválido! Atenção ao formato exigido e tente novamente.")

# Função para coletar CPF
def coletar_cpf():     
    while True:
        cpf = input("Digite o CPF no formato ###.###.###-##: ")
        if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print("CPF válido.")
            return cpf
        else:
            print("Formato inválido! Tente novamente.")

# Função para coletar endereço
def coletar_endereco():
    return input("Digite o endereço em que você reside: ")

# Função para criar um novo usuário e adicioná-lo à lista
def novo_usuario():
    nome = coletar_nome()
    idade = coletar_idade()
    data = coletar_data_nascimento()
    cpf = coletar_cpf()
    endereco = coletar_endereco()
    nova_pessoa = Pessoa(nome, idade, data, cpf, endereco)
    pessoas.append(nova_pessoa)
    print("Novo usuário adicionado com sucesso!")

# Função para exibir dados de uma pessoa com base no CPF
def exibir_dados_usuario():
    cpf = input("Digite o CPF do usuário para exibir os dados: ")
    for pessoa in pessoas:
        if pessoa.cpf == cpf:
            pessoa.exibir_dados()
            return
    print("Usuário não encontrado.")

# Função para atualizar dados de uma pessoa com base no CPF
def atualizar_dados_usuario():
    cpf = input("Digite o CPF do usuário para atualizar os dados: ")
    for pessoa in pessoas:
        if pessoa.cpf == cpf:
            pessoa.atualizar_dado()
            return
    print("Usuário não encontrado.")

# Função para exibir todos os usuários cadastrados
def exibir_todos_usuarios():
    if not pessoas:
        print("Nenhum usuário cadastrado.")
    else:
        print("Lista de todos os usuários cadastrados:")
        for pessoa in pessoas:
            pessoa.exibir_dados()

# Função do menu principal
def menu():
    print("Menu de opções:")
    print("1 >>> Novo Usuário")
    print("2 >>> Exibir dados de um usuário")
    print("3 >>> Atualizar dados de um usuário")
    print("4 >>> Exibir todos os usuários")
    print("5 >>> Sair do programa")
    return input("Escolha uma opção: ")

# Loop principal do programa
while True:
    opcao = menu()
    
    if opcao == "1":
        novo_usuario()
    elif opcao == "2":
        exibir_dados_usuario()
    elif opcao == "3":
        atualizar_dados_usuario()
    elif opcao == "4":
        exibir_todos_usuarios()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
