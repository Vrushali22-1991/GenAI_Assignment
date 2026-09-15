from Source.retrival import Retriever


def test_retrieval():

    chunks = [
        {
            "source": "refund.md",
            "text": "Customers can request refunds within 30 days."
        },
        {
            "source": "shipping.txt",
            "text": "Standard shipping takes 5 to 7 business days."
        }
    ]

    retriever = Retriever()

    retriever.build(chunks)

    results = retriever.search(
        "When can I request a refund?",
        top_k=1
    )

    assert results[0]["source"] == "refund.md"