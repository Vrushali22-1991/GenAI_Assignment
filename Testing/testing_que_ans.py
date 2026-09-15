from Source.que_ans import question_answer


def test_supported_answer():

    results = [
        {
            "source": "refund.md",
            "text": "Refunds are allowed within 30 days.",
            "score": 0.8
        }
    ]

    answer, sources = question_answer(
        "What is the refund policy?",
        results
    )

    assert "30 days" in answer
    assert sources == ["refund.md"]


def test_unsupported_answer():

    results = [
        {
            "source": "shipping.txt",
            "text": "Shipping takes 5 to 7 days.",
            "score": 0.02
        }
    ]

    answer, sources = question_answer(
        "What payment methods are supported?",
        results
    )

    assert "could not find enough support" in answer
    assert sources == []