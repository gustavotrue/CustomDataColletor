# Project name: Data Collector
# Author: Gustavo Torres
# Github: https://github.com/gustavotrue
# Linkedin: www.linkedin.com/in/gustavo-torres-91862a1b0
# Language Data: PT-BR

#----------------------------------------------------------------------------------#

# Import's
import time
import os
import json
from pessoa_class import ( Pessoa )
from dados import pessoas

from adm import (
    salvar_usuarios_em_arquivo,
    carregar_usuarios_do_arquivo,
    exibir_todos_usuarios_arquivo,
    login_adm,
    deletar_usuario
)
from coleta_dados import (
    coletar_nome,
    coletar_idade,
    coletar_data_nascimento,
    coletar_cpf,
    coletar_endereco,
    validar_cpf
)

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

logo = f"""
,-.----.
\    /  \                   ,---,.             ,--,
|   :    \                ,'  .' |   ,--,    ,--.'|
|   |  .\ :             ,---.'   | ,--.'|    |  | :                 __  ,-.
.   :  |: |             |   |   .' |  |,     :  : '               ,' ,'/ /|
|   |   \ :       .--,  :   :  :   `--'_     |  ' |       ,---.   '  | |' |
|   : .   /     /_ ./|  :   |  |-, ,' ,'|    '  | |      /     \  |  |   ,'
;   | |`-'   , ' , ' :  |   :  ;/| '  | |    |  | :     /    /  | '  :  /
|   | ;     /___/ \: |  |   |   .' |  | :    '  : |__  .    ' / | |  | '
:   ' |      .  \  ' |  '   :  '   '  : |__  |  | '.'| '   ;   /| ;  : |
:   : :       \  ;   :  |   |  |   |  | '.'| ;  :    ; '   |  / | |  , ;
|   | :        \  \  ;  |   :  \   ;  :    ; |  ,   /  |   :    |  ---'
`---'.|         :  \  \ |   | ,'   |  ,   /   ---`-'    \   \  /
  `---`          \  ' ; `----'      ---`-'               `----'
                  `--`
[By \x67\x75\x67\x61\x68]
"""

ARQUIVO_USUARIOS = "usuarios.json"

# Limpa a tela no Windows (comando 'cls') e no Linux/macOS (comando 'clear')
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para criar um novo usuário e adicioná-lo à lista
def novo_usuario():
    nome = coletar_nome()
    idade = coletar_idade()
    data = coletar_data_nascimento()
    
    while True:
        cpf = coletar_cpf()
        if validar_cpf(cpf):  # Verifica se o CPF é válido
            break  # Sai do loop se o CPF for válido
        else:
            print("CPF inválido! Tente novamente.")  # Aviso para CPF inválido
    
    endereco = coletar_endereco()
    nova_pessoa = Pessoa(nome, idade, data, cpf, endereco)
    pessoas.append(nova_pessoa)
    salvar_usuarios_em_arquivo(pessoas)
    print("Novo usuário adicionado com sucesso!")
    input("\nPressione Enter para continuar...")  # Pausa após adicionar o usuário

# Função para exibir dados de uma pessoa com esclha de como buscar
def exibir_dados_usuario():
    limpar_tela()  # Limpa a tela ao mostrar o menu
    print("Escolha um método de busca:")
    print("1 >>> Nome")
    print("2 >>> Idade")
    print("3 >>> Data de nascimento")
    print("4 >>> CPF")
    print("5 >>> Voltar ao menu principal")

    metodo = input("Escolha uma opção: ")
    if metodo == "1":
        buscar_usuario_por_nome()

    elif metodo == "2":
        exibir_dados_usuario_idade()

    elif metodo == "3":
        exibir_dados_usuario_d_nascimento()

    elif metodo == "4":
        exibir_dados_usuario_cpf()

    elif metodo == "5":
        print("Voltando ao menu principal...")
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")  # Pausa se a opção for inválida

# Função para exibir dados de uma pessoa com base no nome
def buscar_usuario_por_nome():
    nome_busca = input("Nome: ")
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return
    
    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)
        
        # Busca o usuário pelo nome
        for dados in lista_pessoas:
            if dados['nome'].lower() == nome_busca.lower():  # Ignora diferenças de maiúsculas/minúsculas
                print("Usuário encontrado!")
                print(f"Nome: {dados['nome']}")
                print(f"Idade: {dados['idade']}")
                print(f"Data de Nascimento: {dados['d_nascimento']}")
                print(f"CPF: {dados['cpf']}")
                print(f"Endereço: {dados['endereco']}")
                print("-" * 30)
                input("\nPressione Enter para continuar...")
                return

        # Se nenhum usuário for encontrado
        print("Usuário não encontrado.")
        input("\nPressione Enter para continuar...")

# Função para exibir dados de uma pessoa com base na idade
def exibir_dados_usuario_idade():
    idade_busca = input("Idade: ")
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return
    
    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)
        
        # Busca o usuário pelo nome
        for dados in lista_pessoas:
            if dados['idade'] == idade_busca:
                print("Usuário encontrado!")
                print(f"Nome: {dados['nome']}")
                print(f"Idade: {dados['idade']}")
                print(f"Data de Nascimento: {dados['d_nascimento']}")
                print(f"CPF: {dados['cpf']}")
                print(f"Endereço: {dados['endereco']}")
                print("-" * 30)
                input("\nPressione Enter para continuar...")
                return

        # Se nenhum usuário for encontrado
        print("Usuário não encontrado.")
        input("\nPressione Enter para continuar...")

# Função para exibir dados de uma pessoa com base na data de nascimento
def exibir_dados_usuario_d_nascimento():
    data_busca = input("Data: ")
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return
    
    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)
        
        # Busca o usuário pelo nome
        for dados in lista_pessoas:
            if dados['d_nascimento'] == data_busca:
                print("Usuário encontrado!")
                print(f"Nome: {dados['nome']}")
                print(f"Idade: {dados['idade']}")
                print(f"Data de Nascimento: {dados['d_nascimento']}")
                print(f"CPF: {dados['cpf']}")
                print(f"Endereço: {dados['endereco']}")
                print("-" * 30)
                input("\nPressione Enter para continuar...")
                return

        # Se nenhum usuário for encontrado
        print("Usuário não encontrado.")
        input("\nPressione Enter para continuar...")

# Função para exibir dados de uma pessoa com base no CPF
def exibir_dados_usuario_cpf():
    cpf_busca = input("CPF: ")
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return
    
    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)
        
        # Busca o usuário pelo CPF
        for dados in lista_pessoas:
            if dados['cpf'] == cpf_busca:
                print("Usuário encontrado!")
                print(f"Nome: {dados['nome']}")
                print(f"Idade: {dados['idade']}")
                print(f"Data de Nascimento: {dados['d_nascimento']}")
                print(f"CPF: {dados['cpf']}")
                print(f"Endereço: {dados['endereco']}")
                print("-" * 30)
                input("\nPressione Enter para continuar...")
                return

        # Se nenhum usuário for encontrado
        print("Usuário não encontrado.")
        input("\nPressione Enter para continuar...")


# Função para atualizar dados de um úsuario com base no CPF
def atualizar_usuario():
    login_adm()
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return

    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)

    cpf_busca = input("Digite o CPF do usuário para atualizar os dados: ")

    # Busca o usuário pelo CPF
    for pessoa in lista_pessoas:
        if pessoa["cpf"] == cpf_busca:
            print("Usuário encontrado!")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Data de Nascimento: {pessoa['d_nascimento']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Endereço: {pessoa['endereco']}")
            print("-" * 30)

            # Menu de atualização
            print("\nEscolha o dado que deseja atualizar:")
            print("1 >>> Nome")
            print("2 >>> Idade")
            print("3 >>> Data de Nascimento")
            print("4 >>> CPF")
            print("5 >>> Endereço")
            print("6 >>> Cancelar")
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                pessoa["nome"] = coletar_nome()
                print("Nome atualizado com sucesso!")
                time.sleep(3)
            elif opcao == "2":
                pessoa["idade"] = coletar_idade()
                print("Idade atualizada com sucesso!")
                time.sleep(3)
            elif opcao == "3":
                pessoa["d_nascimento"] = coletar_data_nascimento()
                print("Data de nascimento atualizada")
                time.sleep(3)
            elif opcao == "4":
                while True:
                    novo_cpf = coletar_cpf()
                    if validar_cpf(novo_cpf):
                        pessoa["cpf"] = novo_cpf
                        print("CPF atualizado com sucesso!")
                        break
                    else:
                        print("CPF inválido! Tente novamente.")
            elif opcao == "5":
                pessoa["endereco"] = coletar_endereco()
                print("Endereço atualizado com sucesso!")
            elif opcao == "6":
                print("Atualização cancelada.")
                return
            else:
                print("Opção inválida.")

            # Salva as alterações no arquivo
            with open(ARQUIVO_USUARIOS, "w") as arquivo:
                json.dump(lista_pessoas, arquivo, indent=4)
            print("Dados atualizados com sucesso!")
            return
    print("Usuário não encontrado.")

# Função do menu principal
def menu():
    limpar_tela()  # Limpa a tela ao mostrar o menu
    print(logo)
    print("Menu de opções:")
    print("1 >>> Novo Usuário")
    print("2 >>> Buscar dados de um usuário")
    print("3 >>> Atualizar dados de um usuário")
    print("4 >>> Exibir todos os usuários")
    print("5 >>> Deletar usuario")
    print("6 >>> Sair do programa")
    return input("Escolha uma opção: ")

# Loop principal do programa
while True:
    carregar_usuarios_do_arquivo()
    opcao = menu()
    
    if opcao == "1":
        novo_usuario()
    elif opcao == "2":
        exibir_dados_usuario()
    elif opcao == "3":
        atualizar_usuario()
    elif opcao == "4":
        login_adm()
        exibir_todos_usuarios_arquivo()
    elif opcao == "5":
        login_adm()
        deletar_usuario()
    elif opcao == "6":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")  # Pausa se a opção for inválida
