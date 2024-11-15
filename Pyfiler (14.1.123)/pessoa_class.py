# Arquivo armazenando apenas a classe 'Pessoa' para melhor manutenção

from coleta_dados import (
    coletar_nome,
    coletar_idade,
    coletar_data_nascimento,
    coletar_cpf,
    coletar_endereco,
    validar_cpf
)

class Pessoa:
    
    # Construtor para criar uma pessoa
    def __init__(self, nome, idade, d_nascimento, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.d_nascimento = d_nascimento
        self.cpf = cpf
        self.endereco = endereco