from typing import List

import spacy

nlp = spacy.load("en_core_web_sm")


def Tokenize(text: List[str]):
    tokenized_documents = []
    for doc in nlp.pipe(text):
        tokenized_documents.append([token for token in doc])

    return tokenized_documents


def RemoveNoise(docs):
    return [[token for token in doc if token.is_alpha or token.is_digit] for doc in docs]


def RemoveStopWords(docs):
    return [[token for token in doc if not token.is_stop] for doc in docs]


def Preprocess(texts: List[str]):
    tokenized_documents = Tokenize(texts)
    tokenized_documents = RemoveNoise(tokenized_documents)
    tokenized_documents = RemoveStopWords(tokenized_documents)
    tokenized_documents = [[token.lemma_ for token in doc] for doc in tokenized_documents]
    return tokenized_documents
