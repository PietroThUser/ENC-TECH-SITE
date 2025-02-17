from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

def HTML_CONVERTER(conteudo):
    soup = BeautifulSoup(features="html.parser")
    linhas = conteudo.split("\n")
    ul_atual = None  # Controla a UL atual

    for linha in linhas:
        linha = linha.strip()
        
        if linha.startswith("### "):
            h3 = soup.new_tag("h3")
            h3.string = linha.replace("### ", "", 1).strip()
            soup.append(h3)
            ul_atual = None  # Reseta ao criar novo cabeçalho

        elif linha.startswith("## "):
            h2 = soup.new_tag("h2")
            h2.string = linha.replace("## ", "", 1).strip()
            soup.append(h2)
            ul_atual = None

        elif linha.startswith("# "):
            h1 = soup.new_tag("h1")
            h1.string = linha.replace("# ", "", 1).strip()
            soup.append(h1)
            ul_atual = None

        elif linha.startswith("- "):
            li = soup.new_tag("li")
            li.string = linha.replace("- ", "", 1).strip()
            
            if not ul_atual:  # Cria nova UL se não existir
                ul_atual = soup.new_tag("ul")
                soup.append(ul_atual)
                
            ul_atual.append(li)

        elif linha == "---":
            hr = soup.new_tag("hr")
            soup.append(hr)
            ul_atual = None

        elif linha:
            p = soup.new_tag("p")
            p.string = linha
            soup.append(p)
            ul_atual = None

    return soup.prettify()

@app.route("/")
def hub_introduction():
    conteudo_convertido = []

    for i in range(1, 4):
        with open(f"templates/TEXTO{i}.txt", "r") as arquivo:
            conteudo = arquivo.read()
            HTML_CONVERTER_VAR = HTML_CONVERTER(conteudo)
            conteudo_convertido.append(HTML_CONVERTER_VAR)

    return render_template('index.html', textos=conteudo_convertido)
