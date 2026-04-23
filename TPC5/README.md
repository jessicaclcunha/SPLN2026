# TPC5 • Treino e Comparação de Modelos NER (spaCy vs. BERT)
**Data:** 19/03/2026


### Autor

**ID:** PG60267

**Nome:** Jéssica Cristina Lima da Cunha

<img src="../imgs/autor.jpg" width="150">

---

## Resumo

Este trabalho teve como objetivo o treino de um modelo de **Reconhecimento de Entidades Mencionadas (NER)** utilizando a biblioteca **spaCy**, comparando a sua performance com o modelo **BERT** (Neuralmind) explorado nas aulas. O dataset utilizado foi o `lfcc/portuguese_ner` do HuggingFace, focado em entidades em língua portuguesa.

## Metodologia

### 1. Treino do Modelo spaCy
Seguindo as diretrizes da aula, o processo foi dividido em três etapas principais via CLI:
* **Conversão:** Os dados foram convertidos do formato IOB/HuggingFace para o formato binário do spaCy (`.spacy`) através de um script de mapeamento de spans.
* **Configuração:** Utilizou-se o comando `spacy init config` para gerar um ficheiro de configuração otimizado para eficiência.
* **Treino:** O modelo foi treinado no Google Colab com suporte a GPU, resultando num modelo customizado capaz de detetar categorias como `PESSOA`, `LOCAL`e `ORGANIZAÇÃO`.

### 2. Modelo de Referência (Aula)
Como base de comparação (Baseline de alta performance), utilizou-se o modelo **BERT (Neuralmind/bert-base-portuguese-cased)**, ajustado especificamente para NER em português, que representa o estado da arte para esta tarefa.

### 3. Modelo Base spaCy
Avaliou-se também o modelo pré-treinado `pt_core_news_sm` para medir o impacto do treino específico em domínios personalizados.

## Resultados e Comparação

Abaixo apresentam-se as métricas obtidas na avaliação dos três modelos sobre o conjunto de teste:

| Modelo | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| **BERT (Aula)** | 0.9460 | 0.9699 | **0.9578** |
| **spaCy (Treinado)** | 0.9451 | 0.9517 | **0.9484** |
| **spaCy (Base - sm)** | 0.6646 | 0.6474 | 0.6559 |

### Análise Crítica
* **Performance:** O modelo spaCy treinado obteve um resultado surpreendente (**F1: 0.948**), ficando a menos de 1% de distância do modelo BERT. Isto demonstra que, para este dataset, um modelo mais leve (CNN do spaCy) consegue ser extremamente eficaz.
* **Velocidade:** O modelo spaCy apresentou tempos de inferência significativamente menores que o BERT, sendo uma solução mais viável para ambientes com recursos limitados.

## Ficheiros no Repositório

**[spacy_ner_comparison.ipynb](./spacy_ner_comparison.ipynb)** 
> Notebook com o processo de conversão, treino e avaliação do spaCy.
**[ex1.ipynb](./ex1.ipynb)** 
> Notebook da aula com a implementação e métricas do modelo BERT.

## Conclusão

O treino do modelo spaCy foi bem-sucedido, cumprindo todos os requisitos (convert, init, train). A comparação mostra que o treino personalizado é essencial, elevando o F1-Score de **0.65** para **0.94**, igualando praticamente o desempenho de modelos transformadores mais pesados.