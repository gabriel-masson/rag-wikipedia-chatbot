import re


class TextCleaner:
    def clean(self, text: str) -> str:

        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        # Remove citations like [1], [2], etc.
        text = re.sub(r'\[.*?\]', '', text)
        text = text.strip()

        return text
