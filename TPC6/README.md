# TPC6 • TF-IDF e Information Retrieval
**Data:** 27/04/2026

### Autor

**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo a implementação de um sistema de **Recuperação de Informação (IR)** baseado na métrica **TF-IDF** (*Term Frequency – Inverse Document Frequency*), aplicada a um corpus de documentos em língua inglesa.

O processamento foi feito recorrendo às bibliotecas `nltk`, `collections` e `math`, sem uso de frameworks de IR externas. A tokenização utilizou o `word_tokenize` do NLTK com remoção de *stopwords* em inglês.

A abordagem consistiu em quatro etapas principais. Primeiro, a tokenização do corpus com remoção de palavras funcionais. De seguida, o cálculo do **TF** (*Term Frequency*) por documento, normalizado pelo número de tokens. Depois, o cálculo do **IDF** (*Inverse Document Frequency*) com base logarítmica (`log10(N/df)`), penalizando termos muito frequentes no corpus. Por fim, a construção da **matriz TF-IDF** e a sua **vetorização**, permitindo representar cada documento como um vetor numérico no espaço do vocabulário.

A recuperação de informação foi implementada através de **similaridade cosseno** entre o vetor da *query* e os vetores dos documentos, devolvendo os resultados ordenados por relevância decrescente.

## Resultados

**[ex.ipynb](./ex.ipynb)**
>*Notebook com a implementação completa — tokenização, TF, IDF, matriz TF-IDF, vetorização e IR por similaridade cosseno.*

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*