from gensim import corpora, models


def Vectorize(tokenized_documents, dictionary=None):
    if dictionary is None:
        dictionary = corpora.Dictionary(tokenized_documents)

    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]
    tfidf = models.TfidfModel(corpus)
    vectorized_documents = tfidf[corpus]

    return vectorized_documents, dictionary
