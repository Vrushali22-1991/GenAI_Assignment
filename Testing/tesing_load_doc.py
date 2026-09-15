from Source.load_doc import load_documents


def test_load_documents(tmp_path):

    file = tmp_path / "test.md"

    file.write_text(
        "# Refund Policy \n Refunds allowed within 30 days.",
        encoding="utf-8"
    )

    documents = load_documents(tmp_path)

    assert len(documents) == 1
    assert documents[0]["source"] == "test.md"
    assert "Refunds" in documents[0]["text"]