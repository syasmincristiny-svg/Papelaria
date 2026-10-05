import csv 
import os

ARQUIVO = "dados/produtos.csv"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]


def eh_numero(texto):
    """Diz se o texto é um numero positivo aceitando virgula ou ponto (ex.:3,50)."""
    texto = texto.strip().replace (",",".",1)
    return texto.replace (".", "", 1).isdigit()

def validar_produto(nome, preco, quantidade):
    """Devolve a lista de erros encontrados. Lista vazia = produtos válido."""
    erros = []
    if nome.strip() == "":
        erros.append("O nome não pode ficar vazio.")
        if not eh_numero(preco) or float(preco.replace(",",".", 1)) <= 0:
            erros.append("O preco precisa ser um numero maior que zero.")
            if not quantidade.strip().isdigit():
                erros.append("A quantidade precisa ser um numero inteiro (0 ou mais).")
             return erros
def carregar_produtos ():
    """Lê o CSV e devolve uma lsita de dicionários (um por produto)."""
    if not os.path.exits(ARQUIVO):   













