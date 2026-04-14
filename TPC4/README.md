# TPC4 • Word Embeddings no Universo de Harry Potter
**Data:** 14/04/2026

### Autor
**ID:** PG60267  
**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

## Resumo

Este trabalho teve como objetivo o treino e a exploração de um modelo de **Word Embeddings** (Word2Vec) utilizando o texto dos dois primeiros livros da saga Harry Potter em português: *A Pedra Filosofal* e *A Câmara Secreta*.

O projeto utiliza a biblioteca `Gensim` para criar representações vetoriais das palavras, permitindo analisar semelhanças semânticas, relações analógicas e a estrutura do vocabulário através de visualizações espaciais.

### Metodologia

1.  **Pré-processamento:**
    * Leitura dos ficheiros `Harry_Potter.txt` e `Harry_Potter_Camara_Secreta-br.txt`.
    * Tokenização de sentenças e limpeza de pontuação usando a biblioteca `nltk`.
    * Normalização do texto para minúsculas.
2.  **Treino do Modelo:**
    * Utilização do algoritmo **Word2Vec** (`Skip-gram` ou `CBOW`).
    * Parâmetros: dimensão do vetor = 300, janela = 5, mínimo de ocorrências = 2.
3.  **Exploração e Validação:**
    * **Similaridade:** Cálculo da proximidade entre personagens e conceitos.
    * **Deteção de Intrusos:** Identificação da palavra que não pertence a um grupo semântico.
    * **Analogias:** Resolução de equações linguísticas.
4.  **Visualização:**
    * Redução de dimensionalidade através de **PCA** (Principal Component Analysis) e geração de gráficos 2D.

## Resultados Obtidos

O modelo treinado apresentou os seguintes resultados práticos:

### 1. Similaridade Semântica
* **Harry e Hermione:** 0.6854
* **Grifinória e Sonserina:** 0.8693
* **Hogwarts e Escola:** 0.6426
* **Varinha e Vassoura:** 0.7772

### 2. Deteção de Intrusos (`doesnt_match`)
* No grupo `['harry', 'hermione', 'ron', 'dumbledore', 'vassoura']`, o intruso identificado foi **"vassoura"**.
* No grupo `['grifinória', 'sonserina', 'lufa-lufa', 'corvinal', 'quadribol']`, o intruso foi **"quadribol"**.

### 3. Palavras Mais Semelhantes (`most_similar`)
* **Voldemort:** lorde (0.8576), gringotes (0.8298), você-sabe-quem (0.8196).
* **Harry:** neville (0.7295), draco (0.7022), gina (0.6936).

### 4. Analogias
* **Harry** -> **Grifinória** | **Draco** -> **Lufa-Lufa** (Resultado enviesado pelo corpus reduzido).
* **Harry** -> **Hermione** | **Rony** -> **Mione**.

## Ficheiros no Repositório

* **[potter_model.ipynb](./potter_model.ipynb):** Notebook com o código de treino e testes.
* **[Harry_Potter.txt](./Harry_Potter.txt):** Texto do 1º livro.
* **[Harry_Potter_Camara_Secreta-br.txt](./Harry_Potter_Camara_Secreta-br.txt):** Texto do 2º livro.

---
*Trabalho realizado no âmbito da UC de Processamento de Linguagem Natural (SPLN) 2025/2026*