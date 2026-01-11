from ingestion.wiki_loader import WikipediaLoader

if __name__ == "__main__":
    topics = ["Machine learning",
              "paradigma de linguagem de programação", "Quantum computing"]
    output_directory = "data/raw"

    loader = WikipediaLoader(language='pt')
    loader.load_pages(
        topics,
        output_dir=output_directory
    )
    print("Páginas da Wikipedia carregadas com sucesso.")
