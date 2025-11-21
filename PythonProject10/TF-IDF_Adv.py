# Ex. 18 - TF-IDF Advance
# Kevin Key
# 11/20/2025

import math
import itertools

# Sample text
text = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the King's horses and all the King's men
Couldn't put Humpty Dumpty together again.
'''

def main(text):
    # 1. Split text into documents (lines), ignore empty/blank lines
    docs = [line.lower().split() for line in text.split('\n') if line.strip()]
    N = len(docs)

    # 2. Build sorted vocabulary of all unique words
    vocabulary = sorted({word for doc in docs for word in doc})

    # 3. Initialize term frequency (TF) structure and document frequency (DF) dict
    tf = {word: [] for word in vocabulary}
    df = {}

    # 4. Compute TF and DF
    for word in vocabulary:
        doc_count = 0
        for doc in docs:
            # Guard just in case, though docs are already filtered
            if len(doc) == 0:
                continue
            count = doc.count(word)
            tf[word].append(count / len(doc))   # no division by zero now
            if count > 0:
                doc_count += 1
        df[word] = doc_count / N               # fraction of docs containing the word

    # 5. Build TF-IDF vectors for each document
    tfidf_vectors = []
    for i in range(N):
        vec = []
        for word in vocabulary:
            idf = math.log(1 / df[word], 10)   # log base 10
            vec.append(tf[word][i] * idf)
        tfidf_vectors.append(vec)

    # 6. Euclidean distance between two vectors
    def distance(v1, v2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

    # 7. Find closest pair of documents
    best_pair = None
    min_dist = float('inf')

    for i, j in itertools.combinations(range(N), 2):
        d = distance(tfidf_vectors[i], tfidf_vectors[j])
        if d < min_dist:
            min_dist = d
            best_pair = (i, j)

    print("Docs:", docs)
    print("Vocabulary:", vocabulary)
    print("Best pair (0-based indices):", best_pair)
    print("Minimum distance:", min_dist)


# Run the program
main(text)



