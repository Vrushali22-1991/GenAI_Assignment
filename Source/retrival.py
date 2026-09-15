import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:

    def __init__(self):
        self.vectorizer = None
        self.vectors = None
        self.chunks = None

    def build(self, chunks):

        self.chunks = chunks

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        self.vectors = self.vectorizer.fit_transform(texts)

    def search(self, query, top_k=3):

        if self.vectorizer is None:
            raise RuntimeError("Retriever has not been built.")

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.vectors
        )[0]

        ranked_indexes = scores.argsort()[::-1]

        results = []

        for index in ranked_indexes[:top_k]:

            results.append(
                {
                    "source": self.chunks[index]["source"],
                    "text": self.chunks[index]["text"],
                    "score": float(scores[index])
                }
            )

        return results

    def save(self, path):

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as file:
            pickle.dump(
                {
                    "vectorizer": self.vectorizer,
                    "vectors": self.vectors,
                    "chunks": self.chunks
                },
                file
            )

    def load(self, path):

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(
                f"Index not found: {path}. Run ingest first."
            )

        with open(path, "rb") as file:

            data = pickle.load(file)

        self.vectorizer = data["vectorizer"]
        self.vectors = data["vectors"]
        self.chunks = data["chunks"]