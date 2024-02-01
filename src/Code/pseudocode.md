function createBookRecommendationSystem(documents):
    preprocessed_documents = preprocess(documents)
    tokenized_documents = tokenize(preprocessed_documents)
    vectorized_documents = vectorize(tokenized_documents)
    indexed_data = index(vectorized_documents)
    writeToFile(indexed_data)

function preprocess(documents):
    for each document in documents:
        remove punctuation from document
        convert document to lower case
        remove stop words from document
        stem words in document
    return preprocessed_documents

function tokenize(preprocessed_documents):
    for each document in preprocessed_documents:
        break document into individual words or tokens
    return tokenized_documents

function vectorize(tokenized_documents):
    for each document in tokenized_documents:
        convert tokens in document to numerical vectors using TF-IDF
    return vectorized_documents

function index(vectorized_documents):
    for each document in vectorized_documents:
        store vectors in a way that makes it easy to perform vectorial search
    return indexed_data

function writeToFile(indexed_data):
    open file in write mode
    write indexed_data to file
    close file