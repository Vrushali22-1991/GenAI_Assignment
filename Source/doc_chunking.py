def documents_chunking(documents, chunk_size=500, overlap=50):

    chunks = []

    for document in documents:

        text = document["text"]
        source = document["source"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text.strip():
                chunks.append(
                    {
                        "source": source,
                        "text": chunk_text.strip()
                    }
                )

            start = end - overlap

    return chunks