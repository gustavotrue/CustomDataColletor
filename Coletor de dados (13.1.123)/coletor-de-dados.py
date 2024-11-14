# Project name: Data Collector
# Author: Gustavo Torres
# Github: https://github.com/gustavotrue
# Linkedin: www.linkedin.com/in/gustavo-torres-91862a1b0
# Language Data: PT-BR

#----------------------------------------------------------------------------------#

# Import's

import re
import time

# Class to create an object called "Person" (Possible updates)
class Pessoa:
    
    # Function to create a person
    def __init__(self, nome, idade, d_nascimento, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.d_nascimento = d_nascimento
        self.cpf = cpf
        self.endereco = endereco
        
    # Displays the person's current data
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Data de Nascimento: {self.d_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereco}")
        
    # Function to update the person's data
    def atualizar_dado(self, atributo, novo_valor):
        if hasattr(self, atributo):
            setattr(self, atributo, novo_valor)
            print(f"{atributo.capitalize()} atualizado para: {novo_valor}")
        else:
            print(f"Atributo '{atributo}' não existe.")

# Function to collect the name
def coletar_nome():
    # Loop to collect the name while the user does not type letters
    while True:
        nome = input("Nome: ")

        # Verifica se o usuário digitou apenas letras.
        if nome.isalpha():
            return nome
        else:
            print("Nome inválido, tente novamente. Somente letras são permitidas.")

# Function to collect age
def coletar_idade():
    # Loop to collect age while user does not enter numbers
    while True:
        idade = input("Idade: ")

        if idade.isalpha():
            print("A idade deve conter apenas números.")
        else:
            return idade
        
# Function to collect date of birth
def coletar_data_nascimento():
    # Loop to collect date of birth as long as it is not numbers and follows valid format
    while True:
        d_nascimento = input("Digite a data de nascimento no formato ##/##/####: ")
        
        # Checks if the date is in the correct format
        if re.fullmatch(r'\d{2}\/\d{2}\/\d{4}', d_nascimento):
            print("Data Válida")
            return d_nascimento
        else:
            print("Formato de data inválido! Atenção ao formato exigido e tente novamente.")
            
# Function to collect CPF
def coletar_cpf():     
    # Loop to collect the registration of an individual and as long as the user does not enter numbers and in the correct format
    while True:
        cpf = input("Digite o CPF no formato ###.###.###-##: ")
        
        # Checks if the CPF is in the correct format
        if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print("CPF válido.")
            return cpf
        else:
            print("Formato inválido! Tente novamente.")
            
# Function to collect address
def coletar_endereco():
    endereco = input("Digite o endereço em que você reside: ")
    return endereco

# Collection function
def novo_usuario():
    coletar_nome()
    coletar_idade()
    coletar_data_nascimento()
    coletar_cpf()
    coletar_endereco()

# Menu function
def menu():
    # Displays data manipulation options
    print("Menu de opções:")
    print("1 >>> Novo Úsuario")
    print("2 >>> Exibir meus dados")
    print("3 >>> Atualizar meus dados")
    print("4 >>> Sair do programa")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    
    if opcao == "1":
        novo_usuario()
    
    Pessoa.exibir_dados()