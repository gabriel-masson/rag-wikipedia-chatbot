# Colect data from wikipedia, junt colect and not process it
import os
import wikipedia


class WikipediaLoader:
    def __init__(self, language: str = 'pt'):
        wikipedia.set_lang(language)

    def load_pages(self, topics: list[str], output_dir: str):
        os.makedirs(output_dir, exist_ok=True)

        for topic in topics:
            try:
                page = wikipedia.page(topic)
                file_path = os.path.join(
                    output_dir, f"{topic.replace(' ', '_')}.txt")

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(page.content)

                print(f"Saved page for topic '{topic}' to '{file_path}'")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Disambiguation error for topic '{topic}': {e.options}")
            except wikipedia.exceptions.PageError:
                print(f"Page not found for topic '{topic}'")
