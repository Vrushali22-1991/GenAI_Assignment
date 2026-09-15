from Source.doc_chunking import documents_chunking


def test_chunking():

    documents = [
        {
            "source": "test.txt",
            "text": "a" * 1000
        }
    ]

    chunks = documents_chunking(
        documents,
        chunk_size=500,
        overlap=50
    )

    assert len(chunks) == 3