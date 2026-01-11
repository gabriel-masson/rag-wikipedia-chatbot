import os
from vectorstore import VectorStore

CHUNK_DIR = "data/chunks"


def load_chunks():
    texts = []
    metadatas = []

    for file_name in os.listdir(CHUNK_DIR):

        if not file_name.endswith(".txt"):
            continue

        path = os.path.join(CHUNK_DIR, file_name)

        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        texts.append(text)
        metadatas.append({"source": file_name})

    return texts, metadatas


if __name__ == "__main__":
    texts, metadatas = load_chunks()

    store = VectorStore()
    store.build_from_texts(texts, metadatas)

    print(f"[OK] Vector store criado com {len(texts)} chunks")
