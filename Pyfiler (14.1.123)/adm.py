# Arquivo com funcionalidades restritas

from pessoa_class import( Pessoa )
import os
import json
from dados import pessoas

usuario = "adm"
senha = "123"

# Nome do arquivo para salvar os dados dos usuários
ARQUIVO_USUARIOS = "usuarios.json"

def salvar_usuarios_em_arquivo(pessoas):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        if not pessoas:
            json.dump([], arquivo, indent=4)
        else:
            json.dump([p.__dict__ for p in pessoas], arquivo, indent=4)

# Função para carregar os dados dos usuários de um arquivo JSON
def carregar_usuarios_do_arquivo():
    global pessoas
    if not os.path.exists(ARQUIVO_USUARIOS):
        pessoas = []
        return

    if os.path.getsize(ARQUIVO_USUARIOS) == 0:
        pessoas = []
        return

    try:
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            lista_pessoas = json.load(arquivo)
            pessoas = [Pessoa(**dados) for dados in lista_pessoas]
    except json.JSONDecodeError:
        print("Erro ao carregar dados: arquivo corrompido. Inicializando lista vazia.")
        pessoas = []

def exibir_todos_usuarios_arquivo():
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Nenhum usuário cadastrado.")
        return
    
    # Carrega os dados do arquivo
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        lista_pessoas = json.load(arquivo)
        
        # Verifica se há usuários cadastrados no arquivo
        if not lista_pessoas:
            print("Nenhum usuário cadastrado.")
            return

        # Exibe os dados de cada usuário
        print("Lista de todos os usuários cadastrados:")
        for dados in lista_pessoas:
            # Exibe cada campo do usuário
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Data de Nascimento: {dados['d_nascimento']}")
            print(f"CPF: {dados['cpf']}")
            print(f"Endereço: {dados['endereco']}")
            print("-" * 30)
    
    input("\nPressione Enter para continuar...")  # Pausa após exibir todos os usuários
