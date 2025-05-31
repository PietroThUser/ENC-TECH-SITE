from bs4 import BeautifulSoup, NavigableString

def formatter(content):
    soup = BeautifulSoup(features="html.parser")
    lines = content.split("\n")
    actual_ul = None  # Controla a UL atual

    image_index = 1

    for line in lines:
        line = line.strip()
        
        if line.startswith("### "):
            h3 = soup.new_tag("h3")
            h3.string = line.replace("### ", "")
            soup.append(h3)
            actual_ul = None  # Reseta ao criar novo cabeçalho

        elif line.startswith("## "):
            h2 = soup.new_tag("h2")
            h2.string = line.replace("## ", "")
            soup.append(h2)
            actual_ul = None

        elif line.startswith("# "):
            h1 = soup.new_tag("h1")
            h1.string = line.replace("# ", "")
            soup.append(h1)
            actual_ul = None

        elif line.startswith("- "):
            li = soup.new_tag("li")
            li.string = line.replace("- ", "")
            
            if actual_ul is None:  # Cria nova UL se não existir
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

def formatter_roadmap(roadmap):
    soup = BeautifulSoup(features="html.parser")
    lines = roadmap.split("\n")
    roadmapHome_index = 1

    for line in lines:
        line = line.strip()

        if line.startswith("- "):
            div = soup.new_tag("div")
            div_text = soup.new_tag("div")
            div_text["class"] = "div_text"
            div["id"] = roadmapHome_index
            div["style"] = "display: none;"

            i = soup.new_tag("i")
            i["class"] = "fa-solid fa-play"

            btn = soup.new_tag("button")
            btn["onclick"] = f"window.location.href = '/curso{roadmapHome_index}'"
            btn_a = soup.new_tag("a")
            btn_a["href"] = f"/curso/{roadmapHome_index}"
            btn_p = soup.new_tag("p")
            btn_p.string = "Começar"
            btn_p["class"] = "btn_p"

            div_btn = soup.new_tag("div")
            div_btn["class"] = "div_btn"

            id_p = soup.new_tag("p")
            id_p.string = f"Lição {roadmapHome_index}"
            id_p["class"] = "p"

            a = soup.new_tag("a")
            a.string = line.replace("-", "")

            roadmapHome_index += 1

            btn_a.append(i)
            btn.append(btn_p)
            btn.append(btn_a)
            div_text.append(id_p)
            div_text.append(a)
            div.append(div_text)
            div_btn.append(btn)
            div.append(div_btn)
            soup.append(div)

    return soup.prettify()