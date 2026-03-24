# TPC3 • Extração de Personagens e Relações (Harry Potter)
**Data:** 19/03/2026

### Autor

**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo a extração de personagens e relações de amizade a partir do texto do livro **Harry Potter e a Pedra Filosofal**, utilizando processamento de linguagem natural com a biblioteca **spaCy**.

A fonte de dados é o ficheiro `Harry_Potter.txt`, contendo o texto do livro em português. O processamento foi realizado em Python, recorrendo ao modelo `pt_core_news_sm` do spaCy para análise linguística (NER e POS tagging) e ao `Matcher` para deteção de padrões.

A abordagem consistiu em duas etapas principais:
1. **Extração de Personagens:** O `Matcher` é configurado com um padrão que deteta entidades do tipo `PER` (pessoa) compostas por nomes próprios (`PROPN`). O texto é processado frase a frase e os personagens identificados são filtrados para remover ruído (nomes que começam com minúscula ou contêm caracteres inválidos). O ruído residual deve-se ao facto do modelo `pt_core_news_sm` ter sido treinado em texto jornalístico, não em ficção.
2. **Extração de Relações:** Dois personagens são considerados **amigos** se aparecerem juntos na mesma frase. Para cada frase, são gerados todos os pares de personagens detetados usando `combinations`, e cada par é guardado como um tuplo ordenado para evitar duplicados.

## Resultados

**[script.py](./script.py)**
>*Script de extração — processa o texto do livro e imprime os personagens identificados e as suas relações de amizade.*

---

**[Harry_Potter.txt](./Harry_Potter.txt)**
>*Texto do livro Harry Potter e a Pedra Filosofal em português, utilizado como fonte de dados.*

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*