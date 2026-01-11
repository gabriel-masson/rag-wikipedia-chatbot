
# Chatbot Wikipedia

Projeto com o objetivo de aplicar os conceitos de LLM com RAG


## Como foi construido?
Dividimos em três fases principais:

**Ingestion:** Responsavel pelo processo de extração, tratamento e Chunking;

**Retriver:** Nessa fase construimos o nosso RAG e terá a responsabilidade de conter todas as funções necessarias para a funcionalidade dele. Para isso, utilizamos os dados vindo da fase de ingestion e transformando o texto em Embeddings que serão percistidos no Chromadb, um banco de vetores.

**LLM:** Aqui definimos qual LLM será usada (LLHAMA, phi3:mini, mistral) e juntar com a parte do Retriver.


## Instalação

Primeiro crie o ambiente .venv

```bash
  python -m venv .venv
```

Em seguida intale todas as dependências

```bash
  pip install requirements.txt
```

Intale o [OLLAMA](https://ollama.com/)

Instale o modelo que iremos usar

```bash
  ollama pull mistral
```
## Aprendizado

A primeira novidade foi a estrutura do projeto: Injection, retriever e LLM. Com essa estrutura cada estapa foi bem definida, mantendo o encapsulamento com cada class com sua unica responsabilidade.

A parte de descoberta veio no momento do retriever, onde construimos o nosso RAG. Tudo começa com a escolha de como fazer nosso embeddings, estratégia foi usar HuggingFaceEmbddings com o modelo sentence-transformers/all-MiniLM-L6-v2.

Depois persistimos os dados do chunks num vectordb usando o Chroma, no qual o modelo final irá fazer a busca. E o ultimo passo do Retriever é a partir de uma Query, realizar uma busca no Vectordb para gerar a saida do nosso chatbot.

Aqui algumas perguntas que foram respondidadas durante o projeto:

Qual é o trade-off principal ao aumentar demais o tamanho do chunk em RAG?

```
Diluir relevância. Chunks grandes misturam múltiplos tópicos, pioram o retrieval precision e encarecem o custo computacional (atenção O(n²) do Transformer).
Chunks grandes demais → bom contexto, péssima recuperação.
```

Por que o embedding é feito offline e não a cada pergunta do usuário?
```
Embeddings são feitos offline porque representam o conhecimento estático. Recriá-los a cada pergunta seria computacionalmente caro, redundante e quebraria a separação entre ingestion (offline) e retrieval (online).
- Embedding = custo alto, feito uma vez;
- Busca vetorial = custo baixo, feito por pergunta;
```
Em um sistema RAG, por que aumentar a temperatura do LLM não corrige um retrieval ruim? 

```
Esse é o dilema dos dados "Entra lixo, sai lixo", nossos dados devem ter o máximo de qualidade possível para buscar a melhor saída possível.
```

#Problemas Resolvidos

OOM (out of memory): Esse problema ocorre devido o consumo da memória RAM. Para soluciona-lo temos algumas opções:

- Usar um modelo menor como phi3:mini
- Diminuir o tamanho de caracteres do contexto
- Dimnuir o k do retrieval

