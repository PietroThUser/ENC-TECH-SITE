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

            i = soup.new_tag("i")
            i["class"] = "fa-solid fa-play"

            btn = soup.new_tag("button")
            btn_a = soup.new_tag("a")
            btn_a["href"] = f"/curso/{roadmapHome_index}"

            p = soup.new_tag("p")
            p.string = f"Parte {roadmapHome_index}"

            a = soup.new_tag("a")
            a.string = line.replace("-", "")

            roadmapHome_index += 1

            btn_a.append(i)
            btn.append(btn_a)
            div.append(btn)
            div.append(p)
            div.append(a)
            soup.append(div)

        elif line.startswith("---"):
            hr = soup.new_tag("hr")

            soup.append(hr)

    return soup.prettify()