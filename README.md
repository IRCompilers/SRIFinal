# SRIFinal

The final project for SRI. This is a simple book recommendation system. It uses a simple search engine to find books that contain the query and then uses a simple recommendation system to recommend books based on the books found.

## Technical

In this section we will discuss the technical details of the project, divided in the main 3 core features: **query**, **autocomplete** and **tagging**.

### Query

The query is the core feature of this recommendation system. It is a simple search engine that given a query will return the books that match the query.

It uses **vectorial search** to find the books that match the query. The vectorial search is done using the **cosine similarity** between the query and the documents. The documents are represented as a vector of the words in the document and the query is represented as a vector of the words in the query. The cosine similarity is then calculated between the query and the documents and the documents with the highest cosine similarity are returned.

But before vectorizing either the queries and the documents it first preprocesses the text. The preprocessing consists of removing the punctuation, removing the stop words and lemmatizing the words. The stop words are the most common words in the English language.

To vectorize the query and the documents it uses the **TF-IDF algorithm**. The TF-IDF algorithm is a measure of the importance of a word in a document. It is calculated as the product of the term frequency and the inverse document frequency. The term frequency is the number of times a word appears in a document and the inverse document frequency is the logarithm of the number of documents divided by the number of documents that contain the word.

The process to vectorize the query is the same, but it leaves the query as a bag of words with the ids of the words, because calculating the IDF for the query would result in 0 values for all the words.

### Autocomplete

The autocomplete is the feature that given that the users has written a part of the word it fills in the result with the most probable word they will write.

The autocomplete is done using a data structure created by yours truly, Hector Rodriguez, called an **MCS-Trie**. This structure is a regular trie with the invariant that every node holds the Most Common Suffix of the words that are in the subtree of that node. This allows for a very efficient way to find the most common suffix of the words that are in the trie.

Given that the corpus has n words and m is the largest word in the corpus, the time complexity of the MCS-Trie is O(m) for insertion and search of single words, and the space complexity is O(nm) for the entire corpus.

With this said, it's easy to say that the autocomplete feature is as simply as performing a PrefixQuery in the MCS-Trie, and returning the Most Common Suffix of the node.

### Tagging

The tagging feature in this project is implemented using a machine learning model, specifically a **OneVsRestClassifier model with SGDClassifier** as the base estimator. This model is part of the `sklearn` library in Python. Here's a more detailed explanation of the process:

1. **Libraries Used**: The main libraries used in this process are `sklearn`, `joblib`, and `typing`. `sklearn` is a machine learning library in Python that provides simple and efficient tools for data analysis and modeling. `joblib` is used for saving and loading the trained model, vectorizer, and MultiLabelBinarizer. `typing` is used for type hinting in Python.

2. **Training the Model**: The `TrainModel` function is used to train the model. The training data consists of book descriptions and their corresponding tags. The tags are converted to a binary matrix using the `MultiLabelBinarizer` from `sklearn.preprocessing`. The book descriptions are converted to TF-IDF vectors using the `TfidfVectorizer` from `sklearn.feature_extraction.text`. The model is trained using the `OneVsRestClassifier` with `SGDClassifier` as the base estimator from `sklearn.multiclass` and `sklearn.linear_model` respectively. The trained model, vectorizer, and MultiLabelBinarizer are saved to disk using `joblib.dump`.

3. **Predicting Tags**: The `PredictTags` function is used to predict tags for a given book description. The trained model, vectorizer, and MultiLabelBinarizer are loaded from disk using `joblib.load`. The book description is converted to a TF-IDF vector and then passed to the model for prediction. The model predicts the binary tags of the book, which are then converted back to the original tag format using `mlb.inverse_transform`.

In essence, the model is learning the relationship between the wording of a book description and the tags that are relevant to it. Once trained, it can predict the tags for a new book description based on what it has learned.