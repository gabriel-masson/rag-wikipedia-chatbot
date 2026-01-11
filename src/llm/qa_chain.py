from langchain_community.llms import Ollama
from retrieval.retriever import Retriever

# Fazer ajuste para caber na memória
# Aqui limitamos a quantidade de caracteres do contexto para evitar problemas de memória
MAX_CONTEXT_CHARS = 1500


class RAGChatBot:
    def __init__(self, model_name: str = "mistral"):
        model_name = "phi3:mini"  # modelo menor para evitar OOM
        self.llm = Ollama(model=model_name, temperature=0.2)
        self.retriever = Retriever()

    def ask(self, question: str) -> str:

        docs = self.retriever.retrieve(question)
        context = ""

        for doc in docs:
            if len(context) + len(doc.page_content) > MAX_CONTEXT_CHARS:
                break
            context += doc.page_content + "\n\n"

        prompt = f"""
        Use o contexto abaixo para responder a pergunta.
Se a resposta não estiver no contexto, diga que não sabe.
        Contexto:
        {context}
        Pergunta: 
        {question}

        Resposta:
        """

        return self.llm.invoke(prompt)
