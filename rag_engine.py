import faiss
import pickle
from sentence_transformers import SentenceTransformer


class RAG:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Loading FAISS index...")

        self.index = faiss.read_index("../vectorstore/index.faiss")

        print("Loading metadata...")

        with open("../vectorstore/chunks.pkl", "rb") as f:

            self.chunks = pickle.load(f)


    def retrieve(self, query, k=5):

        query_embedding = self.model.encode([query])

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i in indices[0]:

            results.append(self.chunks[i])

        return results