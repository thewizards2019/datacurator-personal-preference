import requests
import json
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import metrics


def pickle_vectorizer(v, path='model_pickles/vectorizer.pkl'):
        """
        Saves the trained vectorizer for future use.
        """
        with open(path, 'wb') as fl:
            pickle.dump(v, fl)
            print("Pickled vectorizer at {}".format(path))


def pickle_clf(clf, path='model_pickles/clf.pkl'):
        """
        Saves the trained classifier for future use.
        """
        with open(path, 'wb') as fl:
            pickle.dump(clf, fl)
            print("Pickled classifier at {}".format(path))


def build_model():
    """
    on a regular basis reach out to scala api to grab the
    latest training data set, and retrain the model
    """
    # get training set
    training_set = requests.get(url_to_scala_api/training_data)
    training_data = training_set.json()
    if len(training_data) > 0:
        X = [x.get("content") for x in training_data]
        Y = [x.get("tag") for x in training_data]
        
        x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8)
        count_vect = CountVectorizer()
        x_train_counts = count_vect.fit_transform(x_train)
        clf = LogisticRegression(random_state=0).fit(x_train_counts, y_train)
        predictions = clf.predict(count_vect.transform(x_test))
        accuracy = metrics.accuracy_score(y_test, predictions)
        if accuracy > 0.5:
            pickle_vectorizer(count_vect)
            pickle_clf(clf)




if __name__ == "__main__":
    build_model()