from flask import Flask
import pickle


# create_app wraps the other functions to set up the project

app = Flask(__name__, static_folder=None)

@app.route("/preference")
def preference():
    """
    source vectorizer and clf for classification
    """
    with open("model_pickles/vectorizer.pkl", "rb") as fl:
        vectorizer = pickle.load(fl)
    with open("model_pickles/clf.pkl", "rb") as fl:
        clf = pickle.load(fl)

    vect_content = vectorizer.fit_transform([input_string])
    prediction = clf.predict(vect_content)[0]
    return {"personal_preference": prediction}
    


if "__main__" == __name__:
    app = create_app()
    
    