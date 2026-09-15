# GenAI Assignment

This project is a command-line application that reads local `.txt` and `.md`
documents and answers questions based on their content.

## Prerequisites

- Python 3.13.7
- pip

## Setup

Create a virtual environment:

For Windows:

python -m venv assign_venv

Activate it:

assign_venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt


## Documents

Put the documents inside the `uploaded_documents` folder.
currently i added 4 simple txt files. refund policy.txt , shipping policy.txt (taken refrence from flipkart)
Only `.txt` and `.md` files are supported.

Example:
uploaded_documents/
    refund policy.txt
    shipping policy.txt +


## Ingest Documents

Run the following command from the project root:

python app.py ingest ./uploaded_documents

This reads the documents, splits them into smaller chunks, creates the
retrieval index and saves the index locally.

The index is saved in:

data/index.pkl

Ingestion needs to be run whenever the documents are changed or new documents are added.

## Ask a Question

After ingestion, run:

python app.py ask "What is the refund policy?"

Example output:

Answer: Customers may request a refund within 30 days of purchase.

Sources: refund policy.txt

Another example:

python app.py ask "How long does standard shipping take?"

If the required information is not present in the documents, the application
returns:

Answer: I could not find enough support for that answer in the provided documents.

Sources: None

## Run Tests

Run all tests using:

pytest

For detailed test output:

pytest -v

The tests cover document loading, chunking, retrieval and answer generation.

## Dependencies
using this command created requirements.txt  
pip freeze > requirements.txt

The main packages used are:

- scikit-learn
- pytest

The application does not require any paid service.

## Project Structure

source/
    load_doc.py
    doc_chunking.py
    retrival.py
    que_ans.py

Testing/
    test_loader.py
    test_chunking.py
    test_retrieval.py
    test_que_ans.py

uploaded_documents/
    refund policy.txt
    shipping policy.txt

data/
    index.pkl

app.py
requirements.txt
README.txt
NOTES.txt