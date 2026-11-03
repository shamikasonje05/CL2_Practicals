documents = {
    1: "Information retrieval is the process of finding information",
    2: "Information retrieval systems help users find relevant documents",
    3: "Search engines use information retrieval techniques",
    4: "Python is useful for implementing information retrieval systems"}

inverted_index = {}

for doc_id, text in documents.items():
    words = text.lower().split()

    for word in words:
        # Remove simple punctuation
        word = word.strip(".,!?")

        if word not in inverted_index:
            inverted_index[word] = set()

        inverted_index[word].add(doc_id)

print("INVERTED INDEX")
print("-" * 40)

for word in sorted(inverted_index):
    print(word, "->", sorted(inverted_index[word]))
def retrieve_documents(query):
    query_words = query.lower().split()

    result = set()

    for word in query_words:
        word = word.strip(".,!?")

        if word in inverted_index:
            if not result:
                result = inverted_index[word].copy()
            else:
                # AND operation
                result = result.intersection(inverted_index[word])

    return result

query = input("\nEnter your search query: ")

results = retrieve_documents(query)

print("\nRetrieved Documents:")
print("-" * 40)

if results:
    for doc_id in sorted(results):
        print("Document", doc_id, ":", documents[doc_id])
else:
    print("No documents found.")