from typing import List

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer



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


class Tagger:
    def __init__(self):
        self.classifier = joblib.load('Resources/classifier.joblib')
        self.vectorizer = joblib.load('Resources/vectorizer.joblib')
        self.mlb = joblib.load('Resources/mlb.joblib')

    def PredictTags(self, description_words: List[str]) -> List[str]:
        """
        Predicts the tags for a given book description.

        Args:
            description_words (list): A list of words in the book description.

        Returns:
            list: A list of predicted tags for the book.
        """
        # Convert the description words into a single string
        new_description = ' '.join(description_words)

        # Convert the new description to a TF-IDF vector
        new_tfidf = self.vectorizer.transform([new_description])

        # Predict the binary tags of the new book
        predicted_binary_tags = self.classifier.predict(new_tfidf)

        # Convert the predicted binary tags back to the original tag format
        predicted_tags = self.mlb.inverse_transform(predicted_binary_tags)

        return predicted_tags
