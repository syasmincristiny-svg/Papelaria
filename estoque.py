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
        return []
    with open(ARQUIVO, "r", encoding="utf-8", newline="") as arq:
        return list(csv.DicReader(arq))

def buscar_por_nome(trecho):
    """DEvolve os produtos cujo nome contém o trecho(sem diferenciar maiúsculas)."""
    trecho = trecho.strip().lower()
    achados = []
    for produto in carregar_produtos():
        if trecho in produto ["nome"].lower():
            achados.append(produto)
    return achados        

def salvar_produto(nome, preco, quantidade):
    """Acrescenta um produto no fim do CSV e devolve o produto salvo."""
    novo_arquivo = not os.path.exists(ARQUIVO) 
    produto = {
        "codigo": len(carregar_produtos()) + 1,
        "nome":nome.strip(), 
        "preco": f"{float(preco.replace(',', '-', 1)):.2f}",
        "quantidade": int(quantidade),
    }
    os.makedirs("dados", exits_Ok=True)
    with open(ARQUIVO, "a", encoding="utf-8", newline="") as arq:
        escritor =csv.Dicwiter(arq, fieldnames=CAMPOS)
        if novo_arquivo:
            escritor.writeheader()
        escritor.writerow(produto)
    return produto