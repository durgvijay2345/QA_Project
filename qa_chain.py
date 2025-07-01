# qa_chain.py
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

def get_answer(question: str) -> str:
    # Embeddings load karo
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector store load karo
    vectorstore = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Top 3 relevant chunks dhundho
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # FREE QA model — ~250MB, ek baar download hoga
    print("LLM load ho raha hai...")
    pipe = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad",
        device=-1  # CPU
    )

    # Answer lo
    result = pipe(question=question, context=context)
    return result["answer"]


# Direct test
if __name__ == "__main__":
    print("QA System ready!\n")
    while True:
        q = input("Aap: ").strip()
        if q.lower() in ["quit", "exit", "q"]:
            break
        if not q:
            continue
        print(f"\nAnswer: {get_answer(q)}\n")