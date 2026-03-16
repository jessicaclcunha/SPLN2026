# TPC1 • Dicionário de Medicina
**Data:** 05/03/2026

### Autor

**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo a extração e estruturação do *Vocabulario de Ciencias da Saúde* a partir de um ficheiro **XML** gerado pelo conversor `pdftoxml` (poppler), produzindo um dicionário médico multilingue em formato **JSON**.

O ficheiro de entrada (`medicina.xml`) representa o PDF em formato `pdf2xml`, onde cada fragmento de texto é uma tag `<text>` com atributos de posição (`top`, `left`) e tipografia (`font`). O processamento foi feito inteiramente com `re` e `json`, sem recurso a nenhum parser XML.

A abordagem consistiu em três etapas principais. Primeiro, a leitura linha a linha do XML com regex para extrair os atributos `top`, `left`, `font` e o conteúdo de cada fragmento, removendo tags internas (`<b>`, `<i>`). Os fragmentos foram depois ordenados por página, coluna (esquerda/direita, separadas em `left < 340`) e posição vertical, de forma a reconstruir a ordem de leitura do layout a duas colunas. O início de cada entrada foi detetado pelo atributo `font` (`2` ou `3`, correspondente ao Palatino bold) combinado com o padrão numérico do identificador.

Cada entrada do dicionário foi processada com regex para extrair os seguintes campos: termo em galego (`ga`), classe gramatical (`pos`: `m`, `f`, `a`, `s`, `pl`), domínio temático (`dominio`), sinónimos (`sin`), variantes (`var`), nota (`nota`), traduções para espanhol (`es`), inglês (`en`), português (`pt`) e latim (`la`), e ainda a lista de fonts tipográficas usadas na entrada (`fonts`).

Foram extraídas **5362 entradas**.

## Resultados

**[script.py](./script.py)**
>*Script de extração — lê o `medicina.xml` e produz o `dicionario_medicina.json`.*

---

**[dicionario_medicina.json](./dicionario_medicina.json)**
>*Dicionário médico multilingue estruturado com 5362 entradas.*

---

**[medicina.xml](./medicina.xml)**
>*Ficheiro de entrada — representação pdf2xml do vocabulário médico gerada pelo poppler.*

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*