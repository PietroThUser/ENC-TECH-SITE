from bs4 import BeautifulSoup

def formatter(content):
    soup = BeautifulSoup(features="html.parser")
    lines = content.split("\n")
    actual_ul = None  # Controla a UL atual

    image_index = 1

    for line in lines:
        line = line.strip()
        
        if line.startswith("### "):
            h3 = soup.new_tag("h3")
            h3.string = line.replace("### ", "").strip()
            soup.append(h3)
            actual_ul = None  # Reseta ao criar novo cabeçalho

        elif line.startswith("## "):
            h2 = soup.new_tag("h2")
            h2.string = line.replace("## ", "").strip()
            soup.append(h2)
            actual_ul = None

        elif line.startswith("# "):
            h1 = soup.new_tag("h1")
            h1.string = line.replace("# ", "").strip()
            soup.append(h1)
            actual_ul = None

        elif line.startswith("- "):
            li = soup.new_tag("li")
            li.string = line.replace("- ", "").strip()
            
            if not actual_ul:  # Cria nova UL se não existir
                actual_ul = soup.new_tag("ul")
                soup.append(actual_ul)
                
            actual_ul.append(li)

        elif line == "---":
            hr = soup.new_tag("hr")
            soup.append(hr)
            actual_ul = None

        elif line == "-IMG-":
            div_img = soup.new_tag("div")
            div_img["class"] = "div_img"

            img = soup.new_tag("img")
            img["src"] = f"../static/IMAGENS/imagem{image_index}.png"
            img["alt"] = image_index

            image_index += 1
            soup.append(div_img)
            div_img.append(img)
            actual_ul = None

        elif line:
            p = soup.new_tag("p")
            p.string = line
            soup.append(p)
            actual_ul = None

    return soup.prettify()