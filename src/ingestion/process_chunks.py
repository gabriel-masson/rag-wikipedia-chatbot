import os
from chunker import TextChunker

PROCESSED_DIR = "data/processed"
CHUNKED_DIR = "data/chunks"


def process_chunks():
    os.makedirs(CHUNKED_DIR, exist_ok=True)
    chunker = TextChunker(chunk_size=500, overlap=100)

    for file_name in os.listdir(PROCESSED_DIR):
        if not file_name.endswith('.txt'):
            continue

        file_path = os.path.join(PROCESSED_DIR, file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            processed_text = f.read()

        chunks = chunker.chunk(processed_text)

        base_name = file_name.replace(".txt", "")

        for i, chunk in enumerate(chunks):
            chunk_path = os.path.join(
                CHUNKED_DIR, f"{base_name}_chunk_{i}.txt")

            with open(chunk_path, 'w', encoding='utf-8') as f:
                f.write(chunk)
        print(f"Processed {file_name} into {len(chunks)} chunks.")


if __name__ == "__main__":
    process_chunks()
