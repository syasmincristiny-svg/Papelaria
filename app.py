import estoque

from flask import Flask, request



from html import escape

def pagina(titulo, linhas):
    """Monta uma página de resposta simples com um link para voltar ao menu"""
    itens = "".join(f"<li>{escape(linha)}</li>" for linha in linhas)
    return f"""<!DOCTYPE html>
<html lang= "pt-BR"><head><meta charset="UTF-8><title>{escape(titulo)}</title
<link rel= "stylesheet" href="/style.css"></head>
<body><main class="cartao"><h1>{escape(titulo)}</h1><ul>{itens}</ul>
<a class="botao" href="/">Voltar ao menu</a></main></body></html>"""

app= Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def inicio ():
    return app.send_static_file("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    preco = request.form["preco"]
    quantidade = request.form["quantidade"]

    erros = estoque.validar_produto(nome, preco, quantidade)
    if erros: 
        return pagina ("não foi possível cadastrar", erros)


    produto = estoque.salavr_produto(nome, preco, quantidade)
    return pagina ("produto cadastrado!" ,[
        f"codigo:{produto['codigo']}",
        f"Nome:{produto['nome']}",
        f"preço: R$ {produto['preco']}",
        f"Quantidade:{produto['quantidade']}"
    ])

if __name__ == "__main__":
    app.run(debug=True)














