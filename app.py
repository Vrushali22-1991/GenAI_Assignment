import argparse

from Source.load_doc import load_documents
from Source.doc_chunking import documents_chunking
from Source.retrival import Retriever
from Source.que_ans import question_answer


INDEX_PATH = "data/index.pkl"


def ingest(directory):

    print(f"Read the documents from: {directory}")

    documents = load_documents(directory)

    print(f"Loaded {len(documents)} documents.")

    chunks = documents_chunking(documents)

    print(f"Created {len(chunks)} chunks.")

    retriever = Retriever()

    retriever.build(chunks)

    retriever.save(INDEX_PATH)

    print(f"Index saved to: {INDEX_PATH}")


def ask(question):

    retriever = Retriever()

    try:
        retriever.load(INDEX_PATH)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    results = retriever.search(
        question,
        top_k=3
    )

    answer, sources = question_answer(
        question,
        results
    )

    print()
    print(f"Answer: {answer}")
    print()

    if sources:
        print("Sources: " + ", ".join(sources))
    else:
        print("Sources: None")


def main():

    parser = argparse.ArgumentParser(
        description="Local document Q&A application"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Ingest documents"
    )

    ingest_parser.add_argument(
        "directory",
        help="Directory containing .txt and .md files"
    )

    ask_parser = subparsers.add_parser(
        "ask",
        help="Ask a question"
    )

    ask_parser.add_argument(
        "question",
        help="Question to ask"
    )

    args = parser.parse_args()

    if args.command == "ingest":

        try:
            ingest(args.directory)

        except Exception as e:
            print(f"Error: {e}")

    elif args.command == "ask":

        if not args.question.strip():
            print("Error: Question cannot be empty.")
            return

        ask(args.question)

    else:

        parser.print_help()


if __name__ == "__main__":
    main()