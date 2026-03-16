import requests
from bs4 import BeautifulSoup
import json
import string
from urllib.parse import urljoin

base_url = "https://www.atlasdasaude.pt/doencasAaZ/"
base_domain = "https://www.atlasdasaude.pt/" # Mudei o nome para não haver conflitos

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

diseases_by_letter = {}

for letter in string.ascii_lowercase:
    url = f"{base_url}{letter}"
    html_doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    disease_items = soup.find_all('div', class_='views-row')

    diseases = {}
    for item in disease_items:
        name = item.div.h3.a.text.strip()
        disease_url = item.div.h3.a['href']
        
        disease_url = urljoin(base_domain, disease_url)
        disease_page = requests.get(disease_url, headers=headers)
        
        disease_soup = BeautifulSoup(disease_page.text, 'html.parser')
        
        descricao = ""
        causas = []
        sintomas = []
        tratamento = []
        
        body_div = disease_soup.find("div", class_="field-name-body")
        
        if body_div:
            current_section = "descricao"
            for tag in body_div.find_all(["h2", "p", "ul"]):
                if tag.name == "h2":
                    heading = tag.text.strip().lower()
                    if "causa" in heading: current_section = "causas"
                    elif "sintoma" in heading: current_section = "sintomas"
                    elif "tratamento" in heading: current_section = "tratamento"
                    else: current_section = "descricao"
                elif tag.name == "p":
                    txt = tag.text.strip()
                    if txt:
                        if current_section == "descricao": descricao += (" " if descricao else "") + txt
                        elif current_section == "causas": causas.append(txt)
                        elif current_section == "sintomas": sintomas.append(txt)
                        elif current_section == "tratamento": tratamento.append(txt)
                elif tag.name == "ul":
                    for li in tag.find_all("li"):
                        txt = li.text.strip()
                        if txt:
                            if current_section == "descricao": descricao += (" " if descricao else "") + txt
                            elif current_section == "causas": causas.append(txt)
                            elif current_section == "sintomas": sintomas.append(txt)
                            elif current_section == "tratamento": tratamento.append(txt)

        print(f"Extraído: {name}")
        diseases[name] = {
            "Descrição": descricao,
            "Causas": causas,
            "Sintomas": sintomas,
            "Tratamento": tratamento
        }
        
    diseases_by_letter[letter] = diseases

with open("doencas.json", "w", encoding="utf-8") as f_out:
    json.dump(diseases_by_letter, f_out, indent=4, ensure_ascii=False)