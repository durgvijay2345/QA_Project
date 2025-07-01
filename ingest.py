# ingest.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def ingest_pdf(pdf_path):
    print(f"📄 PDF load ho raha hai: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"✅ {len(documents)} pages load hue")

    # Chunks banao
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    print(f"✅ {len(chunks)} chunks bane")

    # FREE HuggingFace embeddings — pehli baar ~90MB download hoga
    print("⏳ Embeddings model load ho raha hai (pehli baar time lagega)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # FAISS vector store
    print("⏳ Vector store ban raha hai...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    os.makedirs("vector_store", exist_ok=True)
    vectorstore.save_local("vector_store")
    print("✅ Vector store ready! Ab qa_chain.py chalao.")

if __name__ == "__main__":
    ingest_pdf("data/sample.pdf")