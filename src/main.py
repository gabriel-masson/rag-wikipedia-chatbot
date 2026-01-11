# importando a classe RAGChatbot da pasta llm
from llm.qa_chain import RAGChatBot


def main():
    chatbot = RAGChatBot()

    print("🤖 Chatbot RAG (digite 'sair' para encerrar)\n")

    while True:
        question = input("Você: ")
        if question.lower() == "sair":
            break

        answer = chatbot.ask(question)
        print(f"\nBot: {answer}\n")


if __name__ == "__main__":
    main()


# Aqui tivemos um problema de OOM (out of memory), a primeira sololução pode ser trocar nosso modelo para um menor, como o "llama2-7b" ou "mistral-7b", ambos disponíveis no Ollama. Outra solução seria otimizar a quantidade de dados que estamos enviando para o modelo, talvez resumindo os documentos recuperados antes de enviá-los como contexto.
