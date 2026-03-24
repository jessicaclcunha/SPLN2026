import spacy
from spacy.matcher import Matcher
from itertools import combinations

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

pattern = [{"ENT_TYPE": "PER", "POS": "PROPN", "OP": "+"}]
matcher.add("PERSONAGEM", [pattern], greedy="LONGEST")

text = open("Harry_Potter.txt", "r", encoding="utf-8").read()
doc = nlp(text)

def nome_valido(nome):
    if not nome[0].isupper():
        return False
    invalidos = ["\n", "©", '"', "www", ".org", "Ltda", "Limited"]
    return not any(c in nome for c in invalidos)

personagens = set()
amizades = set() 

for frase in doc.sents:
    frase_doc = frase.as_doc()
    matches = matcher(frase_doc)

    pers_na_frase = []
    for id, start, end in matches:
        nome = frase_doc[start:end].text
        if nome_valido(nome):
            pers_na_frase.append(nome)
            personagens.add(nome)

    for a, b in combinations(set(pers_na_frase), 2):
        par = (min(a, b), max(a, b))  # ordena o par para evitar duplicados
        amizades.add(par)

print("--- PERSONAGENS ---")
for p in sorted(personagens):
    print(p)

print("\n--- AMIZADES ---")
for a, b in sorted(amizades):
    print(f"{a}  <->  {b}")