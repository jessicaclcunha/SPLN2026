# TPC4 • Word Embeddings no Universo de Harry Potter
**Data:** 14/04/2026

### Autor
**ID:** PG60267  
**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo o treino e a exploração de um modelo de **Word Embeddings** (Word2Vec) utilizando o texto dos dois primeiros livros da saga Harry Potter em português: *A Pedra Filosofal* e *A Câmara Secreta*.

Estefoca-se na extração de relações semânticas complexas, permitindo não só medir similaridades, mas também realizar operações aritméticas com conceitos e analisar o contexto de personagens específicas ao longo da narrativa inicial.

### Metodologia

1.  **Pré-processamento:**
    * Leitura dos ficheiros `Harry_Potter.txt` e `Harry_Potter_Camara_Secreta-br.txt`.
    * Tokenização de sentenças e limpeza de pontuação (`nltk`).
    * Normalização total para minúsculas.
2.  **Treino do Modelo:**
    * Algoritmo: **Word2Vec** via `Gensim`.
    * Hiperparâmetros: Vetores de 300 dimensões, janela de 5 palavras, mínimo de 2 ocorrências.
3.  **Análise Avançada:**
    * **Evolução e Contexto:** Estudo da vizinhança semântica de personagens ambíguas (ex: Snape).
    * **Aritmética de Vetores:** Testes de analogias e transferência de atributos entre heróis e vilões.
4.  **Visualização:**
    * Redução de dimensionalidade (PCA) para mapear o "espaço mágico" em 2D.

## Resultados e Explorações

O modelo permitiu extrair conhecimentos interessantes sobre o mundo de Hogwarts:

### 1. Aritmética Semântica (Analogias)
A capacidade do modelo em resolver equações conceituais foi testada com sucesso:
* **Voldemort - Maldade + Bondade:** Ao subtrair atributos negativos de Voldemort e somar conceitos de bondade, o modelo aproxima-se de figuras como **Dumbledore** ou **Harry**.
* **Harry - Vassoura + Ranhoso:** Operação que visa encontrar o "rival" escolar, aproximando o vetor resultante de **Draco** ou **Duda**.

### 2. Contexto de Personagens (O Caso Snape)
Embora limitado aos dois primeiros livros, o modelo já captura a aura antagonista de Severo Snape:
* A vizinhança de **Snape** inclui termos como *professor*, *masmorras*, *poções* e nomes de outros personagens que desconfiam dele, refletindo o seu papel inicial na saga.

### 3. Deteção de Intrusos
* No conjunto `['harry', 'hermione', 'ron', 'dumbledore', 'vassoura']`, o modelo identificou corretamente **vassoura** como o termo que não pertence ao grupo (por ser um objeto e não uma entidade/personagem).

### 4. Similaridades Chave
* **Grifinória ↔ Sonserina:** 0.86 (indicando que aparecem em contextos gramaticais idênticos, como "Casas").
* **Varinha ↔ Vassoura:** 0.77 (objetos mágicos fundamentais).

## Ficheiros no Repositório

* **[potter_model.ipynb](./potter_model.ipynb):** Notebook principal com o código, visualizações e testes de analogias.
* **[Harry_Potter.txt](./Harry_Potter.txt):** Texto do Livro 1.
* **[Harry_Potter_Camara_Secreta-br.txt](./Harry_Potter_Camara_Secreta-br.txt):** Texto do Livro 2.

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*