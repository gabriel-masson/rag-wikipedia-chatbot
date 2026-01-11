# Armazenamento de vetores para recuperação eficiente
import os
from langchain_community.vectorstores import Chroma
from embedder import Embedder


class VectorStore:
    '''
    Obs: Embbeding não são recalculados se o diretório de persistência já existir; Chroma persiste em disco; ingestion roda sempre e retrieval roda sempre.
    '''

    def __init__(self, persist_dir: str = "vectorstore/chroma"):
        self.persist_dir = persist_dir
        self.embedder = Embedder()

    def build_from_texts(self, texts: list[str], metadatas: list[dict]):
        print(self.persist_dir)
        os.makedirs(self.persist_dir, exist_ok=True)

        print(type(self.embedder.embeddings))
        vectordb = Chroma.from_texts(
            texts=texts,
            embedding=self.embedder.embeddings,
            metadatas=metadatas,
            persist_directory=self.persist_dir
        )

        vectordb.persist()

        return vectordb
