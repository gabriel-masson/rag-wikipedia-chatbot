import os
from text_cleaner import TextCleaner

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def process_file():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    cleaner = TextCleaner()

    for file_name in os.listdir(RAW_DIR):
        if not file_name.endswith('.txt'):
            continue

        raw_path = os.path.join(RAW_DIR, file_name)
        processed_path = os.path.join(PROCESSED_DIR, file_name)

        with open(raw_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        clean_text = cleaner.clean(raw_text)

        with open(processed_path, 'w', encoding='utf-8') as f:
            f.write(clean_text)

        print(f"Processed {file_name} and saved to {processed_path}")


if __name__ == "__main__":
    process_file()
