from typing import List

import spacy

nlp = spacy.load("en_core_web_sm")


def Tokenize(text: List[str]):
    """
    Tokenize the given list of texts.

    Args:
        text (List[str]): The list of texts to tokenize.

    Returns:
        list: A list of tokenized documents.
    """
    tokenized_documents = []
    for doc in nlp.pipe(text):
        tokenized_documents.append([token for token in doc])

    return tokenized_documents


def RemoveNoise(docs):
    """
    Remove noise from the given documents.

    Args:
        docs (list): The list of documents to remove noise from.

    Returns:
        list: A list of documents with noise removed.
    """
    return [[token for token in doc if token.is_alpha or token.is_digit] for doc in docs]


def RemoveStopWords(docs):
    """
    Remove stop words from the given documents.

    Args:
        docs (list): The list of documents to remove stop words from.

    Returns:
        list: A list of documents with stop words removed.
    """
    return [[token for token in doc if not token.is_stop] for doc in docs]


def Preprocess(texts: List[str]):
    """
    Preprocess the given list of texts.

    Args:
        texts (List[str]): The list of texts to preprocess.

    Returns:
        list: A list of preprocessed documents.
    """
    tokenized_documents = Tokenize(texts)
    tokenized_documents = RemoveNoise(tokenized_documents)
    tokenized_documents = RemoveStopWords(tokenized_documents)
    tokenized_documents = [[token.lemma_ for token in doc] for doc in tokenized_documents]
    return tokenized_documents
