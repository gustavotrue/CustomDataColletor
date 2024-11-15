# Arquivo apenas armazenando a coleta de dados para isolar responsabilidades, dividindo o código em módulos lógicos

import re
from datetime import datetime

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

# Função para coletar a data de nascimento, junto de uma verificação de formato
def coletar_data_nascimento():
    while True:
        d_nascimento = input("Digite a data de nascimento no formato ##/##/####: ")
        try:
            data = datetime.strptime(d_nascimento, "%d/%m/%Y")
            if data > datetime.now():
                print("A data de nascimento não pode estar no futuro!")
            else:
                return d_nascimento
        except ValueError:
            print("Data inválida! Use o formato ##/##/####.")

# Função para coletar CPF com validação de formato
def coletar_cpf():
    while True:
        cpf = input("Digite o CPF no formato ###.###.###-##: ")
        if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return cpf
        else:
            print("Formato inválido! Tente novamente.")

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos e não são todos iguais (ex: "111.111.111-11")
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (11 - (soma % 11)) if (soma % 11) >= 2 else 0
    
    # Verifica se o primeiro dígito verificador está correto
    if digito1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (11 - (soma % 11)) if (soma % 11) >= 2 else 0
    
    # Verifica se o segundo dígito verificador está correto
    return digito2 == int(cpf[10])

# Função para coletar endereço
def coletar_endereco():
    return input("Digite o endereço em que você reside: ")

