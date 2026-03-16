# TPC2 • Scraper de Doenças (Atlas da Saúde)
**Data:** 13/03/2026

### Autor

**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo a extração e estruturação de dados sobre doenças a partir do portal **Atlas da Saúde** (secção "Doenças de A a Z"), produzindo um dicionário médico digital em formato **JSON**.

A fonte de dados tem origem na secção "Doenças de A a Z" (`https://www.atlasdasaude.pt/doencasAaZ/`). O processamento e extração de dados foram realizados em Python, recorrendo às bibliotecas `requests` para os pedidos HTTP e `BeautifulSoup` para fazer o *parsing* do HTML. Foi também utilizado o módulo `urllib.parse` para a reconstrução robusta dos URLs.

A abordagem consistiu em três etapas principais:
1. **Navegação Alfabética:** O script itera sobre as letras do alfabeto (a-z), acedendo à página de listagem correspondente a cada letra e extraindo o nome de cada doença e o respetivo URL.
2. **Extração de Artigos:** Para cada doença identificada, o script acede à sua página individual e localiza o bloco principal de texto (identificado pela classe CSS `field-name-body`).
3. **Estruturação de Conteúdo:** O texto do artigo é processado sequencialmente. Através da leitura das *tags* HTML, o conteúdo é categorizado com base nos cabeçalhos (`<h2>`). Se o cabeçalho contiver palavras-chave como "causa", "sintoma" ou "tratamento", os parágrafos (`<p>`) e listas (`<ul>`/`<li>`) subsequentes são guardados nas respetivas listas. O texto introdutório é alocado à "Descrição".

O resultado é um ficheiro JSON onde as entradas estão agrupadas pela letra inicial, mapeando cada doença para a sua Descrição, Causas, Sintomas e Tratamento.

## Resultados

**[script.py](./script.py)**
>*Script de extração — percorre o site do Atlas da Saúde e produz o ficheiro JSON estruturado com a informação das doenças.*

---

**[doencas.json](./doencas.json)**
>*Dicionário médico estruturado contendo a descrição, causas, sintomas e tratamentos das doenças extraídas.*

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*