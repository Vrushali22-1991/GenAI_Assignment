from pathlib import Path


EXTENSIONS = {".txt", ".md"}     #In future if we want to add more extenstions we can mention here


def load_documents(directory):
    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Documents directory does not exist: {directory}"
        )

    if not directory.is_dir():
        raise ValueError(
            f"Provided path is not a directory: {directory}"
        )

    documents = []

    for file_path in directory.iterdir():

        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in EXTENSIONS:
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            raise RuntimeError(
                f"Could not read {file_path.name}: {e}"
            )

        if text.strip():
            documents.append(
                {
                    "source": file_path.name,
                    "text": text
                }
            )

    if not documents:
        raise ValueError(
            "No readable .txt or .md documents found."
        )

    return documents