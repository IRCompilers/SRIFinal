from gensim import corpora, models


def Vectorize(tokenized_documents, dictionary=None, is_query=False):
    """
    Vectorizes the given tokenized documents using the TF-IDF model.

    Args:
        tokenized_documents (list): A list of tokenized documents.
        dictionary (gensim.corpora.Dictionary, optional): The dictionary to be used for the vectorization. If None, a new dictionary is created. Defaults to None.
        is_query (bool, optional): A flag indicating whether the documents are a query. If True, the function returns the corpus and the dictionary, without making applying Tf-IDF to the vector. Defaults to False.

    Returns:
        tuple: A tuple containing the vectorized documents and the dictionary used for the vectorization.
    """
    if dictionary is None:
        dictionary = corpora.Dictionary(tokenized_documents)

    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]

    if is_query:
        return corpus, dictionary

    tfidf = models.TfidfModel(corpus)
    vectorized_documents = tfidf[corpus]

    return vectorized_documents, dictionary