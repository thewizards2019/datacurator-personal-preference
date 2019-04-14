from flask import Flask
import pickle
import json
import model_rebuilder as ml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


# create_app wraps the other functions to set up the project

app = Flask(__name__, static_folder=None)
@app.route("/preference/<input>")
def preference(input):
    """
    source vectorizer and clf for classification
    """
    print(input)
    try:
        with open("app/model_pickles/vectorizer.pkl", "rb") as fl:
            vectorizer = pickle.load(fl)
        with open("app/model_pickles/clf.pkl", "rb") as fl:
            clf = pickle.load(fl)
        vect_content = vectorizer.transform([input])
        prediction = clf.predict(vect_content)[0]
        return str(prediction)
        # return {"personal": prediction}
    except FileNotFoundError:
        return str(1)


@app.route("/retrain")
def model_builder():
    """
    source vectorizer and clf for classification
    """
    try:
        ml.build_model()
        return "success"
    except:
        return "failed"


if "__main__" == __name__:
    app.run(port=5020)
    
    