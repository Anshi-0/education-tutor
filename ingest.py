import fitz
import os
import re
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


DATA_FOLDER = "../data"
INDEX_PATH = "../vectorstore/index.faiss"
CHUNK_PATH = "../vectorstore/chunks.pkl"


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def split_chapters(text):

    pattern = r"(Chapter\s+\d+)"
    splits = re.split(pattern, text)

    chapters = {}

    for i in range(1, len(splits), 2):

        title = splits[i]
        content = splits[i + 1]

        chapters[title] = content

    return chapters


def chunk_text(text, size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + size
        chunk = text[start:end]

        chunks.append(chunk)

        start += size - overlap

    return chunks


def ingest():

    all_chunks = []

    for file in os.listdir(DATA_FOLDER):

        if not file.endswith(".pdf"):
            continue

        pdf_path = os.path.join(DATA_FOLDER, file)

        print("Processing:", file)

        text = extract_text(pdf_path)

        chapters = split_chapters(text)

        for chapter, content in chapters.items():

            chunks = chunk_text(content)

            for chunk in chunks:

                all_chunks.append({
                    "source": file,
                    "chapter": chapter,
                    "text": chunk
                })

    texts = [c["text"] for c in all_chunks]

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Generating embeddings...")

    embeddings = model.encode(texts, show_progress_bar=True)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    print("Building FAISS index...")

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs("../vectorstore", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNK_PATH, "wb") as f:

        pickle.dump(all_chunks, f)

    print("Ingestion complete!")


if __name__ == "__main__":
    ingest()