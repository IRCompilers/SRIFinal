from gensim import corpora, models


def Vectorize(tokenized_documents, dictionary=None, is_query=False):
    if dictionary is None:
        dictionary = corpora.Dictionary(tokenized_documents)

    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    if is_query:
        return corpus, dictionary

    tfidf = models.TfidfModel(corpus)
    vectorized_documents = tfidf[corpus]

    return vectorized_documents, dictionary