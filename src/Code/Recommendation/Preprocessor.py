from typing import List

import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])  # Disable NER also


def Preprocess(texts: List[str], processNumber=1) -> List[List[str]]:
    """
    Preprocesses the given list of texts efficiently.

    Args:
        texts (List[str]): The list of texts to preprocess.
        processNumber (int): The number of processes to use for parallel processing.

    Returns:
        list: A list of preprocessed documents.
    """
    batch_size = 1000  # Adjust for optimal performance

    # Use nlp.pipe for efficient batch processing
    if processNumber == 1:
        docs = list(nlp.pipe(texts, batch_size=batch_size))
    else:
        docs = list(nlp.pipe(texts, batch_size=batch_size, n_process=4))

    # Extract only necessary attributes within the list comprehension
    return [[token.lemma_ for token in doc
             if (token.is_alpha or token.is_digit) and not token.is_stop]
            for doc in docs]
