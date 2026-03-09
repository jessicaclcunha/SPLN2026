import re
import json

f = open("medicina.xml", encoding="utf-8")

# extrair fragmentos: (page, col, top, left, font, text)
fragmentos = []
page = 0
for linha in f:
    m_page = re.search(r'<page number="(\d+)"', linha)
    if m_page:
        page = int(m_page.group(1))
        continue

    m = re.search(r'top="(\d+)" left="(\d+)"[^>]*font="(\d+)"[^>]*>(.*)</text>', linha)
    if not m:
        continue
    top, left, font = int(m.group(1)), int(m.group(2)), m.group(3)
    texto = re.sub(r"<[^>]+>", "", m.group(4)).strip()
    if texto:
        col = 0 if left < 340 else 1
        fragmentos.append((page, col, top, left, font, texto))

f.close()

# ordenar: página → coluna → top → left
fragmentos.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

# detectar inícios de entrada: font 2 ou 3 + número no início
def e_entrada(frag):
    return frag[4] in ("2","3") and re.match(r'\s*\d+\s+\S', frag[5])

starts = [i for i, f in enumerate(fragmentos) if e_entrada(f)]

# reconstruir linhas de um bloco, preservando font
def bloco_linhas(i, j):
    linhas = {}
    for page, col, top, left, font, txt in fragmentos[i:j]:
        linhas.setdefault((page, col, top), []).append((left, font, txt))
    resultado = []
    for key in sorted(linhas.keys()):
        parts = sorted(linhas[key], key=lambda x: x[0])
        texto = " ".join(t for _, _, t in parts)
        font  = parts[0][1]
        resultado.append({"font": font, "text": texto})
    return resultado

# processar um conceito
def processar(linhas):
    c = "\n".join(l["text"] for l in linhas)
    c = re.sub(r"SIN\.-",  "@SIN.-",  c)
    c = re.sub(r"VAR\.-",  "@VAR.-",  c)
    c = re.sub(r"Nota\.-", "@Nota.-", c)
    c = re.sub(r"(?m)^ *(es|en|pt|la) ", r"#\1 ", c)

    id_  = re.search(r"^\s*(\d+)\s+", c)
    ga   = re.match(r"^\s*\d+\s+(.*)", c)
    sin  = re.search(r"@SIN\.-\s*([^@#\n]+)", c)
    var  = re.search(r"@VAR\.-\s*([^@#\n]+)", c)
    nota = re.search(r"@Nota\.-\s*([^@#]*)", c)
    langs = re.findall(r"#(en|pt|es|la) ([^@#\n]+)", c)

    if not id_ or not ga:
        return None, None

    dominio = ""
    for linha in c.split("\n")[1:]:
        linha = linha.strip()
        if linha and not re.match(r"^[#@]|^(es|en|pt|la|Vid\.|SIN|VAR|Nota|\d+)\s", linha):
            dominio = linha
            break

    ga_txt = ga.group(1).strip()
    m_pos = re.match(r'^(.*\S)\s+(m|f|s|a|pl)\s*$', ga_txt)
    if m_pos:
        res = {"ga": m_pos.group(1).strip(), "pos": m_pos.group(2), "dominio": dominio}
    else:
        res = {"ga": ga_txt, "dominio": dominio}
    if sin:  res["sin"]  = sin.group(1).strip()
    if var:  res["var"]  = var.group(1).strip()
    if nota: res["nota"] = nota.group(1).strip()
    for lang, trad in langs:
        res.setdefault(lang, trad.strip())

    res["fonts"] = sorted(set(l["font"] for l in linhas))

    return res, id_.group(1)

# extrair todas as entradas
entries = {}
for idx, start in enumerate(starts):
    end = starts[idx+1] if idx+1 < len(starts) else len(fragmentos)
    res, id_ = processar(bloco_linhas(start, end))
    if res:
        entries[id_] = res

f_out = open("dicionario_medicina.json", "w", encoding="utf8")
json.dump(entries, f_out, indent=4, ensure_ascii=False)
f_out.close()