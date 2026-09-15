## Architecture

There are two main flows.

In the ingestion flow, documents are loaded from the `uploaded_documents`folder. 
The text is split into smaller chunks and converted into TF-IDF vectors. 
The index and document information are then saved locally.

In the question flow, the saved index is loaded.
The question is converted into a TF-IDF vector and compared with the document chunks using cosine
similarity. 
The most relevant chunks are used to prepare the answer.

Question --> TF-IDF Retrieval  --> Relevant document chunks --> Answer + source filename

## Retrieval Strategy

I used TF-IDF with cosine similarity.

I choose this because the assignment uses a small local document collection
and does not require any paid API. It is also simple to run and test locally.

A relevance threshold is used so that the application does not return an
answer when the retrieved content is not relevant enough.

## Limitations

- TF-IDF mainly works based on matching words, so it may miss some semantic
  relationships.
- The current answer generation is simple and does not use an LLM.
- The current chunking approach is basic.
- This approach may not be suitable for a very large document collection.
- A local embedding model and local LLM could be added later to improve
  semantic retrieval and answer generation.