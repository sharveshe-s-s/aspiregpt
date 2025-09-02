# backend/build_vectorstore.py

import os
import torch
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Check GPU availability
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    print("⚠️ CUDA not available. Running on CPU.")

# Explicit CSV file list
csv_files = [
    "data/1.csv", "data/2.csv", "data/3.csv", "data/4.csv", "data/5.csv",
    "data/6.csv", "data/9.csv", "data/10.csv",
    "data/11.csv", "data/12.csv", "data/13.csv", "data/14.csv", "data/15.csv",
    "data/16.csv", "data/17.csv", "data/18.csv", "data/19.csv", "data/20.csv",
    "data/21.csv", "data/22.csv", "data/23.csv", "data/24.csv", "data/25.csv",
    "data/26.csv", "data/27.csv", "data/28.csv", "data/29.csv", "data/30.csv",
    "data/31.csv", "data/32.csv", "data/33.csv", "data/34.csv", "data/35.csv",
    "data/36.csv", "data/37.csv",
]

# Use GPU explicitly
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
)

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len
)

# Create folder for vectorstore
os.makedirs("backend/vectorstore", exist_ok=True)

# Initialize FAISS (empty index first)
db = None

# Process each CSV file
for file in csv_files:
    print(f"📂 Processing {file} ...")
    
    # Read in chunks of 1000 rows to avoid memory overflow
    for chunk in pd.read_csv(file, dtype=str, chunksize=1000):
        chunk = chunk.fillna("")  # replace NaN with empty string
        documents = []
        
        # Convert each row into a Document
        for _, row in chunk.iterrows():
            row_text = " | ".join([str(val) for val in row.values])
            documents.append(Document(page_content=row_text, metadata={"source": file}))
        
        # Split into smaller chunks
        docs = text_splitter.split_documents(documents)
        
        # Build or append to FAISS
        if db is None:
            db = FAISS.from_documents(docs, embedding)
        else:
            db.add_documents(docs)
    
    print(f"✅ Finished {file}")

# Save FAISS index
db.save_local("backend/vectorstore/faiss_index")
print("🎉 FAISS index built successfully!")
