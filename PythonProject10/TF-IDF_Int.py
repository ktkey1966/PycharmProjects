# Ex. 18 - TF-IDF Intermediate
# Kevin Key
# 11/20/2025

# DATA BLOCK

text = """he really really loves coffee
my sister dislikes coffee
my sister loves tea
"""

import math

def main(text):
    # Split the text first into lines and list words
    docs = [line.split() for line in text.splitlines()]
    N = len(docs)

    # Create the vocabulary
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}

    for word in vocabulary:
        tf[word] = [doc.count(word) /len(doc) for doc in docs]  # Creates a list for tf[word]

        df[word] = sum([word in doc for doc in docs])           # Normalizes the df[word]

    # Loop through the words and calculate the tf-idf score
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            idf = math.log(1 / df[word], 10)

            # TF-IDF = TF * IDF
            tfidf_value = tf[word][doc_index] * idf
            tfidf.append(tfidf_value)

        print(tfidf)

main(text)

