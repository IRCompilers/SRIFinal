from typing import List

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

from src.Code.Recommendation.Sampler import get_hardcoded_book_descriptions, get_hardcoded_book_tags


def TrainModel(descriptions: List[str], tags: List[List[str]]):
    """
    Trains a OneVsRestClassifier model with SGDClassifier as the base estimator.

    Args:
        descriptions (list): A list of book descriptions.
        tags (list): A list of lists of book tags.

    Returns:
        tuple: A tuple containing the trained classifier, the TF-IDF vectorizer, and the MultiLabelBinarizer.
    """

    # Convert the tags to a binary matrix
    mlb = MultiLabelBinarizer()
    binary_tags = mlb.fit_transform(tags)

    # Convert the descriptions to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_descriptions = vectorizer.fit_transform(descriptions)

    # Train the model
    classifier = OneVsRestClassifier(SGDClassifier())
    classifier.fit(tfidf_descriptions, binary_tags)

    # Save the trained model, vectorizer, and mlb to disk
    joblib.dump(classifier, 'Resources/classifier.joblib')
    joblib.dump(vectorizer, 'Resources/vectorizer.joblib')
    joblib.dump(mlb, 'Resources/mlb.joblib')

    return classifier, vectorizer, mlb


def PredictTags(description_words: List[str]) -> List[str]:
    """
    Predicts the tags for a given book description.

    Args:
        description_words (list): A list of words in the book description.

    Returns:
        list: A list of predicted tags for the book.
    """
    # Load the trained model, vectorizer, and mlb from disk
    classifier = joblib.load('Resources/classifier.joblib')
    vectorizer = joblib.load('Resources/vectorizer.joblib')
    mlb = joblib.load('Resources/mlb.joblib')

    # Convert the description words into a single string
    new_description = ' '.join(description_words)

    # Convert the new description to a TF-IDF vector
    new_tfidf = vectorizer.transform([new_description])

    # Predict the binary tags of the new book
    predicted_binary_tags = classifier.predict(new_tfidf)

    # Convert the predicted binary tags back to the original tag format
    predicted_tags = mlb.inverse_transform(predicted_binary_tags)

    return predicted_tags
