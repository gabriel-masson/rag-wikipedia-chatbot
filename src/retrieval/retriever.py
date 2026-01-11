# Ao receber uma pergunta, o sistema deve buscar informações relevantes em uma base de dados ou documentos.
from langchain_community.vectorstores import Chroma

from retrieval.embedder import Embedder
# importando a classe Embedder do módulo embedder


class Retriever:
    def __init__(self, persist_dir: str = "vectorstore/chroma", k: int = 3):
        self.embedder = Embedder()
        self.vectordb = Chroma(
            persist_directory=persist_dir,
            embedding_function=self.embedder.embeddings
        )
        self.k = k

    def retrieve(self, query: str):
        return self.vectordb.similarity_search(query, k=self.k)
